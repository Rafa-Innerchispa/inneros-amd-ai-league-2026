# InnerOS Integration & Graduation Lifecycle

## Overview

The InnerOS platform ingests independently validated challenge capabilities through a formal, four-phase graduation pipeline:

```
[Challenge Sandbox (Match Repo)]
                |
                v
    Phase 1: Isolated Validation (PyTest + Docker Build)
                |
                v
    Phase 2: Hardware Attestation (AMD R9700 Physical Soak)
                |
                v
    Phase 3: Protocol Compliance (InnerOS Agent Card & MCP Tool)
                |
                v
[InnerOS Production Swarm (Governed Runtime)]
```

## Policy Safeguards
- **Zero Accidental Regression:** Challenge repos are frozen upon submission (e.g. `inneros-amd-act-iii` SHA `a1b4520921c5198e1444edcb1b8569e00eb4f7a7`).
- **Cryptographic Provenance:** Every graduate image is referenced by immutable SHA256 digest in Google Artifact Registry.
