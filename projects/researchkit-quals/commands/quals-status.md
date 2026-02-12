# ResearchKit Quals Status

Show current competency progress across research domains.

## Usage

```
/quals-status [student-id]
```

If `student-id` not provided, checks for `.researchkit-quals/student-id` in home directory.

## Behavior

1. **Load student record**
   ```
   ~/.researchkit-quals/[student-id]/unlock-status.json
   ```

2. **Display competency progress**

   ```
   ┌─────────────────────────────────────────────────────────────┐
   │  ResearchKit Quals - Student: [name]                        │
   └─────────────────────────────────────────────────────────────┘

   COMPETENCY PROGRESS
   ════════════════════════════════════════════════════════════════

   Domain 1: Pattern Recognition & Data Sense
   ├── Level 1: ████████████████████ PASSED (92%)
   ├── Level 2: ████████████████████ PASSED (78%)
   └── Level 3: ████████████████████ PASSED (85%)

   Domain 2: Theoretical Positioning
   ├── Level 1: ████████████████████ PASSED (88%)
   ├── Level 2: ████████████░░░░░░░░ IN PROGRESS (attempt 2)
   └── Level 3: ░░░░░░░░░░░░░░░░░░░░ LOCKED

   Domain 3: Qualitative Mechanism Extraction
   ├── Level 1: ░░░░░░░░░░░░░░░░░░░░ LOCKED (requires Domain 2, Level 3)
   ├── Level 2: ░░░░░░░░░░░░░░░░░░░░ LOCKED
   └── Level 3: ░░░░░░░░░░░░░░░░░░░░ LOCKED

   [Domains 4-7 similar...]

   NEXT STEPS
   ════════════════════════════════════════════════════════════════

   → Complete Domain 2, Level 2 assessment

   Run: /quals-take domain-2 level-2
   ```

3. **Show time estimates**

   ```
   ESTIMATED TIME TO FULL ACCESS
   ════════════════════════════════════════════════════════════════

   Based on your current progress: ~8-12 weeks

   Current: Domain 2, Level 2
   Remaining: Domains 2-7, ~6 assessments

   Accelerate: Ask your advisor to certify competence for domains
   where you have prior training.
   ```

## Output Files

None created. Display only.

## Student Record Structure

```json
{
  "student_id": "jsmith",
  "name": "Jane Smith",
  "advisor": "Prof. Beane",
  "started": "2025-01-15",

  "domains": {
    "domain-1": {
      "level-1": {
        "status": "passed",
        "score": 92,
        "passed_at": "2025-01-20",
        "attempts": 1
      },
      "level-2": {
        "status": "passed",
        "score": 78,
        "passed_at": "2025-01-28",
        "attempts": 2
      },
      "level-3": {
        "status": "passed",
        "score": 85,
        "passed_at": "2025-02-05",
        "attempts": 1,
        "certified_by": null
      }
    },
    "domain-2": {
      "level-1": {
        "status": "passed",
        "score": 88,
        "passed_at": "2025-02-08",
        "attempts": 1
      },
      "level-2": {
        "status": "in_progress",
        "attempts": 2,
        "last_attempt": "2025-02-12",
        "last_score": 65,
        "feedback_file": "domain-2-level-2-attempt-2-feedback.md"
      },
      "level-3": {
        "status": "locked"
      }
    }
  },

  "advisor_actions": [
    {
      "date": "2025-02-01",
      "action": "certified",
      "domain": "domain-1",
      "level": 3,
      "notes": "Prior qual methods training at Stanford"
    }
  ]
}
```

## Error Handling

**No student record found**:
```
No ResearchKit Quals record found for this user.

To start:
  /quals-init [your-name]

Or ask your advisor to create your record.
```

**Student ID not configured**:
```
No student ID configured.

Set your student ID:
  echo "jsmith" > ~/.researchkit-quals/student-id

Or provide it directly:
  /quals-status jsmith
```
