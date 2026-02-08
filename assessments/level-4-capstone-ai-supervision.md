# Level 4: Capstone Assessment - AI Output Supervision

## What This Is

The integrative final assessment. Students prove they've internalized all seven domains by catching errors in an AI-generated research paper.

**Prerequisite**: Level 3 pass in all seven domains.

**Time**: 4-6 hours (can be split across sessions)

**Attempts**: One. This is the qualifying exam.

---

## The Setup

### Materials Provided

1. **Raw dataset**: Anonymized qualitative data from a faculty contributor
   - Interview transcripts (15-30 interviews)
   - Field notes
   - Any available quantitative data

2. **AI-generated paper**: A "draft" produced by running the dataset through an uncalibrated AI pipeline
   - Full manuscript (~8,000-12,000 words)
   - Abstract, intro, theory, methods, findings, discussion
   - Reference list

3. **Expert baseline** (revealed after submission): What a skilled researcher found in the same data, and what they would catch in the AI draft

### How the AI Draft Is Generated

The AI draft is deliberately produced WITHOUT the safeguards that make theory-forge reliable:
- No human confirmation at gates
- No iterative checking
- Default LLM tendencies uncorrected

This produces a paper that *looks* polished but contains systematic errors across all domains—exactly what a naive user might accept.

**Error types seeded:**
- Pattern noise mistaken for signal (Domain 1)
- Overclaimed contribution (Domain 2)
- Mechanism misidentified or shallow (Domain 3)
- Mushy framing, wrong literature (Domain 4)
- Hypo-deductive language in discovery paper (Domain 5)
- Front-loaded abstract: discoveries presented as premises (Domain 5)
- Disconfirming evidence ignored or buried (Domain 6)
- Claims that outrun evidence (Domain 7)

---

## The Task

### Part A: Issue Identification (60%)

Review the AI-generated paper and identify all issues. For each issue:

1. **Location**: Page/paragraph/line
2. **Domain**: Which of the 7 domains does this violate?
3. **Problem**: What specifically is wrong?
4. **Evidence**: How do you know it's wrong? (reference to data, logic, standards)
5. **Severity**: Critical / Major / Minor

**Format**: Structured issue log (template provided)

**What counts as an issue:**
- Factual errors (AI misread the data)
- Interpretive errors (AI drew wrong conclusions)
- Framing errors (positioning, contribution, genre)
- Missing elements (disconfirming evidence not addressed)
- Overclaims (claims exceed what evidence supports)
- Craft errors (language, structure, conventions)

### Part B: Prioritized Revision Plan (20%)

You can't fix everything. Given the issues you found:

1. **Rank the top 5 issues** that would cause desk rejection or R&R failure
2. **Explain why** each is critical
3. **Describe the fix** (what would need to change)

This tests judgment, not just detection.

### Part C: Meta-Reflection (20%)

Short essay (500-800 words):

1. What systematic patterns did you notice in the AI's errors?
2. Which domains showed the most severe problems? Why might AI struggle there?
3. What would you do differently if you were supervising this AI in real-time rather than reviewing after the fact?

---

## Evaluation

### Part A Scoring

| Criterion | Points |
|-----------|--------|
| Found ≥80% of critical issues | 25 |
| Found ≥70% of major issues | 20 |
| Correctly classified by domain | 10 |
| Evidence/reasoning is sound | 15 |
| Didn't flag false positives (≤3 incorrect flags) | 10 |
| **Subtotal** | **80** |

*Scaled to 60% of total*

### Part B Scoring

| Criterion | Points |
|-----------|--------|
| Top 5 issues are genuinely critical | 15 |
| Prioritization reasoning is sound | 10 |
| Proposed fixes would actually work | 10 |
| **Subtotal** | **35** |

*Scaled to 20% of total*

### Part C Scoring

| Criterion | Points |
|-----------|--------|
| Identifies systematic AI failure patterns | 10 |
| Shows domain-specific insight | 10 |
| Practical supervision recommendations | 10 |
| **Subtotal** | **30** |

*Scaled to 20% of total*

### Passing Threshold

- **Overall**: ≥70%
- **Part A minimum**: ≥50% (must demonstrate detection ability)
- **Critical issues minimum**: Must find ≥70% of critical issues

---

## What This Tests

### Integration
Can you apply all seven domains simultaneously on a realistic artifact?

### Judgment
Can you distinguish critical problems from minor ones?

### Practical Wisdom
Do you understand *why* AI makes these errors and how to prevent them?

### Craft Ownership
When AI produces something plausible-looking, can you tell it's not actually good?

---

## Why This Matters

This is the job now. Researchers will increasingly use AI assistance. The skill isn't "do everything yourself"—it's "know enough to catch what AI gets wrong."

A student who passes this assessment can:
- Use AI tools productively without being misled
- Catch errors that would sink a paper at review
- Supervise junior researchers or collaborators using AI
- Maintain craft standards in an AI-augmented workflow

A student who fails reveals:
- Gaps in domain knowledge (which domains did they miss?)
- Overreliance on surface plausibility
- Inability to integrate skills under realistic conditions

---

## Generating Assessment Materials

### For Faculty Contributors

To create a new capstone assessment:

1. **Contribute anonymized data** via the standard pipeline
2. **Provide expert baseline**:
   - What patterns exist in this data?
   - What mechanisms operate?
   - What's the real contribution potential?
   - What would you catch if AI wrote this?

3. **Generate AI draft**: Run data through uncalibrated pipeline
4. **Validate issues**: Expert reviews AI draft, creates issue key
5. **Calibrate difficulty**: Ensure mix of obvious and subtle errors

### Issue Key Format

```markdown
## Issue Key for [Dataset Name]

### Critical Issues (must catch)
1. [Location] Domain X: [Problem]. [Why it matters]
2. ...

### Major Issues (should catch most)
1. ...

### Minor Issues (good to catch)
1. ...

### Non-Issues (should NOT flag)
1. [Location]: This looks questionable but is actually fine because...
```

---

## Relationship to Theory-Forge

This assessment validates readiness to use theory-forge (or similar AI research tools) responsibly.

**The theory-forge note that prompted this assessment:**

> "Re-run eval-genre after substantive revisions. Gate D is not 'passed once, passed forever.' LLM-generated prose defaults to hypo-deductive framing—the genre eval catches this, but only if run on the actual revised text."

The capstone tests whether students have internalized the eval, not just the tool.

---

## Sample Feedback Report

After submission, students receive:

1. **Issue comparison**: Your list vs. expert baseline
   - What you caught that experts caught ✓
   - What you missed that experts caught ✗
   - What you flagged that wasn't an issue (false positive)

2. **Domain breakdown**: Performance by domain
   - "You caught 90% of Domain 5 issues but only 40% of Domain 3 issues"

3. **Pattern analysis**: What systematic errors did you make?
   - "You consistently missed mechanism problems—review Domain 3"

4. **Prioritization comparison**: Did your top 5 match expert top 5?

5. **Path forward**:
   - Pass → Certified for AI-assisted research workflow
   - Fail → Remediation in specific domains, retake in 30 days

---

## The Karate Kid Moment

You've learned to wax on, wax off. Paint the fence. Sand the floor.

Now: fight.

The AI draft is your opponent. It looks competent. It moves smoothly. But it has weaknesses everywhere—if you've truly learned the craft, you'll see them.

This isn't about rejecting AI. It's about being good enough to use it well.
