#!/usr/bin/env python3
"""
Anonymization Engine - Stage 3: Verification & Application

Applies replacement decisions to source documents and generates:
1. Anonymized documents
2. Audit report documenting all changes
3. Verification check (optional re-ID attempt)

Usage:
    python anonymize_stage3.py <reviewed_json> <source_json> [--output-dir <dir>]

Input:
    - reviewed_json: Output from Stage 2 with replacement mappings
    - source_json: Original Atlas.ti export with full content

Output:
    - anonymized_*.json: Anonymized quotations
    - audit_report.md: Documentation of all changes
    - contributor_signoff.md: Template for contributor approval
"""

import json
import re
import sys
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import Dict, List, Set, Tuple
from datetime import datetime
from collections import defaultdict


@dataclass
class ReplacementRecord:
    """Record of a single replacement made."""
    original: str
    replacement: str
    entity_type: str
    document_name: str
    location: str  # Brief context
    timestamp: str


class AnonymizationApplier:
    """Applies anonymization decisions to source documents."""

    def __init__(self, reviewed_path: Path, source_path: Path):
        with open(reviewed_path) as f:
            self.review_data = json.load(f)

        with open(source_path) as f:
            self.source_data = json.load(f)

        self.replacement_map = self.review_data.get('replacement_mapping', {})
        self.records: List[ReplacementRecord] = []

        # Build case-insensitive replacement patterns
        self.patterns = {}
        for original, replacement in self.replacement_map.items():
            # Create pattern that matches the original (case-insensitive, word boundary)
            pattern = re.compile(
                r'\b' + re.escape(original) + r'\b',
                re.IGNORECASE
            )
            self.patterns[pattern] = (original, replacement)

    def anonymize_text(self, text: str, document_name: str) -> Tuple[str, List[ReplacementRecord]]:
        """
        Apply all replacements to a text string.

        Returns:
            (anonymized_text, list of replacement records)
        """
        records = []
        result = text

        for pattern, (original, replacement) in self.patterns.items():
            matches = list(pattern.finditer(result))
            if matches:
                # Record each match before replacing
                for match in matches:
                    start = max(0, match.start() - 20)
                    end = min(len(result), match.end() + 20)
                    context = result[start:end]

                    records.append(ReplacementRecord(
                        original=match.group(),
                        replacement=replacement,
                        entity_type=self._get_entity_type(original),
                        document_name=document_name,
                        location=f"...{context}...",
                        timestamp=datetime.now().isoformat()
                    ))

                # Perform replacement
                result = pattern.sub(replacement, result)

        return result, records

    def _get_entity_type(self, original: str) -> str:
        """Look up entity type for an original term."""
        for entity in self.review_data.get('reviewed_entities', []):
            if entity.get('original', '').lower() == original.lower():
                return entity.get('entity_type', 'UNKNOWN')
        return 'UNKNOWN'

    def anonymize_quotations(self) -> dict:
        """Anonymize all quotations and return new data structure."""
        anonymized_quots = []

        for quot in self.source_data.get('quotations', []):
            anon_text, records = self.anonymize_text(
                quot['text'],
                quot.get('document_name', 'unknown')
            )
            self.records.extend(records)

            anonymized_quots.append({
                **quot,
                'text': anon_text,
                'anonymized': True
            })

        return {
            'codes': self.source_data.get('codes', {}),
            'code_groups': self.source_data.get('code_groups', []),
            'documents': self.source_data.get('documents', {}),
            'quotations': anonymized_quots,
            'stats': {
                **self.source_data.get('stats', {}),
                'anonymization_applied': True,
                'replacements_made': len(self.records),
            }
        }

    def generate_audit_report(self) -> str:
        """Generate markdown audit report."""
        lines = [
            "# Anonymization Audit Report",
            "",
            f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"**Source file**: {self.source_data.get('stats', {}).get('total_quotations', 0)} quotations",
            "",
            "---",
            "",
            "## Summary Statistics",
            "",
            f"- **Total replacements made**: {len(self.records)}",
            f"- **Unique terms replaced**: {len(self.replacement_map)}",
            "",
            "### Replacement Counts by Type",
            "",
        ]

        # Count by type
        type_counts = defaultdict(int)
        for record in self.records:
            type_counts[record.entity_type] += 1

        for etype, count in sorted(type_counts.items(), key=lambda x: -x[1]):
            lines.append(f"- {etype}: {count}")

        lines.extend([
            "",
            "---",
            "",
            "## Replacement Mapping",
            "",
            "| Original | Replacement | Type |",
            "|----------|-------------|------|",
        ])

        for entity in self.review_data.get('reviewed_entities', []):
            if entity.get('decision') == 'replace':
                orig = entity.get('original', '')
                repl = entity.get('replacement', '')
                etype = entity.get('entity_type', '')
                lines.append(f"| {orig} | {repl} | {etype} |")

        lines.extend([
            "",
            "---",
            "",
            "## Detailed Change Log",
            "",
            "### By Document",
            "",
        ])

        # Group records by document
        by_doc = defaultdict(list)
        for record in self.records:
            by_doc[record.document_name].append(record)

        for doc_name, doc_records in sorted(by_doc.items()):
            lines.append(f"#### {doc_name}")
            lines.append("")
            for record in doc_records:
                lines.append(f"- `{record.original}` → `{record.replacement}` ({record.entity_type})")
            lines.append("")

        lines.extend([
            "---",
            "",
            "## Items Kept As-Is",
            "",
            "The following detected entities were reviewed and determined to not require anonymization:",
            "",
        ])

        for entity in self.review_data.get('reviewed_entities', []):
            if entity.get('decision') == 'keep':
                lines.append(f"- **{entity.get('original')}** ({entity.get('entity_type')}): {entity.get('notes', 'No notes')}")

        lines.extend([
            "",
            "---",
            "",
            "## False Positives",
            "",
            "The following NER detections were marked as false positives:",
            "",
        ])

        for entity in self.review_data.get('reviewed_entities', []):
            if entity.get('decision') == 'false_positive':
                lines.append(f"- {entity.get('original')} ({entity.get('entity_type')})")

        return '\n'.join(lines)

    def generate_signoff_template(self) -> str:
        """Generate contributor signoff template."""
        return f"""# Anonymization Contributor Sign-Off

## Study Information

- **Contributing Faculty**: [NAME]
- **Institution**: [INSTITUTION]
- **Study Title**: [TITLE]
- **Date**: {datetime.now().strftime('%Y-%m-%d')}

## Anonymization Summary

I have reviewed the anonymization process for this contribution:

- **Quotations processed**: {self.source_data.get('stats', {}).get('total_quotations', 0)}
- **Unique entities replaced**: {len(self.replacement_map)}
- **Total replacements**: {len(self.records)}

## Review Confirmation

Please check each box to confirm:

- [ ] I have reviewed the replacement mapping in the audit report
- [ ] I have verified that all identifying information has been replaced
- [ ] I understand that some re-identification risk may remain despite best efforts
- [ ] I confirm that this data may be used for educational purposes in ResearchKit Quals

## Acceptable Risk Items

If any items were marked "keep" despite potential identifying information, list and justify:

1. [Item 1]: [Justification]
2. [Item 2]: [Justification]

## Sign-Off

By signing below, I attest that I have reviewed the anonymization and that reasonable
efforts have been made to protect informant identity.

**Signature**: _________________________

**Printed Name**: _________________________

**Date**: _________________________

---

*This document should be kept with the contribution package.*
"""


def run_verification_check(anonymized_data: dict) -> dict:
    """
    Attempt to re-identify entities in anonymized data.

    This is a basic check - looks for patterns that might indicate
    incomplete anonymization.

    Returns:
        dict with verification results and any flags
    """
    flags = []
    text_sample = ' '.join([q['text'] for q in anonymized_data.get('quotations', [])])

    # Check for common PII patterns that shouldn't be there
    import re

    # Email patterns
    if re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text_sample):
        flags.append("⚠️ Email address pattern detected")

    # Phone patterns
    if re.search(r'\b(\+?1[-.]?)?\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}\b', text_sample):
        flags.append("⚠️ Phone number pattern detected")

    # Common name patterns (titles followed by proper nouns)
    title_matches = re.findall(r'\b(Dr\.?|Mr\.?|Mrs\.?|Ms\.?)\s+[A-Z][a-z]+', text_sample)
    if title_matches:
        flags.append(f"⚠️ Possible names with titles: {title_matches[:3]}")

    # Check for year + role combinations
    if re.search(r'\b(19|20)\d{2}\b.*\bresident\b|\bresident\b.*\b(19|20)\d{2}\b', text_sample, re.I):
        flags.append("⚠️ Year + role combination could be identifying")

    return {
        'verification_complete': True,
        'flags': flags,
        'status': 'PASS' if not flags else 'REVIEW_NEEDED',
        'recommendation': (
            "Anonymization appears complete. Ready for contribution."
            if not flags else
            f"Review {len(flags)} potential issues before contributing."
        )
    }


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Stage 3: Apply anonymization and generate audit report')
    parser.add_argument('reviewed_json', type=Path, help='Reviewed entities from Stage 2')
    parser.add_argument('source_json', type=Path, help='Original Atlas.ti export')
    parser.add_argument('--output-dir', '-o', type=Path, default=Path('.'), help='Output directory')
    parser.add_argument('--verify', '-v', action='store_true', help='Run verification check')

    args = parser.parse_args()

    if not args.reviewed_json.exists():
        print(f"Error: {args.reviewed_json} not found")
        sys.exit(1)

    if not args.source_json.exists():
        print(f"Error: {args.source_json} not found")
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Applying anonymization...")
    applier = AnonymizationApplier(args.reviewed_json, args.source_json)

    # Apply anonymization
    anonymized = applier.anonymize_quotations()
    anon_path = args.output_dir / 'anonymized_quotations.json'
    with open(anon_path, 'w') as f:
        json.dump(anonymized, f, indent=2)
    print(f"✓ Anonymized quotations: {anon_path}")

    # Generate audit report
    audit = applier.generate_audit_report()
    audit_path = args.output_dir / 'audit_report.md'
    with open(audit_path, 'w') as f:
        f.write(audit)
    print(f"✓ Audit report: {audit_path}")

    # Generate signoff template
    signoff = applier.generate_signoff_template()
    signoff_path = args.output_dir / 'contributor_signoff.md'
    with open(signoff_path, 'w') as f:
        f.write(signoff)
    print(f"✓ Sign-off template: {signoff_path}")

    print(f"\nAnonymization complete:")
    print(f"  - {len(applier.records)} replacements made")
    print(f"  - {len(applier.replacement_map)} unique terms replaced")

    if args.verify:
        print("\nRunning verification check...")
        verification = run_verification_check(anonymized)

        if verification['status'] == 'PASS':
            print("✓ Verification PASSED")
        else:
            print(f"⚠️ Verification needs review:")
            for flag in verification['flags']:
                print(f"  {flag}")

        print(f"\n{verification['recommendation']}")

    print("\nNext steps:")
    print("  1. Review audit_report.md for accuracy")
    print("  2. Complete contributor_signoff.md")
    print("  3. Package contribution with /rk.contribution-package")


if __name__ == '__main__':
    main()
