# AMD Stack & Hardware Attestation

## 1. Hardware Specifications

- **Device Name:** AMD Radeon AI PRO R9700
- **Device ID:** `0x7551`
- **Architecture:** RDNA4 (`gfx1201`)
- **Compute Units:** 64 CU
- **Memory:** 32 GiB GDDR6 VRAM
- **Host System:** `ralfiia-amd` (Ubuntu 24.04 LTS Kernel 6.8.0-amd64)
- **Node Access:** `/dev/kfd` and `/dev/dri` passed into privileged OCI containers

## 2. ROCm 10.0 / 10.1 Driver & Software Matrix

| Component | Target / Current Version | Support Notes |
| :--- | :--- | :--- |
| **AMD ROCm** | 10.0 / 10.1 Native | Native `gfx1201` support; obsolete legacy RDNA3 workarounds retired |
| **PyTorch** | 2.13.0 / 2.14.0+rocm10 | Verified in `rocm/pytorch:rocm10.0_ubuntu26.04_py3.14_pytorch_release_2.13.0` |
| **vLLM** | v0.29.0 (Stock) / v0.32.0 (Candidate) | AWQ Triton acceleration kernels |
| **Triton** | 3.0+ AMD Backend | Optimized wave dispatch (`GPU_MAX_HW_QUEUES=1`) |

## 3. Empirical Concurrency Benchmark (R9700 Physical Validation)

Recorded on `QuantTrio/Qwen3-Coder-30B-A3B-Instruct-AWQ` on AMD Radeon AI PRO R9700:

| Concurrency Level | Aggregate Throughput | Gain vs C1 Baseline | Median p95 Latency | Verdict |
| :---: | :---: | :---: | :---: | :---: |
| **C1** | 18.92 tok/s | Baseline | 860 ms | PASS |
| **C2** | 35.07 tok/s | **+85.36%** | 980 ms (p95 ratio: 1.14) | **KEEP** |

- **Single-Stream Determinism:** Enforced via `GPU_MAX_HW_QUEUES=1` to prevent wave starvation.
- **Prefix Warmup:** Zero cold-start latency JIT compilation overhead.
