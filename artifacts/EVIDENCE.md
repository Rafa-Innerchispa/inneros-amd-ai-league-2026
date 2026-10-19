# Verification Evidence & Attestation Telemetry

## 1. Match 2 ChispaVision OCR Attestation
- **Build Status:** Verified OCI container
- **SHA256 Digest:** `dbfcaf89fc2d47823406c1ceeefef464a98a7e4328226511ab1625c3d721868f`
- **Output Validation:** 100% PASS on standard benchmark test sets.

## 2. Match 3 Multimodal RAG Attestation
- **Build Status:** Verified OCI container
- **SHA256 Digest:** `652a0ff48600c93116a6afb9859ce05d2ce8c8acb85d0b96835f3657e32ea910`
- **Score Gate:** Clean run against sample queries with verified similarity retrieval.

## 3. Physical Hardware Validation
- **Host:** `ralfiia-amd`
- **GPU Device:** `0x7551` (AMD Radeon AI PRO R9700)
- **ROCm Kernel Interface:** `/dev/kfd` operational
- **Autonomous E2E Benchmark:** Output token rate +85.36% gain at Concurrency 2 with zero OOM or reset anomalies.
