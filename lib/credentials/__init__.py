"""
Skill-Forge Credentials Module

Handles badge definitions, issuance, and verification.
"""

from .badges import DOMAIN_BADGES, PATH_BADGES, CAPSTONE_BADGE, get_badge_by_id
from .issuer import check_and_issue_badges, issue_badge
from .paths import PATHS, check_path_completion

__all__ = [
    'DOMAIN_BADGES',
    'PATH_BADGES',
    'CAPSTONE_BADGE',
    'PATHS',
    'get_badge_by_id',
    'check_and_issue_badges',
    'issue_badge',
    'check_path_completion',
]
