# Badge Verification System

Git-based proof of work for Skill-Forge badges.

## Overview

Badges are verified through GitHub commit history. No central database needed—the student's repo IS the credential.

---

## Portfolio Repository Structure

Students fork `skill-forge/portfolio-template`:

```
skill-forge-portfolio/
├── README.md                    # Auto-generated progress dashboard
├── BADGES.md                    # Earned badges with verification links
├── .skill-forge/
│   └── config.yaml              # Student metadata, settings
│
├── domain-1-pattern-recognition/
│   ├── foundation/
│   │   ├── exercise-1.md        # Completed exercise
│   │   ├── exercise-2.md
│   │   └── ASSESSMENT.md        # Self-assessment + AI feedback
│   ├── practice/
│   │   ├── exercise-1.md
│   │   └── ASSESSMENT.md
│   └── mastery/
│       ├── exercise-1.md
│       └── ASSESSMENT.md
│
├── domain-2-theoretical-positioning/
│   └── ... (same structure)
│
├── ... (domains 3-7)
│
├── paths/
│   ├── theory-builder/
│   │   └── COMPLETION.md        # Path completion evidence
│   └── ...
│
└── capstone/
    ├── review-task.md           # The AI-generated paper they reviewed
    ├── my-review.md             # Their review catching issues
    ├── issues-found.md          # Documented issues they identified
    └── ASSESSMENT.md            # Grading against rubric
```

---

## Badge Issuance Flow

### 1. Student completes work

```bash
# Student works on domain 1 foundation
cd domain-1-pattern-recognition/foundation/
# ... completes exercises ...
git add .
git commit -m "Complete D1 Foundation exercises"
git push
```

### 2. Student requests badge check

In Claude Code:
```
/skill-forge check d1-foundation
```

Claude Code:
1. Reads their local repo
2. Verifies required files exist with substantive content
3. Checks commit history shows genuine work (not just copy-paste)
4. Runs assessment criteria
5. If passed → issues badge

### 3. Badge issuance = Git tag

```bash
# Claude Code executes:
git tag -a "badge/d1-foundation/2025-02-04" \
  -m "Domain 1: Pattern Recognition - Foundation

Issued: 2025-02-04
Verified by: Skill-Forge v1.0
Evidence commits: abc123, def456, ghi789

Assessment: PASSED
- Exercise completion: ✓
- Quality threshold: ✓
- Original work check: ✓"

git push origin "badge/d1-foundation/2025-02-04"
```

### 4. BADGES.md auto-updated

```markdown
# Earned Badges

## Domain Badges

### 🔍 Pattern Recognition

| Level | Badge | Earned | Verify |
|-------|-------|--------|--------|
| Foundation | ![badge](icons/d1-foundation.png) | 2025-02-04 | [Verify](../../releases/tag/badge/d1-foundation/2025-02-04) |
| Practice | ![badge](icons/d1-practice.png) | 2025-02-05 | [Verify](../../releases/tag/badge/d1-practice/2025-02-05) |
| Mastery | 🔒 | — | — |

...
```

---

## Verification

Anyone can verify a badge:

1. **Click verification link** → Goes to GitHub tag
2. **See tag message** → Shows what was verified
3. **Browse commit history** → See the actual work
4. **Inspect files** → Read their exercise submissions

**Example verification URL:**
```
https://github.com/student/skill-forge-portfolio/releases/tag/badge/ai-supervisor/2025-02-04
```

---

## Badge Requirements

### Domain Badges

Each level requires:

| Level | Requirements |
|-------|--------------|
| Foundation | Complete 2-3 exercises demonstrating concept knowledge |
| Practice | Complete 2-3 exercises applying skills with AI feedback |
| Mastery | Complete 1-2 exercises demonstrating independent judgment |

**Verification checks:**
- [ ] Required files exist
- [ ] Files have substantive content (>500 chars, not boilerplate)
- [ ] Commits show iterative work (not single dump)
- [ ] Assessment criteria met (per-domain rubric)

### Path Badges

Automatically issued when component domain masteries are achieved:

| Path | Required Domain Masteries |
|------|---------------------------|
| Theory Builder | D1 + D2 + D4 + D5 |
| Evidence Analyst | D1 + D3 + D6 |
| Integrity Guardian | D6 + D7 |
| Full Researcher | D1-D7 (all) |

### Capstone Badge: AI Supervisor

Requires:
1. All 7 domain masteries
2. Capstone exercise:
   - Given: AI-generated research paper with planted issues
   - Task: Write a review identifying all critical issues
   - Pass: Find ≥80% of planted issues + no false positives on correct sections

---

## Anti-Gaming Measures

### 1. Commit history inspection

Badge issuance checks:
- Multiple commits over time (not single dump)
- Commit messages show progression
- File diffs show actual work, not copy-paste

### 2. Content quality gates

- Minimum content length per exercise
- Semantic checks (is this actually answering the prompt?)
- Plagiarism detection against template/other portfolios

### 3. Assessment variation

- Exercise prompts have randomized elements
- Capstone uses different planted issues per student
- Can't just copy someone else's answers

### 4. Public auditability

- Anyone can inspect the repo
- Fraudulent badges get called out by community
- Reputation matters in academic circles

---

## CLI Commands

```bash
# Check status
/skill-forge status
# Shows: progress per domain, badges earned, next steps

# Request badge check
/skill-forge check d1-foundation
# Runs verification, issues badge if passed

# View all badges
/skill-forge badges
# Shows earned badges with verification links

# Initialize portfolio
/skill-forge init
# Forks template, sets up local repo

# Sync progress
/skill-forge sync
# Updates README.md and BADGES.md from current state
```

---

## Implementation Components

### 1. Portfolio template repo

`skill-forge/portfolio-template` containing:
- Directory structure
- Exercise prompts (in each domain folder)
- README template with progress tracking
- GitHub Actions for auto-updating BADGES.md

### 2. Verification module

`lib/credentials/verification.py`:
```python
def verify_domain_badge(repo_path: Path, domain: int, level: str) -> VerificationResult:
    """Check if domain badge requirements are met."""

def issue_badge(repo_path: Path, badge_id: str) -> bool:
    """Create and push badge tag."""

def check_commit_history(repo_path: Path, domain: int) -> bool:
    """Verify commits show genuine work progression."""
```

### 3. Assessment rubrics

`competencies/domain-N/rubric.yaml`:
```yaml
foundation:
  exercises: 3
  criteria:
    - name: "Concept identification"
      description: "Can identify X in examples"
      check: "semantic_match"
    - name: "Vocabulary usage"
      description: "Uses correct terminology"
      check: "keyword_presence"

practice:
  exercises: 2
  criteria:
    - name: "Application"
      description: "Applies concept to new case"
      check: "semantic_match"
    # ...
```

---

## Example: Full Badge Issuance

```
$ /skill-forge check d1-mastery

Checking Domain 1: Pattern Recognition - Mastery...

✓ Required files present
  - domain-1-pattern-recognition/mastery/exercise-1.md (2,340 chars)
  - domain-1-pattern-recognition/mastery/ASSESSMENT.md (1,205 chars)

✓ Commit history shows progression
  - 4 commits over 3 days
  - Meaningful diffs (not copy-paste)

✓ Assessment criteria
  - Pattern identification: PASS
  - False positive recognition: PASS
  - Justification quality: PASS

🎖️ BADGE EARNED: D1-MASTERY

Creating tag: badge/d1-mastery/2025-02-04
Pushing to origin...

Badge issued! Verify at:
https://github.com/you/skill-forge-portfolio/releases/tag/badge/d1-mastery/2025-02-04

Updated BADGES.md ✓
```

---

## Privacy Considerations

- Portfolio can be private (verification still works via link for authorized viewers)
- Student controls what's public
- Can use pseudonym in config
- Email not exposed in tags (use GitHub username only)

---

## Future: Employer Verification

Recruiters/hiring managers can:
1. Ask candidate for portfolio link
2. Inspect badges and underlying work
3. See exactly what they did, not just that they "passed"
4. Judge quality themselves

This is **better than a certificate**—it's a portfolio of demonstrated work.
