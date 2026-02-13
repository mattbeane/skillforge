# Assessment Materials

This directory contains materials used in Level 2 and Level 3 assessments for ResearchKit Quals. These are **assessment materials** (stimulus documents students work with during exams), not study guides or instructional content.

---

## Contents

### Domain 5: Epistemological Genre

| File | Purpose | Type | Status |
|------|---------|------|--------|
| `d5-genre-violations-draft.md` | Synthetic paper draft with ~12 seeded genre violations (structural, language, temporal logic). Students must identify violations and propose corrections. | Synthetic | Complete |
| `d5-genre-violations-key.md` | Answer key: each violation's location, type, exact text, explanation, and genre-appropriate revision. Scoring guidance for L2/L3. | Synthetic | Complete |

**Assessment use**: L2 (with feedback) and L3 (without feedback). Student receives the draft and must identify genre violations, classify them, and propose revisions.

### Domain 7: Claim Verification & Integrity

| File | Purpose | Type | Status |
|------|---------|------|--------|
| `d7-overclaim-paper.md` | Synthetic paper draft with 10 seeded overclaims (3 causal, 3 scope, 2 mechanism, 2 evidence-strength) plus 4 properly calibrated claims. Students must identify overclaims, explain why they're overclaims, and propose calibrated revisions. | Synthetic | Complete |
| `d7-overclaim-paper-key.md` | Answer key: each overclaim's location, type, exact text, explanation, and suggested revision. Also documents properly calibrated claims (potential false positives). Scoring guidance for L2/L3. | Synthetic | Complete |

**Assessment use**: L2 (with feedback) and L3 (without feedback). Student receives the draft and must identify overclaims, classify them by type, and produce calibrated revisions.

### Domain 3: Qualitative Mechanism Extraction

Assessment materials for D3 use real (anonymized) data rather than synthetic drafts.

| Resource | Location | Status |
|----------|----------|--------|
| 69 anonymized interview quotations | `../../seed-data/beane-surgery-anonymized/anonymized_quotations.json` | Complete |
| Expert baseline (3 mechanisms, disconfirming evidence, code families) | `../../seed-data/beane-surgery-anonymized/expert_baseline.md` | Complete |
| Anonymization audit report | `../../seed-data/beane-surgery-anonymized/audit_report.md` | Complete |

**Assessment use**: L2 and L3. Student receives anonymized quotations and must extract mechanisms, identify disconfirming evidence, and select key quotes. Scored against expert baseline.

---

## Materials Not Yet Created

| Domain | What's Needed | Blocker | Notes |
|--------|--------------|---------|-------|
| D1 (Pattern Recognition) | Quantitative dataset + expert pattern list | "Company X" anonymized dataset (Matt-dependent) | |
| D2 (Theoretical Positioning) | Finding + expert theoretical positioning | Needs finding from D1 output | |
| D4 (Theoretical Framing) | Evidence package + expert framings | Can derive from D3 output | |
| D6 (Adversarial Evidence) | Paper + full dataset + expert adversarial audit | Beane data exists; needs test paper | |
| Foundation (Argument Construction) | Novel materials for L2/L3 | Can create synthetic (no data dependency) | |

See `../ASSESSMENT_SPECS.md` for full materials status and scoring rubrics.

---

## Design Principles

All synthetic assessment materials follow these principles:

1. **Competent substance, problematic framing.** The papers contain interesting observations, realistic quotes, and reasonable theoretical engagement. The problems are in how claims are calibrated to evidence (D7) or how research is framed in the wrong epistemological genre (D5). Students must distinguish framing problems from content problems.

2. **Mixed difficulty.** Each paper seeds violations at easy, medium, and hard difficulty levels. Easy violations test surface recognition (Level 1 knowledge applied). Medium violations test systematic application. Hard violations test expert judgment.

3. **False positive traps.** Each paper includes properly executed elements that a superficial reader might flag incorrectly. Precision (avoiding false positives) is scored alongside recall (finding real problems).

4. **Answer keys include scoring guidance.** Each key maps to the scoring rubrics in `ASSESSMENT_SPECS.md` and includes worked examples of how to calculate scores.

---

## Synthetic vs. Real Data

- **Synthetic materials** (D5, D7): AI-generated paper drafts with seeded problems. No real participants, no IRB implications. Can be shared freely for teaching purposes.
- **Real data** (D3): Anonymized research data from Beane surgery fieldwork. Three-stage anonymization process documented in audit report. Contains no identifying information but should still be treated as research data with appropriate care.
