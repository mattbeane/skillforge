# Domain 1: Pattern Recognition & Data Sense

## What This Domain Tests

The ability to look at data and see what's worth pursuing. Not just finding patterns—finding patterns that matter.

**Source in TheoryForge**: `/explore-data`, `/hunt-patterns`

## Why It Matters

Novice researchers make two opposite mistakes:
1. **Seeing everything**: Every correlation is exciting, nothing gets killed
2. **Seeing nothing**: Miss the anomaly that would become the paper

Expert researchers have calibrated intuition: they recognize when something in the data signals theoretical interest, and they know when to let go of a finding that doesn't survive scrutiny.

## Core Competencies

### 1.1 Anomaly Recognition
Seeing patterns that deviate from expectation—not just statistical significance, but theoretical surprise.

**What it looks like**:
- "This effect goes the opposite direction of what [Theory X] predicts"
- "These two groups should behave similarly but they don't"
- "There's a bimodal distribution where we expected normal"

**Common failures**:
- Treating all significant coefficients as interesting
- Missing non-obvious patterns (interactions, non-linearities)
- Confusing statistical outliers with theoretically meaningful anomalies

### 1.2 Robustness Instinct
Knowing when a pattern is fragile vs solid—before running every possible robustness check.

**What it looks like**:
- "This finding probably won't survive controlling for [X]"
- "Let me check if this holds in the subgroups where it should be strongest"
- "The effect size is too small to matter even if significant"

**Common failures**:
- Publishing findings that die with first obvious control
- Not checking heterogeneity (effect works for some, not others)
- Conflating statistical significance with substantive importance

### 1.3 Theoretical Interest Assessment
Distinguishing patterns that could become papers from patterns that are merely true.

**What it looks like**:
- "This violates what [Literature X] would predict—that's the story"
- "This is just a replication of a known effect—not a paper"
- "The heterogeneity here is where the contribution lives"

**Common failures**:
- "I found a significant effect" = paper-worthy (no, it isn't)
- Pursuing descriptive findings without theoretical hook
- Missing the more interesting pattern hiding in a subgroup

### 1.4 Finding Discipline
Knowing when to kill a finding and move on.

**What it looks like**:
- "This looked promising but doesn't survive controls—documenting and moving on"
- "I've tested 5 variations; this pattern isn't robust"
- "My initial hypothesis was wrong; the data says something else"

**Common failures**:
- p-hacking to save a pet hypothesis
- Running 20 specifications to find one that works
- Emotional attachment to findings that should die

---

## Assessment Specifications

### Level 1: Knowledge Recognition

**Format**: Multiple choice + short answer

**Sample questions**:

1. A researcher finds that job satisfaction predicts turnover (β = -0.15, p < 0.01). What question should they ask first?
   - a) Is this publishable?
   - b) Does this survive controlling for obvious confounds?
   - c) How can I frame this for ASQ?
   - d) What theory does this support?

   **Correct**: b. Robustness first, framing later.

2. You observe that automation adoption varies significantly across facilities (F = 4.2, p < 0.01). Which next step shows good pattern recognition instinct?
   - a) Write up the finding as evidence of organizational heterogeneity
   - b) Look for what differs between high and low adoption facilities
   - c) Run 10 more regressions with different control variables
   - d) Search the literature for theories that predict this

   **Correct**: b. Explore the heterogeneity—the explanation IS the paper.

3. Your initial hypothesis was that tenure increases productivity. The data shows tenure decreases productivity for workers in one department but increases it in another. What do you do?
   - a) Report the overall null effect
   - b) Report only the positive effect (in the department where hypothesis worked)
   - c) Investigate why the effect reverses—this heterogeneity might be the real story
   - d) Conclude that tenure doesn't matter

   **Correct**: c. The heterogeneity is often where the paper lives.

**Passing threshold**: ≥80% (8/10 questions)

---

### Level 2: Application with Feedback

**Format**: Given a dataset, identify patterns worth pursuing

**Materials provided**:
- Anonymized dataset (Company X temp worker data, heavily modified)
- Data dictionary
- Research context (what the organization does, what we're trying to understand)

**Task**:
1. Explore the data (descriptives, distributions, correlations)
2. Identify your top 3 patterns worth investigating
3. For each pattern, explain:
   - What makes this theoretically interesting (not just statistically significant)
   - What could kill this finding (obvious confounds)
   - What heterogeneity might exist (who does this apply to?)
4. Identify one pattern you explored but decided to kill, and explain why

**Evaluation rubric**:

| Criterion | Expert behavior | Points |
|-----------|-----------------|--------|
| Found ≥2 of expert-identified top patterns | Sees what experts see | 20 |
| Articulated theoretical interest (not just significance) | Understands contribution | 20 |
| Identified appropriate confounds to check | Robustness instinct | 20 |
| Explored heterogeneity | Looks beyond average effects | 20 |
| Documented and killed weak patterns | Research discipline | 20 |

**Passing threshold**: ≥70 points

**Feedback provided**:
- Comparison to expert pattern identification
- What patterns the expert found that student missed
- What patterns the student pursued that experts would have killed early
- Explanation of expert reasoning

---

### Level 3: Authentic Performance

**Format**: Independent pattern hunting on unfamiliar dataset

**Materials provided**:
- Novel anonymized dataset (not used in Level 2)
- Data dictionary
- Research context

**Task**:
Same as Level 2, but:
- No feedback during assessment
- Work evaluated against expert baseline
- Single attempt per assessment period (30-day cooldown)

**Evaluation criteria**:

1. **Pattern Quality** (40 points)
   - Did they find patterns experts found? (comparison)
   - Are their patterns theoretically interesting? (expert judgment)
   - Did they miss obvious patterns? (error tracking)

2. **Robustness Instinct** (30 points)
   - Did they identify the right confounds?
   - Did they check heterogeneity appropriately?
   - Did they avoid chasing fragile findings?

3. **Research Discipline** (30 points)
   - Did they document killed findings?
   - Did they avoid p-hacking behaviors?
   - Did they stay focused on promising patterns?

**Passing threshold**: ≥70 points total; minimum 20 points on Pattern Quality

**Advisor override**: Advisor can certify Level 3 pass if they review the work and judge competence demonstrated.

---

## What This Unlocks

| Level Achieved | TheoryForge Commands Unlocked |
|----------------|------------------------------|
| Level 2 | `/hunt-patterns` (guided mode - shows AI reasoning) |
| Level 3 | `/hunt-patterns` (full mode) |

---

## Common Misconceptions

**"Statistical significance = interesting"**
No. Interesting means it violates or extends theoretical expectation. Many significant effects are boring.

**"More robustness checks = better"**
Only if you're checking meaningful alternatives. Running 50 random specifications is noise, not rigor.

**"My hypothesis was right" = success**
Your hypothesis being wrong is often more interesting. The heterogeneity and surprises are where papers live.

**"I should report all my findings"**
You should report findings that survived scrutiny and matter theoretically. Documenting killed findings is for your records, not the paper.

---

## Readings & Resources

### Required
- Zuckerman, "Tips for Article-Writers" (2008) — Section 7: Building up the null
- TheoryForge `/hunt-patterns.md` — Read the full command spec

### Recommended
- Simmons, Nelson, & Simonsohn (2011), "False-Positive Psychology"
- Gelman & Loken (2013), "The garden of forking paths"
- Any paper that went through 3+ framings before publication (ask your advisor)

---

## Self-Assessment Questions

Before taking the Level 3 assessment, you should be able to answer:

1. Given a dataset, what's your process for deciding what patterns to pursue?
2. How do you distinguish "statistically significant" from "theoretically interesting"?
3. What's your threshold for killing a finding?
4. When you find an effect that varies by subgroup, what do you do?
5. How do you avoid confirmation bias when testing your hypotheses?

If you can't articulate clear answers to these, you're not ready.
