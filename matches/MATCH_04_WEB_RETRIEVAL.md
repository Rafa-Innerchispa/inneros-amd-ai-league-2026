# Match 4: Intelligent Web Information Retrieval

- **Status:** ACTIVE DEVELOPMENT
- **Human Task ID:** `MATCH4-WEB-RETRIEVAL`
- **Canonical Repository:** [Rafa-Innerchispa/amd-academy-mc4-web-retrieval](https://github.com/Rafa-Innerchispa/amd-academy-mc4-web-retrieval)
- **Development Branch:** `chatgpt/mc4-core-20261019`
- **Draft PR:** [#2](https://github.com/Rafa-Innerchispa/amd-academy-mc4-web-retrieval/pull/2)

## Capability under validation

A bounded, evidence-first web retrieval agent that accepts a natural-language request, navigates relevant pages, extracts the specific requested value, verifies it against the source, and fails closed when the evidence is insufficient.

Current implementation includes:

- URL + anchor-aware bounded navigation
- exact-value extraction from text, HTML tables and JSON-LD
- price/date/version/contact/hours/count/person/spec retrieval
- provenance and SHA-256 snapshot evidence
- fail-closed verification
- URL/redirect safety controls
- provisional `/app/app.py` grader adapter
- optional keyless public-web discovery in the demo path
- isolated demo UI
- provisional AMD ROCm container baseline

## Development evidence

Current local functional validation:

- **37 tests passed**
- Python compileall: **PASS**
- offline held-out harness: **9/9 PASS**
- exact-case accuracy: **1.0**

These are local development results, not official Match 4 grader results and not AMD GPU performance measurements.

## Promotion gate

This Match remains **ACTIVE DEVELOPMENT**, not VERIFIED.

Promotion requires the official Match 4 contract/starter kit, official sample/selfcheck pass, AMD physical container validation, public image + anonymous pull/re-run, immutable digest, and a confirmed LabLab submission route.
