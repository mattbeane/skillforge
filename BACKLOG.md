# Skill-Forge Backlog

## Priority 1: Immediate / High Impact

### 1.1 Rename to skill-forge
**Status:** ✅ Complete
**Why:** Parallel construction with theory-forge. Hyphenated for consistency.

**Implementation:**
- ✅ Renamed directory: skillforge → skill-forge
- ✅ Updated README branding
- ✅ Updated pyproject.toml (CLI: `skill-forge`, with `skillforge` alias for compatibility)
- ✅ Updated GitHub URLs
- Pending: GitHub repo rename (manual)

---

### 1.2 Quick Wins in Domain 1
**Status:** ✅ Complete
**Why:** Users should feel smarter on Day 1. Current Domain 1 takes too long.

**Implementation:**
- ✅ Created `assessments/domain-1-quick-start.md`
- ✅ 5-minute diagnostic with fast-track option
- ✅ Streamlined Level 1 (1-2 hours)
- ✅ "Time to value: 30 minutes" framing
- ✅ "After this, you'll read papers differently" messaging
- ✅ Pattern Recognition Checklist quick reference

---

### 1.3 Explicit theory-forge Connection
**Status:** ✅ Complete
**Why:** Users should understand the ecosystem.

**Implementation:**
- ✅ README section: "Skill-Forge + Theory-Forge: The Ecosystem"
- ✅ Unlock messaging table (which levels unlock which theory-forge features)
- ✅ "Why Both?" explanation (AI requires supervision)
- ✅ Capstone as "qualifying exam" framing
- ✅ Cross-link to theory-forge documentation

---

### 1.4 Anxiety-Reducing Messaging
**Status:** ✅ Complete
**Why:** PhD students fear AI replacement.

**Implementation:**
- ✅ Added "If You're Worried About AI Replacing Researchers..." section
- ✅ Frame: "AI doesn't know what it doesn't know"
- ✅ Lists what LLMs get wrong (genre, overclaiming, disconfirming evidence, etc.)
- ✅ "Researchers who can catch these mistakes are more valuable, not less"
- ✅ Capstone as proof of AI supervision capability
- ✅ "Becoming the human who knows when AI is wrong"

---

## Priority 2: Important / Medium Term

### 2.1 Reframe Levels
**Status:** ✅ Complete
**Why:** "Assessment" triggers anxiety. "Level 3 is where it counts" is scary.

**Implementation:**
- ✅ Level 1 → "Foundation" (establishes base understanding)
- ✅ Level 2 → "Practice" (active learning with guidance)
- ✅ Level 3 → "Mastery" (independent demonstration)
- ✅ Level 4 → "AI Supervisor" (capstone)
- ✅ Updated all 7 competency docs
- ✅ Updated README with new terminology
- ✅ Updated unlock table

---

### 2.2 Progressive Unlock
**Status:** Not started
**Why:** Each level should unlock something immediately useful.

**Implementation:**
- Domain 1 Level 1 → Can assess paper quality
- Domain 5 Level 1 → Can run eval-genre on own papers
- Domain 3 Level 2 → Can use mechanism mining tools
- Document what each level unlocks

---

### 2.3 Peer Learning Infrastructure
**Status:** Not started
**Why:** Solo assessment is lonely.

**Implementation:**
- Cohort system: groups progress together
- Peer review exercises at Level 2
- Discussion forum or Slack channel
- Study group formation tools

---

### 2.4 Faculty Dashboard
**Status:** Not started
**Why:** Advisors need visibility into student progress.

**Implementation:**
- Student progress view
- Weak area identification
- Comparison to cohort averages
- Suggested mentoring focus areas

---

### 2.5 Badges/Credentials
**Status:** ✅ Complete
**Why:** Social proof matters.

**Implementation:**
- ✅ Created `lib/credentials/` module with badges, issuer, paths
- ✅ 21 domain badges (7 domains × 3 levels: Foundation/Practice/Mastery)
- ✅ 4 path badges (Theory Builder, Evidence Analyst, Integrity Guardian, Full Researcher)
- ✅ AI Supervisor capstone badge
- ✅ Badge issuance on assessment completion
- ✅ CLI displays badges in `skill-forge status`
- ✅ Path progress tracking with visual progress bars
- ✅ UUID-based verification URLs (verification endpoint future work)

---

## Priority 3: Nice to Have / Long Term

### 3.1 Contributing Data = Status
**Status:** Not started
**Why:** Need faculty buy-in and more datasets.

**Implementation:**
- Recognition system for data contributors
- "My dissertation data is a skill-forge training set" badge
- Co-authorship on methodological papers about the system
- Annual "top contributors" acknowledgment

---

### 3.2 Video Walkthroughs
**Status:** Not started
**Why:** Some users learn better watching.

**Implementation:**
- Domain overview videos
- "How to approach Level 2" guides
- Expert think-alouds on sample assessments
- Host on YouTube, embed in docs

---

### 3.3 Conference Presence
**Status:** Not started
**Why:** Community building requires visibility.

**Implementation:**
- AOM workshop proposal
- Doctoral consortium demos
- Methods conference presentations
- Partner with PhD program directors

---

### 3.4 Calibration Exercises for Faculty
**Status:** Not started
**Why:** Faculty tacit knowledge differs; calibration reveals this.

**Implementation:**
- Faculty can take assessments
- Compare faculty responses to each other
- Identify where "expert" opinions diverge
- Use for research on tacit knowledge

---

### 3.5 Multiple Entry Points
**Status:** Not started
**Why:** Different users have different needs.

**Implementation:**
- "I'm a first-year PhD" track
- "I'm faculty evaluating this" track
- "I'm a researcher wanting AI tools" track
- Tailored onboarding for each

---

## Content Backlog

### C1: Additional Capstone Datasets
**Status:** 1 dataset (surgery)
**Why:** Need rotation to prevent answer sharing.

**Implementation:**
- Recruit 2-3 faculty contributors
- Generate AI drafts for each
- Create issue keys
- Document rotation schedule

---

### C2: Level 2-3 Assessments for All Domains
**Status:** Incomplete
**Why:** Full curriculum not built.

**Implementation:**
- Prioritize by domain usage frequency
- Domain 5 (Genre) Level 2-3
- Domain 3 (Mechanism) Level 2-3
- Domain 7 (Verification) Level 2-3

---

### C3: More Expert Baselines
**Status:** 1 baseline (surgery)
**Why:** More examples = better calibration.

**Implementation:**
- Different methodological approaches
- Different empirical contexts
- Different career stages

---

## Technical Debt

### T1: CLI Implementation
Current CLI is placeholder.

### T2: Student Record Tracking
No persistence layer yet.

### T3: Automated Scoring
Level 1 can be auto-scored; Level 2-3 need rubric automation.

### T4: Progress Persistence
Track attempts, scores, feedback history.

---

## Completed

- [x] P2.1: Reframe levels (Foundation/Practice/Mastery) (2025-02-04)
- [x] P2.5: Badge system with domain/path badges (2025-02-04)
- [x] P1.1: Rename to skill-forge (2025-02-04)
- [x] P1.2: Quick wins in Domain 1 (2025-02-04)
- [x] P1.3: Explicit theory-forge connection (2025-02-04)
- [x] P1.4: Anxiety-reducing messaging (2025-02-04)
- [x] Level 4 Capstone specification (2025-02-04)
- [x] Capstone materials: surgery dataset (2025-02-04)
- [x] Domain 5 competency documentation
- [x] 7 domain specifications
- [x] Anonymization pipeline

---

*Last updated: 2025-02-04*
