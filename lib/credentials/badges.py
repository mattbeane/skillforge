"""
Badge Definitions for Skill-Forge

Three types of badges:
1. Domain badges (21 total: 7 domains × 3 levels)
2. Path badges (thematic groupings across domains)
3. Capstone badge (AI Supervisor certification)
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum


class BadgeType(Enum):
    DOMAIN = "domain"
    PATH = "path"
    CAPSTONE = "capstone"


class Level(Enum):
    FOUNDATION = "foundation"
    PRACTICE = "practice"
    MASTERY = "mastery"


@dataclass
class BadgeDefinition:
    """Definition of a badge that can be earned."""
    id: str
    name: str
    type: BadgeType
    description: str
    requirements: List[str]  # List of requirement IDs (e.g., "domain-1:mastery")
    emoji: str = "🎖️"

    def check_requirements(self, completed: set) -> bool:
        """Check if all requirements are met."""
        return all(req in completed for req in self.requirements)


# Domain badges - one for each level of each domain
DOMAIN_BADGES: Dict[str, BadgeDefinition] = {
    # Domain 1: Pattern Recognition
    "foundation-d1": BadgeDefinition(
        id="foundation-d1",
        name="Foundation: Pattern Recognition",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of pattern recognition concepts",
        requirements=["domain-1:foundation"],
        emoji="🔍"
    ),
    "practice-d1": BadgeDefinition(
        id="practice-d1",
        name="Practice: Pattern Recognition",
        type=BadgeType.DOMAIN,
        description="Applied pattern recognition skills with feedback",
        requirements=["domain-1:practice"],
        emoji="🔍"
    ),
    "mastery-d1": BadgeDefinition(
        id="mastery-d1",
        name="Mastery: Pattern Recognition",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent pattern recognition ability",
        requirements=["domain-1:mastery"],
        emoji="🔍"
    ),

    # Domain 2: Theoretical Positioning
    "foundation-d2": BadgeDefinition(
        id="foundation-d2",
        name="Foundation: Theoretical Positioning",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of theoretical positioning",
        requirements=["domain-2:foundation"],
        emoji="🎯"
    ),
    "practice-d2": BadgeDefinition(
        id="practice-d2",
        name="Practice: Theoretical Positioning",
        type=BadgeType.DOMAIN,
        description="Applied theoretical positioning skills with feedback",
        requirements=["domain-2:practice"],
        emoji="🎯"
    ),
    "mastery-d2": BadgeDefinition(
        id="mastery-d2",
        name="Mastery: Theoretical Positioning",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent theoretical positioning ability",
        requirements=["domain-2:mastery"],
        emoji="🎯"
    ),

    # Domain 3: Qualitative Mechanism
    "foundation-d3": BadgeDefinition(
        id="foundation-d3",
        name="Foundation: Qualitative Mechanism",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of mechanism extraction",
        requirements=["domain-3:foundation"],
        emoji="⚙️"
    ),
    "practice-d3": BadgeDefinition(
        id="practice-d3",
        name="Practice: Qualitative Mechanism",
        type=BadgeType.DOMAIN,
        description="Applied mechanism extraction skills with feedback",
        requirements=["domain-3:practice"],
        emoji="⚙️"
    ),
    "mastery-d3": BadgeDefinition(
        id="mastery-d3",
        name="Mastery: Qualitative Mechanism",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent mechanism extraction ability",
        requirements=["domain-3:mastery"],
        emoji="⚙️"
    ),

    # Domain 4: Theoretical Framing
    "foundation-d4": BadgeDefinition(
        id="foundation-d4",
        name="Foundation: Theoretical Framing",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of framing strategies",
        requirements=["domain-4:foundation"],
        emoji="🖼️"
    ),
    "practice-d4": BadgeDefinition(
        id="practice-d4",
        name="Practice: Theoretical Framing",
        type=BadgeType.DOMAIN,
        description="Applied framing skills with feedback",
        requirements=["domain-4:practice"],
        emoji="🖼️"
    ),
    "mastery-d4": BadgeDefinition(
        id="mastery-d4",
        name="Mastery: Theoretical Framing",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent framing ability",
        requirements=["domain-4:mastery"],
        emoji="🖼️"
    ),

    # Domain 5: Epistemological Genre
    "foundation-d5": BadgeDefinition(
        id="foundation-d5",
        name="Foundation: Epistemological Genre",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of discovery vs. testing",
        requirements=["domain-5:foundation"],
        emoji="📜"
    ),
    "practice-d5": BadgeDefinition(
        id="practice-d5",
        name="Practice: Epistemological Genre",
        type=BadgeType.DOMAIN,
        description="Applied genre discipline with feedback",
        requirements=["domain-5:practice"],
        emoji="📜"
    ),
    "mastery-d5": BadgeDefinition(
        id="mastery-d5",
        name="Mastery: Epistemological Genre",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent genre mastery",
        requirements=["domain-5:mastery"],
        emoji="📜"
    ),

    # Domain 6: Adversarial Evidence
    "foundation-d6": BadgeDefinition(
        id="foundation-d6",
        name="Foundation: Adversarial Evidence",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of disconfirming evidence",
        requirements=["domain-6:foundation"],
        emoji="⚔️"
    ),
    "practice-d6": BadgeDefinition(
        id="practice-d6",
        name="Practice: Adversarial Evidence",
        type=BadgeType.DOMAIN,
        description="Applied adversarial evidence handling with feedback",
        requirements=["domain-6:practice"],
        emoji="⚔️"
    ),
    "mastery-d6": BadgeDefinition(
        id="mastery-d6",
        name="Mastery: Adversarial Evidence",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent adversarial evidence handling",
        requirements=["domain-6:mastery"],
        emoji="⚔️"
    ),

    # Domain 7: Claim Verification
    "foundation-d7": BadgeDefinition(
        id="foundation-d7",
        name="Foundation: Claim Verification",
        type=BadgeType.DOMAIN,
        description="Demonstrated understanding of claim-evidence calibration",
        requirements=["domain-7:foundation"],
        emoji="✅"
    ),
    "practice-d7": BadgeDefinition(
        id="practice-d7",
        name="Practice: Claim Verification",
        type=BadgeType.DOMAIN,
        description="Applied verification skills with feedback",
        requirements=["domain-7:practice"],
        emoji="✅"
    ),
    "mastery-d7": BadgeDefinition(
        id="mastery-d7",
        name="Mastery: Claim Verification",
        type=BadgeType.DOMAIN,
        description="Demonstrated independent claim verification ability",
        requirements=["domain-7:mastery"],
        emoji="✅"
    ),
}


# Path badges - thematic groupings
PATH_BADGES: Dict[str, BadgeDefinition] = {
    "theory-builder": BadgeDefinition(
        id="theory-builder",
        name="Theory Builder",
        type=BadgeType.PATH,
        description="Mastered theory-building competencies: pattern recognition, positioning, framing, and genre",
        requirements=[
            "domain-1:mastery",
            "domain-2:mastery",
            "domain-4:mastery",
            "domain-5:mastery"
        ],
        emoji="🏗️"
    ),
    "evidence-analyst": BadgeDefinition(
        id="evidence-analyst",
        name="Evidence Analyst",
        type=BadgeType.PATH,
        description="Mastered evidence-focused competencies: patterns, mechanisms, and adversarial analysis",
        requirements=[
            "domain-1:mastery",
            "domain-3:mastery",
            "domain-6:mastery"
        ],
        emoji="🔬"
    ),
    "integrity-guardian": BadgeDefinition(
        id="integrity-guardian",
        name="Integrity Guardian",
        type=BadgeType.PATH,
        description="Mastered research integrity competencies: adversarial evidence and claim verification",
        requirements=[
            "domain-6:mastery",
            "domain-7:mastery"
        ],
        emoji="🛡️"
    ),
    "full-researcher": BadgeDefinition(
        id="full-researcher",
        name="Full Researcher",
        type=BadgeType.PATH,
        description="Mastered all seven research competency domains",
        requirements=[
            "domain-1:mastery",
            "domain-2:mastery",
            "domain-3:mastery",
            "domain-4:mastery",
            "domain-5:mastery",
            "domain-6:mastery",
            "domain-7:mastery"
        ],
        emoji="🎓"
    ),
}


# Capstone badge
CAPSTONE_BADGE = BadgeDefinition(
    id="ai-supervisor",
    name="AI Supervisor",
    type=BadgeType.CAPSTONE,
    description="Certified to supervise AI research tools. Passed the capstone: reviewing AI-generated research and catching all critical issues.",
    requirements=[
        "domain-1:mastery",
        "domain-2:mastery",
        "domain-3:mastery",
        "domain-4:mastery",
        "domain-5:mastery",
        "domain-6:mastery",
        "domain-7:mastery",
        "capstone:passed"
    ],
    emoji="🤖"
)


# Combined lookup
ALL_BADGES: Dict[str, BadgeDefinition] = {
    **DOMAIN_BADGES,
    **PATH_BADGES,
    "ai-supervisor": CAPSTONE_BADGE,
}


def get_badge_by_id(badge_id: str) -> Optional[BadgeDefinition]:
    """Get a badge definition by ID."""
    return ALL_BADGES.get(badge_id)


def get_available_badges(completed: set) -> List[BadgeDefinition]:
    """Get all badges the student has earned based on completed requirements."""
    return [
        badge for badge in ALL_BADGES.values()
        if badge.check_requirements(completed)
    ]


def get_next_badges(completed: set) -> List[tuple]:
    """Get badges that are partially complete and what's needed.

    Returns list of (badge, remaining_requirements) tuples.
    """
    result = []
    for badge in ALL_BADGES.values():
        if badge.check_requirements(completed):
            continue  # Already earned
        remaining = [r for r in badge.requirements if r not in completed]
        if len(remaining) < len(badge.requirements):
            # Partially complete
            result.append((badge, remaining))
    return result
