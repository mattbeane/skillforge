# Assessment Specifications

## The Problem With My Original Design

I wrote 400-line competency documents but never specified:
- How to actually score assessments
- What datasets to use
- What "overlap with expert" means operationally

This document fixes that.

---

## Scoring Rubrics

### Level 1: Knowledge Recognition (All Domains)

**Format**: 10-15 multiple choice + 2-3 short answer
**Time**: 30-45 minutes
**Passing**: ≥80% (no partial credit on MC)
**Retake**: Immediately, unlimited attempts

**Scoring is binary**: Right or wrong answers with answer key.

---

### Level 2: Application with Feedback (All Domains)

**Format**: Apply concepts to provided materials
**Time**: 2-4 hours
**Passing**: ≥70/100 on rubric
**Retake**: After reviewing feedback, 7-day cooldown

**Scoring rubric template**:

| Criterion | Points | How to Score |
|-----------|--------|--------------|
| Found target patterns/evidence | 30 | Count: (found ∩ expected) / expected |
| Avoided false positives | 20 | Count: (found - expected) / found → penalize |
| Reasoning quality | 30 | Holistic: 0-10 scale × 3 |
| Completeness | 20 | Did they do all parts? Binary per part |

---

### Level 3: Authentic Performance (All Domains)

**Format**: Independent work on novel materials
**Time**: 4-8 hours (varies by domain)
**Passing**: ≥70/100 AND no criterion below 50%
**Retake**: 30-day cooldown (one attempt per month)

**Scoring**: Same rubric as Level 2, but:
- No feedback during assessment
- Stricter floor requirements
- Single attempt enforced

---

## Domain-Specific Scoring

### Domain 1: Pattern Recognition

**Expert baseline**: Matt identifies top 5 patterns in dataset, rates each 1-5 on interest.

**Scoring**:
- Student identifies same patterns: +6 points each (max 30)
- Student identifies pattern Matt rated 1-2: +2 points each
- Student pursues pattern Matt would kill: -5 points each
- Robustness instinct demonstrated: +20 (holistic)
- Heterogeneity explored: +10
- Killed findings documented: +10

### Domain 3: Qualitative Mechanism Extraction

**CRITICAL: This is the hardest to score objectively**

**Expert baseline**: Matt codes 10 interviews, identifies:
- Top 3 mechanisms with quote IDs
- Disconfirming evidence (quote IDs)
- Unexpected themes

**Scoring**:

```
Mechanism overlap = |student_mechanisms ∩ expert_mechanisms| / |expert_mechanisms|
Quote overlap = |student_quotes ∩ expert_quotes| / |expert_quotes|
Disconfirm found = |student_disconfirm ∩ expert_disconfirm| / |expert_disconfirm|

Score = (mechanism_overlap × 30) + (quote_overlap × 25) + (disconfirm_found × 30) + (holistic × 15)
```

**Minimum bar**: Must find ≥50% of disconfirming evidence. Zero tolerance for cherry-picking.

### Domain 4: Theoretical Framing

**Scoring uses Zuckerman rubric-eval**:

```bash
rubric-eval eval student_framing.md rubrics/zuckerman.json \
  --runs 5 --model haiku
```

Each of 10 criteria scored 1-5. Pass requires:
- Total ≥35/50
- No criterion below 2/5
- Generated ≥3 distinct framings

### Domain 7: Claim Verification

**Expert baseline**: Matt identifies all overclaims in test paper.

**Scoring**:
```
Overclaims found = |student ∩ expert| / |expert|
False positives = |student - expert| / |student|
Calibration quality = holistic assessment of revisions

Score = (found × 40) - (false_pos × 20) + (calibration × 40)
```

---

## Assessment Materials Needed

### Priority 1: Create These First

| Domain | Materials | Source | Prep Time |
|--------|-----------|--------|-----------|
| D1 | Quantitative dataset + expert pattern list | Company X (anonymized) | 4-6 hours |
| D3 | 10 interview transcripts + expert coding | Company Y (anonymized) | 8-12 hours |
| D7 | Paper draft with seeded overclaims | Create synthetic | 2-3 hours |

### Priority 2: Create After Pilot

| Domain | Materials | Source | Prep Time |
|--------|-----------|--------|-----------|
| D2 | Finding + expert theoretical positioning | From D1 output | 2-3 hours |
| D4 | Evidence package + expert framings | From D3 output | 4-6 hours |
| D5 | Draft with genre violations + expert revision | Create synthetic | 3-4 hours |
| D6 | Paper + data + expert audit | From prior | 4-6 hours |

---

## Advisor Certification Protocol

When an advisor certifies competence without full assessment:

**Required**:
1. Advisor reviews student's prior work demonstrating competence
2. Advisor signs certification form with:
   - Domain and level being certified
   - Evidence reviewed (paper title, course, etc.)
   - Attestation: "I have reviewed [evidence] and certify that [student] demonstrates competence in [domain] at Level [N]"
3. Certification logged to student record with advisor ID and date

**Audit trail**:
```json
{
  "type": "advisor_certification",
  "domain": "domain-3",
  "level": 3,
  "advisor": "Prof. Beane",
  "advisor_id": "mbeane",
  "date": "2025-02-02",
  "evidence": "Prior qual methods course at Stanford (TM 502), A grade",
  "attestation_signed": true
}
```

**Limits**:
- Advisor can certify max 3 domains per student (prevents blanket exemption)
- Domains 6-7 cannot be certified (must demonstrate adversarial + verification skills)

---

## Note

> **Assessment approach is draft.** Whether rubric-based scoring is appropriate for all domains is an open question. Some competencies (like research integrity under pressure, or "taste" in framing) may resist formal assessment. Faculty and student input on the assessment approach is actively sought.

> Tool integration planning (e.g., how competency status might gate access to AI-assisted research tools) has been moved to `THEORYFORGE_INTEGRATION.md`.

---

## What's Still Needed

1. **Actually create the assessment datasets** - This is real work
2. **Build the quals CLI** - Commands to take/submit assessments
3. **Create the Level 1 question banks** - Multiple choice from competency docs
4. **Set up rubric-eval for D4** - Zuckerman criteria as rubric

The competency definitions are design docs. The system isn't operational until the above exist.
