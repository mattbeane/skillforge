# ResearchKit Quals

A framework for identifying and developing the research competencies PhD students need to produce rigorous, publishable work.

## Purpose

Power tools in untrained hands produce polished-looking work without genuine understanding. But the deeper problem isn't tool access — it's that we rarely make explicit what "good research instincts" actually are or how to develop them.

ResearchKit Quals is our current attempt to name these skills, describe what competence looks like, and think about how to assess them. It's a draft, not a decree — we expect this framework to change significantly through faculty and student input.

## Philosophy

**Competency-based, not time-based**: No arbitrary waiting periods. Students prove readiness through demonstrated skill.

**Authentic assessment**: Tests require doing actual research work — not multiple choice questions about research.

**Progressive development**: Some skills build on others. We think the sequencing below is roughly right, but which domains are truly prerequisite vs. parallel is an open question.

**Advisor-verifiable**: Faculty can review student work and accelerate progression.

## Foundational Skills (Draft)

Some skills cross-cut all domains — they're the medium through which domain-specific competencies are demonstrated. We're calling these "foundational skills" to distinguish them from the numbered domains.

| Foundation | Core Question | Status |
|------------|---------------|--------|
| **Argument Construction** | Can you build a paragraph, a section, and a paper that moves a reader from puzzle to contribution? | Draft — see `competencies/foundation-argument-construction.md` |

This is our first attempt to handle skills that don't fit into a single domain (see Open Question #6 below). Argument construction — paragraph architecture, transitions, citation deployment, section-level arcs — is required everywhere but doesn't belong to any one domain. Whether it should be assessed separately or emerges through domain assessments is an open question.

```
Foundation: Argument Construction (prerequisite or parallel)
         ↓
1 → 2 → 3 → 4 → 5 → 6 → 7
         ↗ (possibly parallel)
```

## The Domains (Draft)

We currently think there are seven core research competencies. This list is up for discussion — what's missing? What should be combined? What's mislabeled?

| # | Domain | Core Question |
|---|--------|---------------|
| 1 | Pattern Recognition & Data Sense | Can you see what's worth pursuing in data — and kill what isn't? |
| 2 | Theoretical Positioning | Do you know what makes a finding a *contribution*? |
| 3 | Qualitative Mechanism Extraction | Can you code data systematically and find disconfirming evidence? |
| 4 | Theoretical Framing | Can you generate multiple framings for the same finding and choose wisely? |
| 5 | Epistemological Genre | Do you know the difference between discovery and testing — and can you write authentically in each? |
| 6 | Adversarial Evidence Handling | Can you audit your own claims against ALL the data? |
| 7 | Claim Verification & Integrity | Do your claims match your evidence — honestly? |

## Suggested Sequencing

We think these domains build on each other roughly in order: you need pattern recognition before theoretical positioning, and you need both before you can extract mechanisms from qualitative data, etc. But some domains might be more parallel than sequential (e.g., Epistemological Genre might not strictly require Theoretical Framing).

Argument Construction (the foundational skill) can be developed in parallel with domain work or as a prerequisite — this is an open question.

Students with prior qualitative methods training may be able to demonstrate competence in early domains immediately.

## Assessment Approach (Draft)

We're currently thinking about three levels of assessment per domain:

### Level 1: Knowledge Recognition
- Conceptual understanding (multiple choice, terminology)
- Necessary but not sufficient
- Unlimited retakes

### Level 2: Application with Feedback
- Apply concepts to provided materials
- AI + expert comparison with detailed feedback
- Multiple attempts allowed, used for learning

### Level 3: Authentic Performance
- Real research task with real data
- Work evaluated against expert baseline
- Required for demonstrated competence

**Whether rubric-based assessment is appropriate for all domains is an open question.** Some competencies (like research integrity under pressure) may only be developed through mentorship and modeling, not formal assessment.

## Time Estimates

Typical PhD student working through all domains: 3-6 months
With prior qual methods training: 6-10 weeks (test out of early domains)

## Directory Structure

```
researchkit-quals/
├── competencies/       # Competency definitions & rubrics
├── assessments/        # Assessment specifications by level
├── materials/          # Datasets for assessments
├── grading/            # Evaluation rubrics & expert baselines
├── student-records/    # Progress tracking per student
├── tools/              # Data anonymization pipeline
└── commands/           # CLI for taking/grading assessments
```

## Advisor Role

Advisors can:
- Review student assessment work
- Accelerate Level 2 → Level 3 progression
- Certify competence without full assessment (up to 3 domains)

Advisors cannot:
- Skip entire domains (pedagogical sequencing preserved)
- Override without reviewing work

## For Contributors: The Anonymization Engine

Faculty can contribute their dissertation or prior study data to create assessment materials. The anonymization engine ensures data is safe before contribution.

### Three-Stage Process

1. **Stage 1: Automatic Detection** (`anonymize.py detect`)
   - NER (Named Entity Recognition) for people, orgs, locations
   - Regex patterns for PII (emails, phones, dates, MRNs)
   - Medical/hospital-specific patterns (OR numbers, room numbers)
   - Risk flagging for identifying role+context combinations

2. **Stage 2: Guided Human Review** (`anonymize.py review`)
   - Interactive CLI for reviewing each detected entity
   - Assign pseudonyms (Dr. A, Hospital B, Site C)
   - Mark false positives from NER errors
   - Save progress and resume later

3. **Stage 3: Verification & Application** (`anonymize.py apply`)
   - Apply all replacements to source documents
   - Generate comprehensive audit report
   - Run re-identification check
   - Create contributor sign-off template

### Quick Start (Contributors)

```bash
# 1. Parse your Atlas.ti project
python tools/atlasti_parser.py "My Project.atlpac" parsed_data.json

# 2. Run detection
python tools/anonymize.py detect parsed_data.json

# 3. Review entities (interactive)
python tools/anonymize.py review parsed_data.entities.json

# 4. Apply and verify
python tools/anonymize.py apply parsed_data.entities.reviewed.json parsed_data.json \
    --output-dir contribution/ --verify
```

### What Gets Detected

| Type | Examples | Replacement Pattern |
|------|----------|---------------------|
| PERSON | Dr. Smith, Nurse Jones | Dr. A, Nurse B |
| ORG | Lahey, MGH, Hospital | Hospital A, Center B |
| GPE | Boston, California | Site A, Region B |
| FAC | OR 17, Room 3, Floor 4 | OR 1, Room 1, Floor 1 |
| DATE | 2014-07-15, July 2014 | [date removed] |
| EMAIL | name@hospital.org | [email removed] |
| PHONE | 617-555-1234 | [phone removed] |

### Trust Model

- **All processing runs locally** - your data never leaves your machine
- **You review all detections** before anonymization is applied
- **You sign off** on the final anonymized version
- **Audit trail** documents every change for reproducibility

### Output Package

After anonymization, contributors receive:
- `anonymized_quotations.json` - Ready for use in assessments
- `audit_report.md` - Every replacement documented
- `contributor_signoff.md` - Sign-off template for IRB compliance

---

## Current Status

**Built:**
- 7 competency domain definitions (draft)
- Assessment specifications with scoring rubrics (draft)
- Atlas.ti parser (extracts quotes with codes)
- Anonymization engine (3-stage NER + review + apply)

**Not Yet Built:**
- Assessment question banks (Level 1)
- Expert baselines (from contributed data)
- quals CLI commands (take, submit, status)

See `TODO.md` for implementation roadmap.

---

## Open Questions for Discussion

These are genuine questions we'd like faculty and student input on:

1. **Is this the right set of domains?** What research competencies are missing? What's listed here that shouldn't be a separate domain?

2. **Is the sequencing right?** We think these build on each other in order, but could some be parallel? Does Epistemological Genre really require Theoretical Framing as a prerequisite, or are they independent skills?

3. **Is rubric-based assessment appropriate for all domains?** Some skills (like research integrity, or finding discipline) might resist formal assessment. Are there domains better served by mentorship and modeling?

4. **How should prior training be credited?** We allow "testing out" of early domains, but what counts as evidence of prior competence? A course grade? A published paper? Advisor attestation?

5. **Are the three assessment levels right?** Knowledge → Application → Authentic Performance seems sound, but is Level 1 (multiple choice) actually useful, or is it just a speed bump?

6. **What about skills that cross domains?** For example, "knowing when to kill a finding" appears in Pattern Recognition but also matters in Theoretical Framing and Adversarial Evidence. We're experimenting with a "foundational skills" layer (see Argument Construction above) as one way to handle this — is that the right architecture, or should cross-cutting skills be woven into each domain instead?

7. **How domain-specific should this be?** These competencies are written from a qualitative/mixed-methods organizational studies perspective. How much would need to change for other methodological traditions?
