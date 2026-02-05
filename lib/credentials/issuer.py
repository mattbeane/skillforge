"""
Badge Issuing Logic for Skill-Forge

Handles checking eligibility and issuing badges to students.
"""

import uuid
from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
import json
from pathlib import Path

from .badges import (
    BadgeDefinition,
    ALL_BADGES,
    DOMAIN_BADGES,
    PATH_BADGES,
    CAPSTONE_BADGE,
    get_available_badges
)


@dataclass
class IssuedBadge:
    """A badge that has been issued to a student."""
    badge_id: str
    name: str
    type: str
    description: str
    emoji: str
    issued_at: str  # ISO format
    issuer: str  # "system" or advisor email
    student_id: str
    verification_url: str

    def to_dict(self) -> dict:
        return {
            "badge_id": self.badge_id,
            "name": self.name,
            "type": self.type,
            "description": self.description,
            "emoji": self.emoji,
            "issued_at": self.issued_at,
            "issuer": self.issuer,
            "student_id": self.student_id,
            "verification_url": self.verification_url
        }

    @classmethod
    def from_dict(cls, data: dict) -> "IssuedBadge":
        return cls(**data)


def generate_badge_uuid() -> str:
    """Generate a unique badge ID."""
    return f"b-{uuid.uuid4()}"


def generate_verification_url(badge_uuid: str) -> str:
    """Generate verification URL for a badge."""
    return f"https://skill-forge.dev/verify/{badge_uuid}"


def get_completed_requirements(student_record: dict) -> set:
    """Extract completed requirements from student record.

    Returns set like {"domain-1:foundation", "domain-1:practice", "domain-2:foundation"}
    """
    completed = set()
    domains = student_record.get("domains", {})

    for domain_id, levels in domains.items():
        for level_name, level_data in levels.items():
            if isinstance(level_data, dict) and level_data.get("status") == "passed":
                # Normalize level name to new terminology
                normalized_level = level_name.replace("level-1", "foundation") \
                                             .replace("level-2", "practice") \
                                             .replace("level-3", "mastery") \
                                             .replace("level_1", "foundation") \
                                             .replace("level_2", "practice") \
                                             .replace("level_3", "mastery")
                completed.add(f"{domain_id}:{normalized_level}")

    # Check for capstone
    capstone = student_record.get("capstone", {})
    if capstone.get("status") == "passed":
        completed.add("capstone:passed")

    return completed


def get_existing_badges(student_record: dict) -> set:
    """Get set of badge IDs already issued to student."""
    credentials = student_record.get("credentials", {})
    badges = credentials.get("badges", [])
    return {b.get("badge_id") for b in badges if "badge_id" in b}


def issue_badge(
    badge_def: BadgeDefinition,
    student_id: str,
    issuer: str = "system"
) -> IssuedBadge:
    """Issue a badge to a student.

    Returns the issued badge with unique ID and verification URL.
    """
    badge_uuid = generate_badge_uuid()

    return IssuedBadge(
        badge_id=badge_uuid,
        name=badge_def.name,
        type=badge_def.type.value,
        description=badge_def.description,
        emoji=badge_def.emoji,
        issued_at=datetime.utcnow().isoformat() + "Z",
        issuer=issuer,
        student_id=student_id,
        verification_url=generate_verification_url(badge_uuid)
    )


def check_and_issue_badges(
    student_record: dict,
    issuer: str = "system"
) -> List[IssuedBadge]:
    """Check if student qualifies for new badges and issue them.

    Args:
        student_record: Full student record dict
        issuer: Who is issuing (default "system", could be advisor email)

    Returns:
        List of newly issued badges
    """
    student_id = student_record.get("student_id", "unknown")

    # Get what's completed
    completed = get_completed_requirements(student_record)

    # Get what's already issued
    existing = get_existing_badges(student_record)

    # Find all badges we qualify for
    qualified = get_available_badges(completed)

    # Issue new ones
    new_badges = []
    for badge_def in qualified:
        # Check if already issued (match by definition ID, not UUID)
        already_has = any(
            b.get("name") == badge_def.name
            for b in student_record.get("credentials", {}).get("badges", [])
        )
        if not already_has:
            issued = issue_badge(badge_def, student_id, issuer)
            new_badges.append(issued)

    return new_badges


def add_badges_to_record(student_record: dict, badges: List[IssuedBadge]) -> dict:
    """Add issued badges to student record.

    Modifies and returns the record.
    """
    if "credentials" not in student_record:
        student_record["credentials"] = {
            "badges": [],
            "paths_completed": [],
            "capstone_achieved": False
        }

    for badge in badges:
        student_record["credentials"]["badges"].append(badge.to_dict())

        # Update paths_completed if this is a path badge
        if badge.type == "path" and badge.name not in student_record["credentials"]["paths_completed"]:
            student_record["credentials"]["paths_completed"].append(badge.name)

        # Update capstone status
        if badge.type == "capstone":
            student_record["credentials"]["capstone_achieved"] = True

    return student_record


def format_badges_for_display(badges: List[dict]) -> str:
    """Format badges for CLI display."""
    if not badges:
        return "No badges earned yet."

    lines = []
    for badge in badges:
        emoji = badge.get("emoji", "🎖️")
        name = badge.get("name", "Unknown")
        issued = badge.get("issued_at", "")[:10]  # Just the date
        lines.append(f"{emoji} {name} ({issued})")

    return "\n".join(lines)


def format_badge_progress(student_record: dict) -> str:
    """Format badge progress including what's next."""
    from .badges import get_next_badges

    completed = get_completed_requirements(student_record)
    next_badges = get_next_badges(completed)

    if not next_badges:
        return "All available badges earned! 🎉"

    lines = ["BADGES IN PROGRESS", "═" * 40]
    for badge, remaining in next_badges:
        pct = ((len(badge.requirements) - len(remaining)) / len(badge.requirements)) * 100
        bar_filled = int(pct / 5)
        bar = "█" * bar_filled + "░" * (20 - bar_filled)
        lines.append(f"{badge.emoji} {badge.name}: {bar} {len(badge.requirements) - len(remaining)}/{len(badge.requirements)}")
        lines.append(f"   Remaining: {', '.join(remaining)}")

    return "\n".join(lines)
