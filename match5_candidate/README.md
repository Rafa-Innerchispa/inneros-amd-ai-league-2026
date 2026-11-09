# Match 5 Candidate Foundation — Code Repository Repair

This directory is a **contract-agnostic engineering foundation** for the AMD AI League Match 5 theme shown publicly by LabLab: AI-Powered Code Repository Repair.

It is intentionally **not** an official Match 5 submission implementation yet. As of 2026-11-09, LabLab's migrated `lablab.build` event page still shows Match 5 as “Coming soon” and does not expose an official starter kit or grader contract.

## What is implemented

The reusable safety core already supports:

1. bounded repository snapshotting with SHA-256 evidence;
2. an explicit structured repair plan;
3. repair execution inside an isolated temporary copy;
4. enforcement that only planned files may change;
5. shell-free targeted test execution with timeouts;
6. fail-closed rollback semantics when verification fails;
7. before/after hashes and test evidence in a machine-readable receipt.

A deterministic `TextReplacementRepair` adapter exists only to exercise the core in tests. The future official adapter can replace it with local AMD/Qwen3-Coder planning without changing the safety boundary.

## Run tests

```bash
python3 -m pytest -q match5_candidate/tests
```

## Truth boundary

This code does **not** claim:

- an official AMD/LabLab Match 5 input/output contract;
- an official Docker entrypoint;
- an official hidden-set score;
- a published final challenge image;
- prize eligibility.

Those fields remain blocked until LabLab publishes the actual Match 5 contract.
