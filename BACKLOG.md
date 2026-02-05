# Skill-Forge Backlog

## Priority 1: Immediate / High Impact

### 1.1 Rename to skill-forge
**Status:** Not started
**Why:** Parallel construction with theory-forge. Hyphenated for consistency.

**Implementation:**
- Rename repository: skillforge → skill-forge
- Update all internal references
- Update GitHub URL
- Redirect old URL

---

### 1.2 Quick Wins in Domain 1
**Status:** Not started
**Why:** Users should feel smarter on Day 1. Current Domain 1 takes too long.

**Implementation:**
- Streamline Level 1 to 1-2 hours max
- Add "immediate value" framing: "After this, you'll read papers differently"
- Create 5-minute diagnostic: "Can you already do this?"
- Fast-track for those who pass diagnostic

---

### 1.3 Explicit theory-forge Connection
**Status:** Partial (mentioned in capstone)
**Why:** Users should understand the ecosystem.

**Implementation:**
- README section: "skill-forge + theory-forge"
- Unlock messaging: "Complete Level 3 in all domains to use theory-forge responsibly"
- Shared terminology check
- Cross-link documentation

---

### 1.4 Anxiety-Reducing Messaging
**Status:** Not started
**Why:** PhD students fear AI replacement.

**Implementation:**
- Add "Why This Exists" section to README
- Frame: "AI will change research. This prepares you to direct AI, not be replaced."
- Capstone proves you know things AI doesn't
- Career positioning: "Researchers who can supervise AI are more valuable"

---

## Priority 2: Important / Medium Term

### 2.1 Reframe Levels
**Status:** Not started
**Why:** "Assessment" triggers anxiety. "Level 3 is where it counts" is scary.

**Implementation:**
- Level 1-2: "Practice" (unlimited attempts, rich feedback)
- Level 3: "Demonstration" (show what you can do)
- Level 4: "Integration" (capstone)
- Update all documentation with new framing

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
**Status:** Not started
**Why:** Social proof matters.

**Implementation:**
- Digital badges for each domain completion
- Shareable credentials (LinkedIn integration)
- "skill-forge certified" designation
- Cohort leaderboards (optional)

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

- [x] Level 4 Capstone specification (2025-02-04)
- [x] Capstone materials: surgery dataset (2025-02-04)
- [x] Domain 5 competency documentation
- [x] 7 domain specifications
- [x] Anonymization pipeline

---

*Last updated: 2025-02-04*
