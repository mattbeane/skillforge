# ResearchKit Quals - What's Actually Left To Build

## Status: Tools Built, Assessment Materials Needed

**Completed:**
- Atlas.ti parser - extracts quotes with codes
- Anonymization engine (3 stages) - NER detection, review, application
- Competency definitions (7 domains)
- Assessment specifications with scoring rubrics
- Command unlock map

**Critical Path:** Matt needs to run anonymization on his dissertation data, then we have a seed contribution for testing.

---

## Phase 1: Seed Data & Pilot (Matt's Data)

### Step 1: Complete Anonymization (2-3 hours)
- [x] Parse Atlas.ti project → `beane-surgery-extracted.json`
- [x] Run Stage 1 detection → `beane-surgery-entities.json`
- [ ] **Run Stage 2 review** (interactive - Matt must do this)
  ```bash
  cd /Users/mattbeane/knowledge-work/projects/researchkit-quals
  python3.11 tools/anonymize.py review seed-data/beane-surgery-entities.json
  ```
- [ ] **Run Stage 3 application** (after review complete)
  ```bash
  python3.11 tools/anonymize.py apply \
      seed-data/beane-surgery-entities.reviewed.json \
      seed-data/beane-surgery-extracted.json \
      --output-dir seed-data/beane-surgery-anonymized/ --verify
  ```
- [ ] **Sign contributor form**

### Step 2: Create Expert Baseline (4-6 hours - Matt's tacit knowledge)
- [ ] Document top 3 mechanisms from dissertation
- [ ] Identify key quotes for each mechanism
- [ ] Document disconfirming evidence found
- [ ] Write up "what makes a good coding" notes

### Step 3: Write Level 1 Quiz Questions (2-3 hours)
- [ ] Domain 1: Pattern Recognition (12 questions)
- [ ] Domain 3: Qual Mechanism Extraction (12 questions)
- [ ] Domain 7: Claim Verification (12 questions)

**Phase 1 Total: ~10-15 hours of Matt's time**

---

## Phase 2: Build the Infrastructure

### quals CLI Commands (6-8 hours)
- [ ] `quals-status` - Show progress and unlocks
- [ ] `quals-take D1 L1` - Take Level 1 quiz
- [ ] `quals-submit D3 L3` - Submit Level 3 work
- [ ] Student record schema (JSON)
- [ ] Progress tracking

### TheoryForge Integration (2-3 hours)
- [ ] Competency gate function
- [ ] Integration with command dispatch
- [ ] Helpful "locked" messages

### Level 2 Feedback System (4-6 hours)
- [ ] Compare student coding to expert baseline
- [ ] Generate feedback report
- [ ] Track attempts

---

## Phase 3: Expand Domain Coverage

After pilot works with Matt's data:

- [ ] Domain 2: Theoretical Positioning assessment
- [ ] Domain 4: Theoretical Framing (Zuckerman rubric-eval)
- [ ] Domain 5: Epistemological Genre assessment
- [ ] Domain 6: Adversarial Evidence assessment

---

## Phase 4: Scale

- [ ] Solicit faculty data contributions
- [ ] Build contribution acceptance workflow
- [ ] Create 2nd assessment set (retakes)
- [ ] Build advisor certification workflow
- [ ] Create student dashboard

---

## What's Working Right Now

### Atlas.ti Parser
```bash
python3 tools/atlasti_parser.py "Project.atlpac" output.json
```
- Extracts all coded quotations
- Maps codes (tags) to quotes
- Preserves document structure
- Handles .atlpac archives directly

### Anonymization Engine
```bash
# Stage 1: Detect entities
python3.11 tools/anonymize.py detect input.json

# Stage 2: Review (interactive)
python3.11 tools/anonymize.py review input.entities.json

# Stage 3: Apply and verify
python3.11 tools/anonymize.py apply reviewed.json source.json --output-dir out/ --verify
```

**Requires:** spaCy with en_core_web_sm model
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

---

## Critical Dependencies

1. **Matt must complete Stage 2 review** - Only he knows what's identifying
2. **Matt must create expert baseline** - Can't outsource his tacit knowledge
3. **Need pilot students** - Test before full deployment

---

## Files Structure

```
researchkit-quals/
├── README.md                    # Overview
├── QUICK_START.md               # 1-page student guide
├── TODO.md                      # This file
│
├── competencies/                # Domain definitions (complete)
│   ├── domain-1-pattern-recognition.md
│   ├── domain-2-theoretical-positioning.md
│   ├── domain-3-qual-mechanism-extraction.md
│   ├── domain-4-theoretical-framing.md
│   ├── domain-5-epistemological-genre.md
│   ├── domain-6-adversarial-evidence.md
│   └── domain-7-claim-verification.md
│
├── assessments/
│   └── ASSESSMENT_SPECS.md      # Scoring rubrics
│
├── commands/
│   ├── unlock-map.json          # Command → competency requirements
│   └── quals-status.md          # Status command spec
│
├── tools/                       # Working tools
│   ├── atlasti_parser.py        # Parse .atlpac files
│   ├── anonymize.py             # Main anonymization CLI
│   ├── anonymize_stage1.py      # NER detection
│   ├── anonymize_stage2.py      # Human review
│   └── anonymize_stage3.py      # Apply & verify
│
└── seed-data/                   # Matt's dissertation (WIP)
    ├── beane-surgery-extracted/     # Parsed project
    ├── beane-surgery-extracted.json # Quotations + codes
    └── beane-surgery-entities.json  # Detected entities
```
