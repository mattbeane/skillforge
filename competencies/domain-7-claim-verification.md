# Domain 7: Claim Verification & Integrity

## What This Domain Tests

The ability to match claim strength to evidence strength—and the integrity to do so honestly under publication pressure.

**Source in TheoryForge**: `/verify-claims`, `/package-verification`

## Why It Matters

This is the final gate before publication. After all the analysis, framing, and writing, the question is: Do your claims actually match your evidence?

Overclaiming is the most common failure at this stage. Researchers have invested months of work and naturally want to make the strongest possible claims. But reviewers (and the scientific record) need claims calibrated to evidence.

This domain tests whether you can be your own toughest critic—and whether you can create verification packages that allow others to check your work.

## Core Competencies

### 7.1 Claim-Evidence Calibration
Matching the strength of claims to the strength of evidence.

**What it looks like**:
- "The evidence strongly supports X" → claim X confidently
- "The evidence suggests Y" → claim Y tentatively
- "The evidence is consistent with Z but doesn't prove it" → claim Z as possible, not established

**Claim strength ladder**:
- **Proved/Established**: Overwhelming evidence, no plausible alternatives
- **Strongly supported**: Multiple lines of evidence, alternatives addressed
- **Supported**: Clear evidence, some limitations acknowledged
- **Suggested**: Evidence consistent with claim but other interpretations possible
- **Possible**: Speculation based on patterns, requires future research

**Common failures**:
- "Suggested" evidence leading to "established" claims
- Using causal language ("causes," "leads to") when only showing correlation
- Not distinguishing "revealed preferences" from "stated preferences"

### 7.2 Overclaim Detection
Recognizing when claims exceed what the data support.

**Types of overclaims**:
- **Causal overclaims**: Claiming causation from correlational data
- **Scope overclaims**: Generalizing beyond your sample
- **Mechanism overclaims**: Claiming mechanism when only showing pattern
- **Counterfactual overclaims**: Claiming what would have happened without your IV
- **Measurement overclaims**: Claiming access to constructs you only proxied

**Red flag phrases**:
- "This proves that..." (almost never appropriate)
- "Workers want..." (you measured behavior, not preferences)
- "This causes..." (did you rule out reverse causality?)
- "This will..." (prediction beyond your data)

**Common failures**:
- Not recognizing own overclaims
- Defending overclaims as "standard in the field"
- Weakening claims only when reviewers force you to

### 7.3 Verification Package Creation
Creating self-contained materials that let others check your work.

**A verification package contains**:
- Each substantive claim explicitly stated
- Evidence supporting each claim (with links to raw data)
- Evidence challenging each claim (with links)
- Alternative interpretations considered
- Specification choices that could be questioned
- Data limitations acknowledged

**Why it matters**:
- Papers shouldn't be verified by the same system that built them
- Colleagues, reviewers, or different AI should be able to check
- Forces you to document everything that could be questioned

**Common failures**:
- Package not self-contained (requires context only you have)
- Missing claims (not all substantive claims documented)
- Missing challenging evidence (only supporting evidence included)
- Assumes reader trust (doesn't document questionable choices)

### 7.4 Research Integrity Under Pressure
Maintaining honest calibration when you want the paper to succeed.

**What it looks like**:
- Acknowledging limitations even when they make the paper weaker
- Revising claims when evidence doesn't support them
- Being transparent about researcher degrees of freedom
- Not hiding negative results or failed analyses

**Pressure points where integrity is tested**:
- Reviewer asks for stronger claims
- Co-author wants to oversell
- Time pressure to submit
- Sunk cost of work already done
- Career pressure to publish

**Common failures**:
- Gradually inflating claims through revisions
- Removing caveats that reviewers didn't notice
- HARKing (Hypothesizing After Results Known)
- Selective reporting of analyses

---

## Assessment Specifications

### Foundation (Level 1)

**Format**: Claim evaluation + calibration exercises

**Sample questions**:

1. Match the claim to the appropriate evidence strength:

   | Claim | Evidence Level | Appropriate? |
   |-------|----------------|--------------|
   | "Automation causes skill degradation" | Cross-sectional correlation | No - overclaim |
   | "Workers with more automation exposure show lower skill levels" | Cross-sectional correlation | Yes - descriptive |
   | "The pattern is consistent with skill degradation" | Cross-sectional correlation | Yes - appropriately hedged |

2. Identify the overclaim in this passage:

   > "Workers in automated facilities prefer routine work. Our survey shows 73% of workers in automated facilities report high satisfaction with repetitive tasks, compared to 45% in traditional facilities."

   **Overclaim**: "Workers prefer" — the survey measured satisfaction (revealed preference), not preference. "Reported higher satisfaction" is supportable; "prefer" is not.

3. Which is NOT required in a verification package?
   - a) Evidence supporting each claim
   - b) Evidence challenging each claim
   - c) Your response to anticipated reviewer comments
   - d) Specification choices that could be questioned

   **Correct**: c. Verification is about checking claims against evidence, not anticipating reviews.

4. A reviewer asks you to strengthen a claim that your evidence only weakly supports. What should you do?
   - a) Strengthen the claim as requested (they're the expert)
   - b) Decline and explain why the evidence doesn't support a stronger claim
   - c) Find additional evidence to support the stronger claim
   - d) Compromise with slightly stronger language

   **Correct**: b. Claim strength should match evidence strength, not reviewer preferences.

**Passing threshold**: ≥80%

---

### Practice (Level 2)

**Format**: Audit a paper for overclaims and create verification package

**Materials provided**:
- A paper draft with claims
- The evidence base (data, quotes, statistics)
- Analysis code and outputs

**Task**:
1. Extract all substantive claims from the paper
2. For each claim, assess:
   - Evidence strength (proved/supported/suggested/possible)
   - Claim strength as written
   - Match? (Yes/Overclaim/Underclaim)
3. Identify specific overclaims with:
   - The problematic text
   - Why it's an overclaim
   - Suggested revision
4. Create a verification package:
   - Claims registry (all claims listed)
   - Evidence links (supporting and challenging)
   - Alternative interpretations
   - Specification choices
   - Limitations

**Evaluation rubric**:

| Criterion | Expert behavior | Points |
|-----------|-----------------|--------|
| Found ≥80% of overclaims in document | Sees problems | 25 |
| Correctly assessed claim-evidence match | Calibration skill | 20 |
| Revisions appropriately calibrated | Can fix problems | 20 |
| Verification package is complete | Thoroughness | 20 |
| Package is self-contained (could be used by outsider) | Independence | 15 |

**Passing threshold**: ≥70 points

**Feedback provided**:
- Complete overclaim list (comparison)
- Expert claim-evidence assessments (comparison)
- Model verification package
- Analysis of student's calibration patterns (systematic over/under?)

---

### Mastery (Level 3)

**Format**: Full verification of unfamiliar paper

**Materials provided**:
- New paper draft
- New evidence base
- No hints about where overclaims are

**Task**: Same as Level 2

**Evaluation criteria**:

1. **Overclaim Detection** (30 points)
   - Found ≥75% of overclaims
   - No false positives (didn't "find" problems that aren't there)
   - Correctly categorized types of overclaims

2. **Claim-Evidence Calibration** (30 points)
   - Assessments match expert judgment
   - Revisions are appropriately calibrated (not over-corrected)
   - Distinguishes types of evidence appropriately

3. **Verification Package Quality** (25 points)
   - All claims included
   - Evidence links are accurate
   - Challenging evidence is represented
   - Package could be used by independent verifier

4. **Judgment Quality** (15 points)
   - Recommendations are actionable
   - Priorities are correct (major overclaims flagged as more important)
   - Doesn't demand impossible precision

**Passing threshold**: ≥70 points; must achieve ≥20 on Overclaim Detection

---

## What This Unlocks

| Level Achieved | TheoryForge Commands Unlocked |
|----------------|------------------------------|
| Level 3 | `/package-verification` (submission-ready) |

**Prerequisite**: Must have passed Domain 6, Level 3

**This is the final gate**. Passing Domain 7 means you have demonstrated all competencies required for full TheoryForge access.

---

## The Verification Protocol (Reference)

From TheoryForge's `/verify-claims.md`:

### Claim Registry Structure

```markdown
### CLM-001: [Short description]

**Claim text**: "[Exact claim as written in paper]"

**Claim type**: mechanism / boundary_condition / descriptive / causal

**Evidence strength**: proved / strongly_supported / supported / suggested / possible

**Supporting evidence**:
- EVD-001: [Description] (weight: 0.8)
- EVD-002: [Description] (weight: 0.6)

**Challenging evidence**:
- EVD-003: [Description] (weight: 0.4)

**Alternative interpretations**:
- The pattern could also be explained by [X]
- A critic might argue [Y]

**Calibration assessment**: MATCHED / OVERCLAIM / UNDERCLAIM

**If overclaim, suggested revision**:
- Current: "[problematic text]"
- Revised: "[calibrated text]"
```

### Verification Questions

For each claim, ask:
1. What's the evidence type? (Correlation, mechanism, boundary condition)
2. What's the evidence strength? (How many lines? How robust?)
3. Does the language match? (Causal language for correlational evidence?)
4. What would challenge this claim? (Is that evidence documented?)
5. What alternative interpretations exist? (Are they acknowledged?)

---

## Common Misconceptions

**"Strong findings deserve strong claims"**
Claims should match evidence type, not finding strength. A "strong" correlation still doesn't prove causation.

**"Reviewers will catch overclaims anyway"**
Some will. But catching your own is a sign of research maturity—and saves revision cycles.

**"Everyone in my field writes this way"**
Field norms aren't justification. If the norm is to overclaim, don't perpetuate it.

**"Hedging makes papers boring"**
Precision isn't hedging. "We show that X is consistent with Y" is more precise than "X causes Y"—and more defensible.

**"The paper is verified because I ran the analyses"**
Running analyses isn't verification. Verification is documenting claims against evidence so others can check.

---

## Readings & Resources

### Required
- TheoryForge `/verify-claims.md`, `/package-verification.md` — Full specs
- Simmons, Nelson, & Simonsohn (2011), "False-Positive Psychology"
- One exemplary paper from your field that handles limitations well

### Recommended
- Bem (2004), "Writing the Empirical Journal Article" — section on claiming
- Your target journal's "best practices" or ethics guidelines
- Retracted papers in your field (study what went wrong)

---

## Self-Assessment Questions

Before taking the Level 3 assessment, you should be able to:

1. Read a claim and immediately assess what evidence type would support it
2. Identify at least one overclaim in most papers you read
3. Create a verification package for your own work without missing major claims
4. Resist the urge to oversell when you've invested heavily in a finding
5. Explain the difference between "causes," "is associated with," and "is consistent with"

This domain is about integrity as much as skill. You can have the skill but lack the will to apply it under pressure. Both are required.

---

## Graduation

Passing Domain 7, Level 3 means you have demonstrated competence across all seven domains:

1. Pattern Recognition & Data Sense
2. Theoretical Positioning
3. Qualitative Mechanism Extraction
4. Theoretical Framing
5. Epistemological Genre
6. Adversarial Evidence Handling
7. Claim Verification & Integrity

You now have full access to TheoryForge. Use it wisely.

Remember: The tool amplifies. If you've developed these competencies, it amplifies good research. If you haven't, it amplifies bad research that looks good. The competencies are the point.
