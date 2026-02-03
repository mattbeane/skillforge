# ResearchKit Quals

A competency assessment and gating system for TheoryForge.

## Purpose

TheoryForge is a powerful paper-mining pipeline that encodes expert research methodology knowledge. But power tools in untrained hands can produce polished-looking work without genuine understanding.

ResearchKit Quals ensures students develop the underlying competencies BEFORE gaining access to TheoryForge's advanced capabilities.

## Philosophy

**Competency-based, not time-based**: No arbitrary waiting periods. Students prove readiness through demonstrated skill.

**Authentic assessment**: Tests require doing actual research work—not multiple choice questions about research.

**Progressive unlocking**: Master fundamentals before accessing advanced capabilities. Domains build on each other.

**Advisor-verifiable**: Faculty can review student work and accelerate progression (but not skip domains).

## The Seven Domains

| Domain | Core Skill | Unlocks |
|--------|------------|---------|
| 1. Pattern Recognition | See signal in noise | `/hunt-patterns` |
| 2. Theoretical Positioning | Know what's a contribution | `/find-theory`, `/find-lens` |
| 3. Qualitative Mechanism Extraction | Code data systematically | `/mine-qual` |
| 4. Theoretical Framing | Generate and evaluate framings | `/smith-frames`, `/eval-zuckerman` |
| 5. Epistemological Genre | Distinguish discovery from testing | `/eval-genre`, `/draft-paper` |
| 6. Adversarial Evidence | Find disconfirming evidence | `/audit-claims`, `/verify-claims` |
| 7. Claim Verification | Match claims to evidence honestly | `/package-verification` |

## Assessment Levels

### Level 1: Knowledge Recognition
- Necessary but not sufficient
- Tests conceptual understanding
- Identifies knowledge gaps to address
- Multiple choice, terminology matching

### Level 2: Application with Feedback
- Students apply concepts to provided materials
- AI provides detailed feedback comparing to expert work
- Multiple attempts allowed
- Used for learning and building competence

### Level 3: Authentic Performance
- Real research task with real data
- Work submitted for evaluation
- Single attempt per assessment period
- Required for unlocking TheoryForge commands

## Time to Full Access

Typical PhD student: 3-6 months
- Domains 1-2: 2-4 weeks (foundational)
- Domain 3: 2-4 weeks (requires data practice)
- Domains 4-5: 4-6 weeks (iteration and feedback)
- Domains 6-7: 2-4 weeks (builds on prior)

**Fast track**: Students with prior qual methods training can test out of Domains 1-3 immediately.

## Directory Structure

```
researchkit-quals/
├── competencies/       # Competency definitions & rubrics
├── assessments/        # Assessment specifications by level
├── materials/          # Datasets for assessments
├── grading/            # Evaluation rubrics & expert baselines
├── student-records/    # Progress tracking per student
└── commands/           # CLI for taking/grading assessments
```

## Integration with TheoryForge

TheoryForge checks `~/.researchkit-quals/[student-id]/unlock-status.json` before running gated commands. Students see helpful messages about which competencies they need to develop.

## Advisor Role

Advisors can:
- Review student assessment work
- Accelerate Level 2 → Level 3 progression
- Certify competence without full assessment

Advisors cannot:
- Skip entire domains (pedagogical sequencing preserved)
- Override without reviewing work

## Getting Started

```bash
# Check your current status
/quals-status

# Take a Level 1 assessment
/quals-take domain-1 level-1

# Submit Level 3 work for evaluation
/quals-submit domain-3 --file my-coding.md
```

---

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
- ✅ 7 competency domain definitions
- ✅ Assessment specifications with scoring rubrics
- ✅ Command→competency unlock mapping
- ✅ Atlas.ti parser (extracts quotes with codes)
- ✅ Anonymization engine (3-stage NER + review + apply)

**Not Yet Built:**
- ⏳ Assessment question banks (Level 1)
- ⏳ Expert baselines (from contributed data)
- ⏳ quals CLI commands (take, submit, status)
- ⏳ TheoryForge integration code

See `TODO.md` for implementation roadmap.
