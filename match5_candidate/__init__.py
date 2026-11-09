"""Contract-agnostic Match 5 code-repair foundation."""

from .repair_pipeline import (
    EvidenceReceipt,
    RepairPlan,
    RepositoryRepairPipeline,
    TextReplacementRepair,
)

__all__ = [
    "EvidenceReceipt",
    "RepairPlan",
    "RepositoryRepairPipeline",
    "TextReplacementRepair",
]
