"""
Path Definitions for Skill-Forge

Paths are thematic groupings of domains that represent coherent skill bundles.
"""

from dataclasses import dataclass
from typing import List, Dict, Set


@dataclass
class PathDefinition:
    """Definition of a learning path across domains."""
    id: str
    name: str
    description: str
    domains: List[int]  # Domain numbers (1-7)
    level_required: str  # "foundation", "practice", or "mastery"
    unlocks: str  # What this path unlocks


PATHS: Dict[str, PathDefinition] = {
    "theory-builder": PathDefinition(
        id="theory-builder",
        name="Theory Builder",
        description="Build theory from data: find patterns, position contributions, frame arguments, match genre",
        domains=[1, 2, 4, 5],
        level_required="mastery",
        unlocks="Full theory-building pipeline in theory-forge"
    ),
    "evidence-analyst": PathDefinition(
        id="evidence-analyst",
        name="Evidence Analyst",
        description="Deep evidence work: find patterns, extract mechanisms, handle disconfirmation",
        domains=[1, 3, 6],
        level_required="mastery",
        unlocks="Advanced qualitative analysis tools"
    ),
    "integrity-guardian": PathDefinition(
        id="integrity-guardian",
        name="Integrity Guardian",
        description="Research integrity: adversarial evidence handling and claim verification",
        domains=[6, 7],
        level_required="mastery",
        unlocks="Self-audit and verification tools"
    ),
    "full-researcher": PathDefinition(
        id="full-researcher",
        name="Full Researcher",
        description="Complete mastery across all seven research competency domains",
        domains=[1, 2, 3, 4, 5, 6, 7],
        level_required="mastery",
        unlocks="Unrestricted access to all theory-forge capabilities"
    ),
}


def check_path_completion(completed_requirements: Set[str], path_id: str) -> dict:
    """Check progress on a specific path.

    Args:
        completed_requirements: Set like {"domain-1:mastery", "domain-2:foundation"}
        path_id: The path to check

    Returns:
        Dict with:
        - complete: bool
        - progress: float (0.0 to 1.0)
        - completed_domains: list
        - remaining_domains: list
    """
    if path_id not in PATHS:
        return {"error": f"Unknown path: {path_id}"}

    path = PATHS[path_id]
    level = path.level_required

    completed_domains = []
    remaining_domains = []

    for domain_num in path.domains:
        req = f"domain-{domain_num}:{level}"
        if req in completed_requirements:
            completed_domains.append(domain_num)
        else:
            remaining_domains.append(domain_num)

    return {
        "complete": len(remaining_domains) == 0,
        "progress": len(completed_domains) / len(path.domains),
        "completed_domains": completed_domains,
        "remaining_domains": remaining_domains,
        "unlocks": path.unlocks if len(remaining_domains) == 0 else None
    }


def check_all_paths(completed_requirements: Set[str]) -> Dict[str, dict]:
    """Check progress on all paths."""
    return {
        path_id: check_path_completion(completed_requirements, path_id)
        for path_id in PATHS
    }


def format_path_progress(completed_requirements: Set[str]) -> str:
    """Format path progress for display."""
    lines = ["PATH PROGRESS", "═" * 60]

    for path_id, path in PATHS.items():
        status = check_path_completion(completed_requirements, path_id)
        pct = status["progress"] * 100

        # Progress bar
        bar_filled = int(pct / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)

        if status["complete"]:
            lines.append(f"✅ {path.name}: COMPLETE")
            lines.append(f"   → Unlocked: {path.unlocks}")
        else:
            done = len(status["completed_domains"])
            total = len(path.domains)
            lines.append(f"◐ {path.name}: {bar} {done}/{total} domains at {path.level_required}")

            # Show what's remaining
            remaining = [f"D{d}" for d in status["remaining_domains"]]
            lines.append(f"   Remaining: {', '.join(remaining)}")

        lines.append("")  # Blank line between paths

    return "\n".join(lines)
