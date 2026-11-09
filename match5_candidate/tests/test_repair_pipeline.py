from __future__ import annotations

import json
import sys
from pathlib import Path

from match5_candidate.repair_pipeline import RepairPlan, RepositoryRepairPipeline, TextReplacementRepair


def _fixture(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    (repo / "calc.py").write_text("def add(a, b):\n    return a - b\n", encoding="utf-8")
    (repo / "test_calc.py").write_text(
        "from calc import add\n\n"
        "def test_add():\n"
        "    assert add(2, 3) == 5\n",
        encoding="utf-8",
    )
    return repo


def test_verified_repair_produces_evidence(tmp_path: Path):
    repo = _fixture(tmp_path)
    pipeline = RepositoryRepairPipeline()
    action = TextReplacementRepair("calc.py", "return a - b", "return a + b")

    receipt = pipeline.run(repo, action, test_commands=[[sys.executable, "-m", "pytest", "-q"]])

    assert receipt.status == "VERIFIED"
    assert receipt.changed_files == ["calc.py"]
    assert receipt.before_sha256["calc.py"] != receipt.after_sha256["calc.py"]
    assert receipt.tests[0]["returncode"] == 0
    assert json.loads(receipt.to_json())["status"] == "VERIFIED"
    # Source checkout is untouched because work happens in an isolated copy.
    assert "return a - b" in (repo / "calc.py").read_text(encoding="utf-8")


def test_failed_verification_rolls_back_and_preserves_source(tmp_path: Path):
    repo = _fixture(tmp_path)
    pipeline = RepositoryRepairPipeline()
    action = TextReplacementRepair("calc.py", "return a - b", "return a * b")

    receipt = pipeline.run(repo, action, test_commands=[[sys.executable, "-m", "pytest", "-q"]])

    assert receipt.status == "ROLLED_BACK"
    assert "verification failed" in receipt.error
    assert "return a - b" in (repo / "calc.py").read_text(encoding="utf-8")


def test_path_escape_fails_closed(tmp_path: Path):
    repo = _fixture(tmp_path)
    pipeline = RepositoryRepairPipeline()
    action = TextReplacementRepair("../outside.py", "x", "y")

    receipt = pipeline.run(repo, action, test_commands=[])

    assert receipt.status == "ROLLED_BACK"
    assert "escapes repair workspace" in receipt.error


def test_unplanned_file_change_is_rejected(tmp_path: Path):
    repo = _fixture(tmp_path)
    pipeline = RepositoryRepairPipeline()

    class BadRepair:
        plan = RepairPlan(summary="bad", target_files=("calc.py",))

        def apply(self, workspace: Path) -> None:
            (workspace / "calc.py").write_text("def add(a,b): return a+b\n", encoding="utf-8")
            (workspace / "test_calc.py").write_text("# tampered\n", encoding="utf-8")

    receipt = pipeline.run(repo, BadRepair(), test_commands=[])

    assert receipt.status == "ROLLED_BACK"
    assert "outside plan" in receipt.error
