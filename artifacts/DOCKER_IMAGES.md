# Official Docker Artifacts Catalog

All container images are built, tested, and published to Google Artifact Registry with public read access.

| Image Name | Tag | Digest (SHA256) | Ports | Purpose |
| :--- | :--- | :--- | :---: | :--- |
| `chispavision-mc2` | `final-512` | `sha256:dbfcaf89fc2d47823406c1ceeefef464a98a7e4328226511ab1625c3d721868f` | 8080 | Match 2 Vision OCR Service |
| `amd-academy-mc3-rag` | `mc3-final` | `sha256:652a0ff48600c93116a6afb9859ce05d2ce8c8acb85d0b96835f3657e32ea910` | 8501 | Match 3 Multimodal RAG Service |

### Pull and Inspection Recipes

```bash
# Pull Match 2
docker pull us-central1-docker.pkg.dev/innerops-agentic-platform/amd-academy-public/chispavision-mc2:final-512

# Pull Match 3
docker pull us-central1-docker.pkg.dev/innerops-agentic-platform/amd-academy-public/amd-academy-mc3-rag:mc3-final
```
