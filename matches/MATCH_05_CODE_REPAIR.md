# Match 5: AI-Powered Code Repository Repair

- **Status:** PLATFORM CONTRACT NOT PUBLISHED · FOUNDATION PREPARATION
- **Points:** 2,100
- **Public objective shown by LabLab:** Build a multi-agent AI system that analyzes code, detects defects, and proposes fixes with minimal human intervention.

## Current platform reality — 2026-11-09

The original AMD AI League schedule announced Match 5 for the period ending around November 10. However, after LabLab's migration to `lablab.build`, the official event page still labels Match 5 as **Coming soon** and exposes no distinct starter kit, grader contract, sample harness, or working Match 5 details route.

No dedicated Match 5 repository or official submission artifact is claimed complete yet.

## InnerOS foundation already available

We do not need to start from zero. Existing InnerOS capabilities map directly to the announced objective:

- Dev Swarm task decomposition and bounded implementation
- ContributorOps / GitLab repair workflows
- isolated worktrees
- deterministic test execution
- evidence-first verification
- rollback and human approval gates
- local Qwen3-Coder inference on AMD Radeon AI PRO R9700
- persistent coordination through MongoDB / Temporal / MCP / NATS

## Preparation boundary

Until AMD/LabLab publishes an official Match 5 contract, work should stay contract-agnostic:

1. defect discovery
2. repair-plan generation
3. isolated patch application
4. targeted tests
5. regression verification
6. evidence receipt
7. rollback on failed verification

Do **not** invent a grader schema, Docker entrypoint, output JSON contract, or official score.

## Next gate

The moment an official Match 5 starter kit or grader contract appears, adapt the existing InnerOS code-repair loop to that exact contract, build the challenge container, run it on AMD, publish the artifact, and submit it.
