# InnerOS Architecture on AMD: Governed Agentic Intelligence

## 1. System Vision

InnerOS is designed as a sovereign, local-first operating system for autonomous AI agents. Unlike standard agent frameworks that rely exclusively on cloud APIs and unverified local execution, InnerOS enforces strict governance, cryptographic attestation, durable workflow state (via Temporal and MongoDB), and high-throughput physical acceleration on AMD Radeon hardware.

## 2. Layered Architecture

```
+-----------------------------------------------------------------+
|                        Evaluation & UI Layer                     |
|  - Hackathon Judge Dashboards                                   |
|  - ChispaVision Web Interface (:8080)                           |
|  - MC3 Multimodal RAG Explorer (:8501)                          |
+-----------------------------------------------------------------+
                                |
+-----------------------------------------------------------------+
|                     InnerOS Governance Plane                    |
|  - Coordination State Engine (Revision Control / State Projections)|
|  - Agent Mailbox Protocol (Mongo ralfia_agent_messages)         |
|  - Resource Attribution & Immutable Branch Freeze               |
|  - Autonomy Policy (question_budget=0, bounded error recovery)   |
+-----------------------------------------------------------------+
                                |
+-----------------------------------------------------------------+
|                  Execution & Orchestration Fabric                |
|  - Temporal Durable Workflows                                   |
|  - Isolated Git Worktrees (/var/local_execution/worktrees)      |
|  - Autonomous Agent Roles (Antigravity, Cursor, Codex, ChatGPT) |
+-----------------------------------------------------------------+
                                |
+-----------------------------------------------------------------+
|                  AMD Hardware & Accelerated Inference            |
|  - Physical GPU: AMD Radeon AI PRO R9700 (gfx1201 / 32GB VRAM)  |
|  - Driver: ROCm 10.1 native kernel interfaces (/dev/kfd)       |
|  - Inference Engines: vLLM v0.32 + AWQ / WNA16 Triton Kernels  |
|  - Containerization: OCI compliant containers on containerd     |
+-----------------------------------------------------------------+
```

## 3. Challenge Sandboxing & Graduation

Every Match in the AMD AI League represents a modular capability:
1. **Perception (Match 2):** OCR & document parsing via ChispaVision.
2. **Context & Retrieval (Match 3 & 4):** Vector-based multimodal search and external web grounding.
3. **Execution & Self-Healing (Match 5):** Automated AST inspection and test repair.
4. **Coordination (Match 6):** Autonomous multi-agent coordination.

Each component is developed and proven in an isolated repository before being bound to InnerOS capabilities.
