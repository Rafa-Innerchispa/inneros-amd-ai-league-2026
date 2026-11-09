# Match 4: Intelligent Web Information Retrieval

- **Status:** IMPLEMENTATION COMPLETE · PLATFORM SUBMISSION RECOVERY PENDING
- **Human Task ID:** `MATCH4-WEB-RETRIEVAL`
- **Canonical Repository:** [Rafa-Innerchispa/amd-academy-mc4-web-retrieval](https://github.com/Rafa-Innerchispa/amd-academy-mc4-web-retrieval)
- **Final Branch:** `main`
- **Final Commit:** `0780101a8a4098063b7fbc743430b6e23a244019`

## Capability

A bounded, evidence-first web retrieval agent that accepts a natural-language request, navigates relevant pages, extracts the specific requested value, verifies it against the source, and fails closed when evidence is insufficient.

## Verified engineering evidence

Completed before the original Match 4 deadline:

- **74/74 tests PASS**
- core benchmark: **16/16 PASS**
- adversarial benchmark: **30/30 PASS**
- physical AMD Radeon AI PRO R9700 / `gfx1201`
- production ROCm 10.1 runtime verified
- ROCm 10.1 engineering container build: **PASS**
- `--network none` smoke: **PASS**
- agent import inside container: **PASS**
- public GitHub repository available

These are engineering validation results, not an official hidden-set AMD grader score.

## LabLab platform state

The original Match 4 submission/editing flow was inaccessible during the final submission window. A support escalation was sent to LabLab on 2026-10-31 with the completed public repository and evidence.

As of 2026-11-09:

- LabLab has migrated its public home from `lablab.ai` to `lablab.build`.
- The new AMD AI League page still incorrectly shows Match 4 as **Live** and Match 5 as **Coming soon**, despite the original schedule.
- No reply has been received to the Match 4 support escalation.
- The official FAQ states that closed Matches remain playable for points even after prize eligibility ends.

## Current action

Treat Match 4 as **technically complete** and preserve all evidence. The remaining action is platform-side: attach/accept the completed submission for points or reopen the authenticated submission route.
