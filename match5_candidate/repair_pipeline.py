from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tempfile
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable, Protocol, Sequence


DEFAULT_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".json", ".toml", ".yaml", ".yml", ".md"
}


@dataclass(frozen=True)
class RepairPlan:
    summary: str
    target_files: tuple[str, ...]
    rationale: str = ""


@dataclass
class EvidenceReceipt:
    status: str
    plan: RepairPlan
    tests: list[dict] = field(default_factory=list)
    before_sha256: dict[str, str] = field(default_factory=dict)
    after_sha256: dict[str, str] = field(default_factory=dict)
    changed_files: list[str] = field(default_factory=list)
    error: str | None = None

    def to_json(self) -> str:
        payload = asdict(self)
        return json.dumps(payload, sort_keys=True, indent=2)


class RepairAction(Protocol):
    plan: RepairPlan

    def apply(self, workspace: Path) -> None:
        ...


@dataclass(frozen=True)
class TextReplacementRepair:
    relative_path: str
    old: str
    new: str
    summary: str = "Replace a known defective fragment"

    @property
    def plan(self) -> RepairPlan:
        return RepairPlan(
            summary=self.summary,
            target_files=(self.relative_path,),
            rationale="Deterministic replacement adapter used for contract-independent validation.",
        )

    def apply(self, workspace: Path) -> None:
        target = _safe_join(workspace, self.relative_path)
        original = target.read_text(encoding="utf-8")
        if self.old not in original:
            raise ValueError(f"expected fragment not found in {self.relative_path}")
        target.write_text(original.replace(self.old, self.new, 1), encoding="utf-8")


class RepositoryRepairPipeline:
    """Bounded repair executor with isolation, verification, evidence, and fail-closed semantics.

    The pipeline deliberately has no AMD/LabLab grader assumptions. A future challenge adapter can
    translate an official input contract into a RepairAction and map EvidenceReceipt to the required
    output schema without changing the repair safety core.
    """

    def __init__(
        self,
        *,
        allowed_extensions: Iterable[str] = DEFAULT_EXTENSIONS,
        max_files: int = 500,
        test_timeout_seconds: int = 60,
    ) -> None:
        self.allowed_extensions = frozenset(allowed_extensions)
        self.max_files = max_files
        self.test_timeout_seconds = test_timeout_seconds

    def run(
        self,
        source_repo: Path | str,
        action: RepairAction,
        *,
        test_commands: Sequence[Sequence[str]],
    ) -> EvidenceReceipt:
        source = Path(source_repo).resolve()
        if not source.is_dir():
            raise ValueError("source_repo must be an existing directory")

        before = self._snapshot(source)
        receipt = EvidenceReceipt(status="STARTED", plan=action.plan, before_sha256=before)

        with tempfile.TemporaryDirectory(prefix="inneros-mc5-") as tmp:
            workspace = Path(tmp) / "repo"
            shutil.copytree(source, workspace, symlinks=False)

            try:
                action.apply(workspace)
                after_apply = self._snapshot(workspace)
                changed = sorted(
                    path for path in set(before) | set(after_apply)
                    if before.get(path) != after_apply.get(path)
                )
                unexpected = sorted(set(changed) - set(action.plan.target_files))
                if unexpected:
                    raise RuntimeError(f"repair changed files outside plan: {unexpected}")

                receipt.changed_files = changed
                for argv in test_commands:
                    result = self._run_test(workspace, argv)
                    receipt.tests.append(result)
                    if result["returncode"] != 0:
                        receipt.status = "ROLLED_BACK"
                        receipt.error = f"verification failed: {' '.join(argv)}"
                        return receipt

                receipt.after_sha256 = after_apply
                receipt.status = "VERIFIED"
                return receipt
            except Exception as exc:
                receipt.status = "ROLLED_BACK"
                receipt.error = str(exc)
                return receipt

    def _snapshot(self, root: Path) -> dict[str, str]:
        entries: dict[str, str] = {}
        files = [p for p in root.rglob("*") if p.is_file() and p.suffix in self.allowed_extensions]
        if len(files) > self.max_files:
            raise ValueError(f"repository exceeds max_files={self.max_files}")
        for path in sorted(files):
            if path.is_symlink():
                raise ValueError(f"symlinked file rejected: {path}")
            rel = path.relative_to(root).as_posix()
            entries[rel] = hashlib.sha256(path.read_bytes()).hexdigest()
        return entries

    def _run_test(self, workspace: Path, argv: Sequence[str]) -> dict:
        if not argv:
            raise ValueError("test command must not be empty")
        if any("\x00" in item for item in argv):
            raise ValueError("invalid NUL in test command")
        proc = subprocess.run(
            list(argv),
            cwd=workspace,
            capture_output=True,
            text=True,
            timeout=self.test_timeout_seconds,
            check=False,
            shell=False,
        )
        return {
            "argv": list(argv),
            "returncode": proc.returncode,
            "stdout": proc.stdout[-4000:],
            "stderr": proc.stderr[-4000:],
        }


def _safe_join(root: Path, relative_path: str) -> Path:
    candidate = (root / relative_path).resolve()
    try:
        candidate.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError("path escapes repair workspace") from exc
    if not candidate.is_file():
        raise ValueError(f"target is not a file: {relative_path}")
    return candidate
