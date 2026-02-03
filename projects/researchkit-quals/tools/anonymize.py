#!/usr/bin/env python3
"""
ResearchKit Quals - Anonymization Engine

A three-stage system for anonymizing qualitative research data:

Stage 1: Automatic Detection
    - NER (Named Entity Recognition) for people, orgs, locations
    - Regex patterns for PII (emails, phones, dates)
    - Custom dictionary for study-specific terms
    - Risk flagging for identifying combinations

Stage 2: Guided Human Review
    - Interactive CLI for reviewing detected entities
    - Assign replacement names (Dr. A, Hospital B, Site C)
    - Mark false positives
    - Save progress and resume later

Stage 3: Verification & Application
    - Apply replacements to source documents
    - Generate audit report
    - Run re-identification check
    - Create contributor sign-off template

Usage:
    python anonymize.py detect <atlas_export.json>
    python anonymize.py review <entities.json>
    python anonymize.py apply <reviewed.json> <source.json> --output-dir <dir>
    python anonymize.py full <atlas_export.json>  # All stages

Prerequisites:
    pip install spacy
    python -m spacy download en_core_web_sm
"""

import sys
import argparse
from pathlib import Path


def run_detection(args):
    """Run Stage 1: Automatic NER detection."""
    from anonymize_stage1 import analyze_atlas_export

    input_path = args.input
    output_path = args.output or input_path.with_suffix('.entities.json')

    print(f"Stage 1: Detecting entities in {input_path}...")
    results = analyze_atlas_export(input_path, custom_dict=None)

    import json
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\nDetection complete:")
    print(f"  - {results['stats']['total_quotations']} quotations analyzed")
    print(f"  - {results['stats']['unique_entities']} unique entities found")
    print(f"\nOutput: {output_path}")
    print(f"\nNext: python anonymize.py review {output_path}")


def run_review(args):
    """Run Stage 2: Guided human review."""
    from anonymize_stage2 import ReviewSession

    session = ReviewSession(args.input)
    session.show_summary()

    if args.status:
        return

    if session.is_complete() and not args.force:
        print("\nAll entities have been reviewed!")
        response = input("Re-review? (y/n): ")
        if response.lower() != 'y':
            return

    session.run_review(entity_types=args.types)
    session.show_summary()

    print(f"\nNext: python anonymize.py apply {session.output_path} {args.input.with_suffix('.json')}")


def run_apply(args):
    """Run Stage 3: Verification and application."""
    from anonymize_stage3 import AnonymizationApplier, run_verification_check
    import json

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Stage 3: Applying anonymization...")
    applier = AnonymizationApplier(args.reviewed, args.source)

    # Apply anonymization
    anonymized = applier.anonymize_quotations()
    anon_path = output_dir / 'anonymized_quotations.json'
    with open(anon_path, 'w') as f:
        json.dump(anonymized, f, indent=2)
    print(f"✓ Anonymized quotations: {anon_path}")

    # Generate audit report
    audit = applier.generate_audit_report()
    audit_path = output_dir / 'audit_report.md'
    with open(audit_path, 'w') as f:
        f.write(audit)
    print(f"✓ Audit report: {audit_path}")

    # Generate signoff template
    signoff = applier.generate_signoff_template()
    signoff_path = output_dir / 'contributor_signoff.md'
    with open(signoff_path, 'w') as f:
        f.write(signoff)
    print(f"✓ Sign-off template: {signoff_path}")

    print(f"\nAnonymization complete:")
    print(f"  - {len(applier.records)} replacements made")

    if args.verify:
        print("\nRunning verification check...")
        verification = run_verification_check(anonymized)
        if verification['status'] == 'PASS':
            print("✓ Verification PASSED")
        else:
            for flag in verification['flags']:
                print(f"  {flag}")


def run_full(args):
    """Run all three stages in sequence."""
    input_path = args.input
    output_dir = args.output_dir or input_path.parent / 'anonymized'
    output_dir.mkdir(parents=True, exist_ok=True)

    # Stage 1
    print("=" * 60)
    print("STAGE 1: AUTOMATIC DETECTION")
    print("=" * 60)

    from anonymize_stage1 import analyze_atlas_export
    import json

    entities_path = output_dir / 'entities.json'
    results = analyze_atlas_export(input_path)
    with open(entities_path, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"Detected {results['stats']['unique_entities']} unique entities")

    # Stage 2
    print("\n" + "=" * 60)
    print("STAGE 2: GUIDED HUMAN REVIEW")
    print("=" * 60)

    from anonymize_stage2 import ReviewSession
    session = ReviewSession(entities_path)
    session.show_summary()

    if not session.is_complete():
        print("\nStarting interactive review...")
        session.run_review()

    # Stage 3
    print("\n" + "=" * 60)
    print("STAGE 3: VERIFICATION & APPLICATION")
    print("=" * 60)

    reviewed_path = session.output_path

    from anonymize_stage3 import AnonymizationApplier, run_verification_check

    applier = AnonymizationApplier(reviewed_path, input_path)
    anonymized = applier.anonymize_quotations()

    anon_path = output_dir / 'anonymized_quotations.json'
    with open(anon_path, 'w') as f:
        json.dump(anonymized, f, indent=2)

    audit_path = output_dir / 'audit_report.md'
    with open(audit_path, 'w') as f:
        f.write(applier.generate_audit_report())

    signoff_path = output_dir / 'contributor_signoff.md'
    with open(signoff_path, 'w') as f:
        f.write(applier.generate_signoff_template())

    verification = run_verification_check(anonymized)

    print("\n" + "=" * 60)
    print("ANONYMIZATION COMPLETE")
    print("=" * 60)
    print(f"\nOutputs in {output_dir}:")
    print(f"  - anonymized_quotations.json")
    print(f"  - audit_report.md")
    print(f"  - contributor_signoff.md")
    print(f"\nVerification: {verification['status']}")
    print(f"\n{verification['recommendation']}")


def main():
    parser = argparse.ArgumentParser(
        description='ResearchKit Quals Anonymization Engine',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    subparsers = parser.add_subparsers(dest='command', required=True)

    # Detect command
    detect_parser = subparsers.add_parser('detect', help='Stage 1: Automatic NER detection')
    detect_parser.add_argument('input', type=Path, help='Atlas.ti export JSON')
    detect_parser.add_argument('--output', '-o', type=Path, help='Output path')

    # Review command
    review_parser = subparsers.add_parser('review', help='Stage 2: Guided human review')
    review_parser.add_argument('input', type=Path, help='Entities JSON from Stage 1')
    review_parser.add_argument('--types', '-t', nargs='+', help='Filter by entity type')
    review_parser.add_argument('--status', '-s', action='store_true', help='Show status only')
    review_parser.add_argument('--force', '-f', action='store_true', help='Force re-review')

    # Apply command
    apply_parser = subparsers.add_parser('apply', help='Stage 3: Apply anonymization')
    apply_parser.add_argument('reviewed', type=Path, help='Reviewed JSON from Stage 2')
    apply_parser.add_argument('source', type=Path, help='Original Atlas.ti export')
    apply_parser.add_argument('--output-dir', '-o', type=Path, default=Path('.'), help='Output directory')
    apply_parser.add_argument('--verify', '-v', action='store_true', help='Run verification')

    # Full pipeline command
    full_parser = subparsers.add_parser('full', help='Run all stages')
    full_parser.add_argument('input', type=Path, help='Atlas.ti export JSON')
    full_parser.add_argument('--output-dir', '-o', type=Path, help='Output directory')

    args = parser.parse_args()

    if args.command == 'detect':
        run_detection(args)
    elif args.command == 'review':
        run_review(args)
    elif args.command == 'apply':
        run_apply(args)
    elif args.command == 'full':
        run_full(args)


if __name__ == '__main__':
    main()
