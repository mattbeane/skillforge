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

### Domain 2: Theoretical Positioning

**Expert baseline**: Matt produces expert theoretical positioning for a provided finding:
- Violated/extended theory with rationale
- Audience choice (row/column) with justification
- Sensitizing literature selection with bridging argument
- 1-paragraph contribution statement

**Scoring**:

```
Theory match = does student identify same (or comparably valid) theory? (0/15/25)
  25 = Same theory or equally valid alternative with clear rationale
  15 = Related theory, partially correct reasoning
   0 = Missed the violation entirely or cited decorative theory

Audience calibration = correct row/column choice with rationale (0/10/20)
  20 = Correct choice, clear rationale
  10 = Correct choice, weak rationale (or defensible alternative)
   0 = Misidentified audience

Sensitizing literature quality (0/10/20/30)
  30 = Literature explains heterogeneity, bridge clearly articulated
  20 = Good literature choice, bridge partially articulated
  10 = Literature is decorative (related but doesn't explain variance)
   0 = No sensitizing literature or completely irrelevant

Contribution statement (0/10/15/25)
  25 = Specific, names what changes, no empty verbs
  15 = Mostly specific, minor empty verb use
  10 = Vague ("contributes to the literature on...")
   0 = Missing or purely descriptive

Score = theory_match + audience + sensitizing + contribution
```

**Passing**: ≥70/100. Must score ≥15 on theory match (can't pass with wrong theory).

### Domain 5: Epistemological Genre

**Expert baseline**: Expert identifies all genre violations in a provided draft and produces corrected version.

**Scoring**:

```
Violation detection = |student_violations ∩ expert_violations| / |expert_violations|
False positives = |student_violations - expert_violations| / |student_violations|

Score breakdown:
  Detection (30 pts): violation_detection × 30
  Classification (15 pts): correctly categorized each found violation as
    structural / language / temporal logic → 5 pts per correct classification (max 15)
  Revision quality (30 pts): holistic assessment of genre-appropriate rewrites
    30 = Rewrites are fully genre-appropriate, natural-sounding
    20 = Mostly genre-appropriate, minor slips
    10 = Shows understanding but execution is awkward
     0 = Rewrites still contain genre violations
  Precision (10 pts): 10 - (false_positive_rate × 20), floor 0
    (penalizes "fixing" things that weren't broken)
  Explanation quality (15 pts): holistic assessment of why each revision is
    genre-appropriate → 15/10/5/0

Score = detection + classification + revision + precision + explanation
```

**Passing**: ≥70/100. Must score ≥20 on detection (can't pass if you miss most violations).

**Assessment materials needed**: A 5-10 page draft written in the wrong genre (e.g., inductive research framed deductively), with known violations seeded at specific points. Prep time: 3-4 hours to create synthetic draft.

### Domain 6: Adversarial Evidence Handling

**Expert baseline**: Matt audits a test paper against its full dataset, documenting:
- All disconfirming evidence found (with source IDs)
- Evidence distribution by role, site, time period
- Alternative interpretations for each major claim

**Scoring**:

```
Disconfirm found = |student_disconfirm ∩ expert_disconfirm| / |expert_disconfirm|
Distribution accuracy = did student correctly identify concentration patterns? (0/10/20)
Alternatives quality = number and quality of alternative interpretations (0-20)

Score breakdown:
  Disconfirming evidence discovery (30 pts): disconfirm_found × 30
  Distribution analysis (20 pts):
    20 = Correctly identified which roles/sites/periods support vs challenge
    10 = Partial distribution analysis, missed key concentration
     0 = No distribution analysis attempted
  Alternative interpretations (20 pts):
    20 = Named ≥2 plausible alternatives, engaged seriously with strongest
    10 = Named 1 alternative but didn't fully engage
     0 = No alternatives or only straw man alternatives
  Search comprehensiveness (15 pts):
    15 = Searched all data sources, including uncited ones
    10 = Searched most data sources
     5 = Only searched cited sources
     0 = Spot-checked or didn't search systematically
  Recommendation quality (15 pts): holistic assessment of audit summary
    15 = Actionable recommendations, correctly prioritized
    10 = Reasonable recommendations, some prioritization issues
     5 = Vague recommendations
     0 = No recommendations

Score = disconfirm + distribution + alternatives + comprehensiveness + recommendations
```

**Passing**: ≥70/100. Must score ≥20 on disconfirming evidence discovery. Zero tolerance: if student finds 0 disconfirming evidence in a dataset where expert found ≥3, automatic fail regardless of other scores.

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
| D5 | Synthetic draft with seeded genre violations + expert revision | Create synthetic | 3-4 hours |
| D6 | Paper draft with claims + full dataset + expert adversarial audit | From prior work | 4-6 hours |

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

## Foundation: Argument Construction Scoring (Draft)

Argument Construction is assessed using the same three-level structure as domains, but with mechanical (not holistic) criteria. The key difference: these assessments evaluate *structure* — paragraph architecture, transitions, citation deployment, section arcs — not content quality, theoretical sophistication, or domain-specific knowledge.

### Foundation Level 1: Knowledge Recognition

**Format**: 10-12 multiple choice + 3 short-answer diagnostic exercises
**Time**: 30 minutes
**Passing**: ≥80%

Questions test:
- Identifying citation functions (consensus, steelman, absence, tension)
- Recognizing good vs. bad topic sentences
- Identifying "The Turn" in a published introduction
- Diagnosing paragraph transition failures

### Foundation Level 2: Application with Feedback

**Format**: Construct arguments from provided materials
**Time**: 2-4 hours
**Passing**: ≥70/100

| Criterion | Points | How to Score |
|-----------|--------|--------------|
| Introduction follows WORLD → PROBLEM → GAP → QUESTION → PREVIEW | 20 | Check arc completeness; each step present and in order |
| Topic sentences are claims (not citations or descriptions) | 15 | Count: paragraphs with claim-first / total paragraphs |
| Transitions use lexical repetition + conceptual escalation | 15 | Check 3+ paragraph boundaries for concept threading |
| Citation deployment uses ≥3 of 4 functions appropriately | 15 | Label each citation cluster; count distinct functions |
| Gap statement specifies missing process/mechanism | 10 | Binary: specific mechanism gap vs. vague "more research" |
| Paragraph ordering exercise correct with rationale | 15 | Binary per paragraph; rationale quality 0-5 |
| Contribution paragraph follows 4-move pattern | 10 | Check: literature anchor → contrast → mechanism → implication |

### Foundation Level 3: Authentic Performance

**Format**: Write introduction, theory outline, contribution paragraphs, and closing from novel materials
**Time**: 4-8 hours
**Passing**: ≥70/100, no criterion below 50%

Same criteria as L2 but applied to independent work with no scaffolding. Expert comparison available for calibration.

**Open question**: Should Foundation L3 be a prerequisite for any domain's L3? The argument: every domain L3 requires written work, and that written work needs competent argument construction. Counter-argument: students may develop argument construction skills naturally through domain work — requiring it separately adds bureaucracy.

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
