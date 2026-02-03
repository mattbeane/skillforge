#!/usr/bin/env python3
"""
Anonymization Engine - Stage 2: Guided Human Review

Interactive CLI for reviewing detected entities and assigning replacements.

Features:
- Review entities by type (PERSON, ORG, GPE, etc.)
- Assign replacement names (e.g., "Dr. Alpha", "Hospital A")
- Mark false positives
- Flag risky combinations for special attention
- Save progress and resume later

Usage:
    python anonymize_stage2.py <entities_json> [--output <reviewed_json>]

Input: JSON from anonymize_stage1.py
Output: JSON with review decisions and replacement mappings
"""

import json
import sys
import os
from pathlib import Path
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional
from collections import defaultdict


# Replacement name generators
REPLACEMENT_TEMPLATES = {
    'PERSON': {
        'pattern': '{role} {letter}',
        'roles': ['Dr.', 'Nurse', 'Resident', 'Surgeon', 'Tech', 'Person'],
        'letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    },
    'ORG': {
        'pattern': '{type} {letter}',
        'types': ['Hospital', 'Center', 'Clinic', 'Institution', 'Org'],
        'letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    },
    'GPE': {
        'pattern': 'Site {letter}',
        'letters': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    },
    'FAC': {
        'pattern': '{type} {number}',
        'types': ['Room', 'OR', 'Floor', 'Unit'],
        'numbers': range(1, 100)
    },
}


@dataclass
class ReviewDecision:
    """A reviewed entity with replacement decision."""
    original: str
    entity_type: str
    decision: str  # 'replace', 'keep', 'false_positive'
    replacement: Optional[str] = None
    notes: str = ""
    confidence: str = "HIGH"  # Review confidence


class ReviewSession:
    """Interactive review session for entities."""

    def __init__(self, entities_path: Path):
        self.entities_path = entities_path
        self.output_path = entities_path.with_suffix('.reviewed.json')

        with open(entities_path) as f:
            self.data = json.load(f)

        self.entity_summary = self.data.get('entity_summary', [])
        self.decisions: Dict[str, ReviewDecision] = {}

        # Track used replacement names
        self.used_replacements: Dict[str, List[str]] = defaultdict(list)

        # Load any existing review progress
        if self.output_path.exists():
            self._load_progress()

    def _load_progress(self):
        """Load existing review progress."""
        try:
            with open(self.output_path) as f:
                saved = json.load(f)

            for entity in saved.get('reviewed_entities', []):
                original = entity['original']
                self.decisions[original.lower()] = ReviewDecision(
                    original=original,
                    entity_type=entity['entity_type'],
                    decision=entity['decision'],
                    replacement=entity.get('replacement'),
                    notes=entity.get('notes', ''),
                    confidence=entity.get('confidence', 'HIGH')
                )

                if entity.get('replacement'):
                    self.used_replacements[entity['entity_type']].append(
                        entity['replacement']
                    )

            print(f"Loaded {len(self.decisions)} previous review decisions.")
        except Exception as e:
            print(f"Could not load previous progress: {e}")

    def save_progress(self):
        """Save current review progress."""
        reviewed = [
            {
                **asdict(dec),
                'count': next(
                    (e['count'] for e in self.entity_summary
                     if e['normalized'] == dec.original.lower()),
                    0
                )
            }
            for dec in self.decisions.values()
        ]

        output = {
            'source_file': str(self.entities_path),
            'review_complete': self.is_complete(),
            'stats': {
                'total_entities': len(self.entity_summary),
                'reviewed': len(self.decisions),
                'replaced': len([d for d in self.decisions.values() if d.decision == 'replace']),
                'kept': len([d for d in self.decisions.values() if d.decision == 'keep']),
                'false_positives': len([d for d in self.decisions.values() if d.decision == 'false_positive']),
            },
            'reviewed_entities': reviewed,
            'replacement_mapping': {
                dec.original: dec.replacement
                for dec in self.decisions.values()
                if dec.decision == 'replace' and dec.replacement
            },
        }

        with open(self.output_path, 'w') as f:
            json.dump(output, f, indent=2)

        print(f"Progress saved to {self.output_path}")

    def is_complete(self) -> bool:
        """Check if all entities have been reviewed."""
        for entity in self.entity_summary:
            if entity['normalized'] not in self.decisions:
                return False
        return True

    def suggest_replacement(self, entity_type: str, original: str) -> str:
        """Suggest a replacement name for an entity."""
        template = REPLACEMENT_TEMPLATES.get(entity_type, {})
        used = self.used_replacements.get(entity_type, [])

        if entity_type == 'PERSON':
            # Try to infer role from original
            original_lower = original.lower()
            if 'dr' in original_lower or 'doctor' in original_lower:
                role = 'Dr.'
            elif 'nurse' in original_lower:
                role = 'Nurse'
            elif 'resident' in original_lower:
                role = 'Resident'
            else:
                role = 'Person'

            for letter in template.get('letters', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                suggestion = f"{role} {letter}"
                if suggestion not in used:
                    return suggestion

        elif entity_type == 'ORG':
            for letter in template.get('letters', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                suggestion = f"Hospital {letter}"
                if suggestion not in used:
                    return suggestion

        elif entity_type == 'GPE':
            for letter in template.get('letters', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
                suggestion = f"Site {letter}"
                if suggestion not in used:
                    return suggestion

        elif entity_type == 'FAC':
            # Try to preserve type (OR, Room, etc.)
            import re
            match = re.match(r'(OR|Room|Floor|Unit)\s*', original, re.I)
            fac_type = match.group(1).upper() if match else 'Room'
            for num in range(1, 100):
                suggestion = f"{fac_type} {num}"
                if suggestion not in used:
                    return suggestion

        return f"[{entity_type} X]"

    def review_entity(self, entity: dict) -> Optional[ReviewDecision]:
        """Interactively review a single entity."""
        print("\n" + "=" * 60)
        print(f"Entity: \"{entity['text']}\"")
        print(f"Type: {entity['type']}")
        print(f"Occurrences: {entity['count']}")
        print("\nSample contexts:")
        for ctx in entity.get('sample_contexts', [])[:3]:
            print(f"  ...{ctx}...")

        suggestion = self.suggest_replacement(entity['type'], entity['text'])

        print("\nOptions:")
        print(f"  [r] Replace with: {suggestion}")
        print(f"  [c] Custom replacement")
        print(f"  [k] Keep as-is (not identifying)")
        print(f"  [f] False positive (NER error)")
        print(f"  [s] Skip for now")
        print(f"  [q] Quit and save")

        while True:
            choice = input("\nChoice: ").strip().lower()

            if choice == 'r':
                self.used_replacements[entity['type']].append(suggestion)
                return ReviewDecision(
                    original=entity['text'],
                    entity_type=entity['type'],
                    decision='replace',
                    replacement=suggestion
                )

            elif choice == 'c':
                custom = input("Enter custom replacement: ").strip()
                if custom:
                    self.used_replacements[entity['type']].append(custom)
                    return ReviewDecision(
                        original=entity['text'],
                        entity_type=entity['type'],
                        decision='replace',
                        replacement=custom
                    )

            elif choice == 'k':
                notes = input("Notes (optional): ").strip()
                return ReviewDecision(
                    original=entity['text'],
                    entity_type=entity['type'],
                    decision='keep',
                    notes=notes
                )

            elif choice == 'f':
                return ReviewDecision(
                    original=entity['text'],
                    entity_type=entity['type'],
                    decision='false_positive'
                )

            elif choice == 's':
                return None

            elif choice == 'q':
                raise KeyboardInterrupt

            else:
                print("Invalid choice. Please try again.")

    def run_review(self, entity_types: Optional[List[str]] = None):
        """Run interactive review session."""
        # Filter entities to review
        to_review = []
        for entity in self.entity_summary:
            if entity['normalized'] in self.decisions:
                continue  # Already reviewed
            if entity_types and entity['type'] not in entity_types:
                continue  # Filter by type
            to_review.append(entity)

        if not to_review:
            print("All entities have been reviewed!")
            return

        print(f"\n{len(to_review)} entities to review")
        if entity_types:
            print(f"Filtering to types: {', '.join(entity_types)}")

        # Sort by count (review most frequent first)
        to_review.sort(key=lambda e: -e['count'])

        try:
            for i, entity in enumerate(to_review):
                print(f"\n[{i + 1}/{len(to_review)}]")
                decision = self.review_entity(entity)

                if decision:
                    self.decisions[entity['normalized']] = decision
                    self.save_progress()

        except KeyboardInterrupt:
            print("\n\nSaving progress...")
            self.save_progress()
            print("Review session ended. Resume later to continue.")

    def show_summary(self):
        """Show current review status."""
        total = len(self.entity_summary)
        reviewed = len(self.decisions)
        pending = total - reviewed

        print("\n" + "=" * 60)
        print("REVIEW STATUS")
        print("=" * 60)
        print(f"Total entities: {total}")
        print(f"Reviewed: {reviewed}")
        print(f"Pending: {pending}")

        if self.decisions:
            replaced = len([d for d in self.decisions.values() if d.decision == 'replace'])
            kept = len([d for d in self.decisions.values() if d.decision == 'keep'])
            false_pos = len([d for d in self.decisions.values() if d.decision == 'false_positive'])
            print(f"\nDecisions:")
            print(f"  - Replace: {replaced}")
            print(f"  - Keep: {kept}")
            print(f"  - False positive: {false_pos}")

        if pending > 0:
            print(f"\nEntity types remaining:")
            remaining_types = defaultdict(int)
            for entity in self.entity_summary:
                if entity['normalized'] not in self.decisions:
                    remaining_types[entity['type']] += 1
            for etype, count in sorted(remaining_types.items(), key=lambda x: -x[1]):
                print(f"  - {etype}: {count}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Stage 2: Guided human review of detected entities')
    parser.add_argument('entities_json', type=Path, help='JSON from Stage 1')
    parser.add_argument('--output', '-o', type=Path, help='Output path (default: input.reviewed.json)')
    parser.add_argument('--types', '-t', nargs='+', help='Filter to specific entity types')
    parser.add_argument('--status', '-s', action='store_true', help='Show status only')

    args = parser.parse_args()

    if not args.entities_json.exists():
        print(f"Error: {args.entities_json} not found")
        sys.exit(1)

    session = ReviewSession(args.entities_json)

    if args.output:
        session.output_path = args.output

    if args.status:
        session.show_summary()
        return

    session.show_summary()

    if session.is_complete():
        print("\nAll entities have been reviewed!")
        response = input("Would you like to re-review any? (y/n): ")
        if response.lower() != 'y':
            return
        # Reset decisions for re-review
        session.decisions = {}

    session.run_review(entity_types=args.types)
    session.show_summary()


if __name__ == '__main__':
    main()
