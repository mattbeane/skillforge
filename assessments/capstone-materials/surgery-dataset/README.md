# Capstone Materials: Surgery Dataset

## Contents

- `AI_GENERATED_DRAFT.md` - The deliberately flawed paper students must evaluate
- `ISSUE_KEY.md` - **EVALUATOR ONLY** - Complete issue list with scoring guide
- Raw data available in `/seed-data/beane-surgery-anonymized/`

## How This Was Generated

The AI draft was produced by running the surgery dataset through an uncalibrated pipeline that:
- Did NOT have human confirmation at gates
- Did NOT check for genre appropriateness
- Did NOT hunt for disconfirming evidence
- Applied default LLM tendencies (hypo-deductive framing, overclaiming, surface-level mechanism identification)

This simulates what a naive user might accept as a "good" AI-generated draft.

## Seeded Error Types

| Domain | Error Type | Severity |
|--------|-----------|----------|
| 5 | Hypo-deductive framing throughout | Critical |
| 2 | Overclaimed contribution | Critical |
| 3 | Key mechanism undersold (shadow learning → "informal strategies") | Critical |
| 6 | Disconfirming evidence absent | Critical |
| 7 | Quantitative claims without support | Critical |
| 4 | Generic literature positioning | Major |
| 3 | Portfolio degradation undertheorized | Major |
| 7 | Sample description mismatch | Major |
| 5 | Missing discovery narrative | Major |
| 3 | Unintegrated findings | Major |

## Expert Baseline

The expert baseline (`/seed-data/beane-surgery-anonymized/expert_baseline.md`) documents:
- What mechanisms actually exist in this data
- How they were discovered
- What disconfirming evidence exists
- What good coding looks like

Students should NOT see the expert baseline before the assessment. It's used for:
1. Generating the issue key
2. Post-assessment feedback comparison

## Usage

1. Student receives: `AI_GENERATED_DRAFT.md` + access to raw data
2. Student submits: Issue log, prioritization, meta-reflection
3. Evaluator uses: `ISSUE_KEY.md` to score
4. Feedback includes: Comparison to expert baseline

## Rotating This Dataset

To prevent answer sharing:
- This dataset should be used for one cohort
- New cohorts should use different faculty-contributed datasets
- The issue key structure is reusable; specific issues will differ by dataset
