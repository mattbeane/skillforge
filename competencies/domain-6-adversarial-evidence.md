# Domain 6: Adversarial Evidence Handling

## What This Domain Tests

The ability to search ALL data for evidence that challenges your claims—not just evidence that supports them.

**Source in TheoryForge**: `/audit-claims`, `/verify-claims`

## Why It Matters

Cherry-picking is the silent killer of research integrity. It doesn't require malice—just motivated reasoning. Researchers naturally gravitate toward evidence that supports their claims and unconsciously filter out evidence that challenges them.

Expert researchers actively work against this tendency. They search for disconfirming evidence as deliberately as they search for supporting evidence. They document alternative interpretations. They're honest about boundary conditions.

This domain tests whether you can audit your own work—or AI-generated work—with intellectual honesty.

## Core Competencies

### 6.1 Comprehensive Data Search
Searching ALL data sources, not just the ones you cited.

**What it looks like**:
- "I searched all 47 interviews, not just the 12 I quoted"
- "I checked the quantitative data for patterns that contradict the qualitative story"
- "I examined cases from Site B even though my main findings are from Site A"

**Common failures**:
- Only reading interviews you expect to support your claims
- Stopping search when you have "enough" supporting evidence
- Ignoring data sources that might complicate the story

### 6.2 Disconfirming Evidence Documentation
Actively hunting for and recording evidence against your claims.

**What it looks like**:
- "3 of 47 informants describe the opposite experience—documented here"
- "The mechanism doesn't operate in [specific context]—that's a boundary condition"
- "This quote directly challenges my interpretation: [quote]"

**Common failures**:
- Zero disconfirming evidence reported (statistically impossible if searching honestly)
- Disconfirming evidence mentioned but explained away
- Treating exceptions as "noise" rather than information

### 6.3 Evidence Distribution Analysis
Understanding WHERE support and challenges come from.

**What it looks like**:
- "Supporting evidence comes primarily from managers; workers show mixed views"
- "Site A strongly supports the claim; Site B challenges it"
- "Early-phase informants support this; late-phase informants contradict"

**Why it matters**:
- If support comes only from one role/site/time, you may have selection bias
- If challenges come from specific contexts, that's a boundary condition to document
- Reviewers will notice patterns you didn't

**Common failures**:
- Not tracking evidence source demographics
- Assuming uniform support when it's actually concentrated
- Missing boundary conditions hiding in the distribution

### 6.4 Alternative Interpretation Identification
Recognizing that the same data could support different stories.

**What it looks like**:
- "The data is also consistent with [Alternative Interpretation]"
- "A critic might argue this pattern reflects [X] rather than [Y]"
- "We prefer our interpretation because [reason], but acknowledge [alternative]"

**Common failures**:
- Acting as if your interpretation is the only possible one
- Not considering what a hostile reviewer would argue
- Dismissing alternatives without engaging seriously

---

## Assessment Specifications

### Foundation (Level 1)

**Format**: Multiple choice + scenario analysis

**Sample questions**:

1. A researcher quotes 8 informants who support her mechanism claim. What should she report about the other 39 interviews?
   - a) Nothing—8 supporting quotes is sufficient
   - b) "The remaining interviews did not address this topic"
   - c) Whether any contradict the claim, with documentation if so
   - d) A count of interviews that partially support

   **Correct**: c. Silence about contradicting evidence is a form of cherry-picking.

2. You find that your proposed mechanism has strong support from managers (10/12 support) but weak support from workers (4/15 support). What do you do?
   - a) Report only the manager data since it's stronger
   - b) Report aggregate support (14/27 = 52%) without the breakdown
   - c) Report the role-based pattern and discuss what it means
   - d) Interview more workers until you get better numbers

   **Correct**: c. The distribution is informative—it might reveal a boundary condition.

3. Which audit behavior is most rigorous?
   - a) Searching for quotes that support each claim
   - b) Searching for evidence that would CHALLENGE each claim, then documenting what's found
   - c) Having a research assistant independently code the data
   - d) Running sentiment analysis on all interviews

   **Correct**: b. Adversarial search means actively looking for contradictions.

4. You discover that 2 informants describe an experience that directly contradicts your main claim. What's the most intellectually honest response?
   - a) Exclude them as outliers
   - b) Document them and investigate why they differ—they might reveal a boundary condition
   - c) Reframe the claim to exclude their context
   - d) Note them in a footnote

   **Correct**: b. Exceptions are data, not noise.

**Passing threshold**: ≥80%

---

### Practice (Level 2)

**Format**: Audit a provided analysis against raw data

**Materials provided**:
- A paper draft with 5-7 substantive claims
- The full dataset (qual + quant) from which claims were derived
- An evidence mapping showing which data supports each claim

**Task**:
1. For each claim, search the FULL dataset for:
   - Additional supporting evidence (not in the current mapping)
   - Disconfirming evidence (anything that challenges the claim)
   - Alternative interpretations the data could support
2. Analyze evidence distribution:
   - By informant role
   - By site
   - By time period (if applicable)
3. Flag claims with concerning evidence patterns:
   - Support concentrated in one source
   - Significant disconfirming evidence not acknowledged
   - Alternative interpretations not addressed
4. Write an audit summary with recommendations

**Evaluation rubric**:

| Criterion | Expert behavior | Points |
|-----------|-----------------|--------|
| Found ≥75% of disconfirming evidence in dataset | Thorough search | 30 |
| Correctly analyzed evidence distribution | Sees patterns | 20 |
| Identified legitimate alternative interpretations | Thinks like reviewer | 20 |
| Flagged appropriate claims as concerning | Good judgment | 15 |
| Recommendations are actionable | Practical | 15 |

**Passing threshold**: ≥70 points; must achieve ≥20 on disconfirming evidence

**Feedback provided**:
- Complete audit (comparison)
- Disconfirming evidence student missed
- Evidence distribution patterns student didn't see
- Alternative interpretations student didn't consider

---

### Mastery (Level 3)

**Format**: Full audit of unfamiliar analysis

**Materials provided**:
- New paper draft with claims
- New full dataset
- NO prior evidence mapping (student must search from scratch)

**Task**: Same as Level 2, but completely independent

**Evaluation criteria**:

1. **Search Comprehensiveness** (30 points)
   - Did they search ALL data sources?
   - Did they search specifically for contradictions (not just scan for support)?
   - Did they find evidence in sources the original analysis missed?

2. **Disconfirming Evidence Discovery** (30 points)
   - Found ≥70% of disconfirming evidence that exists
   - Documented it accurately (not dismissively)
   - Identified boundary conditions implied by contradictions

3. **Distribution Analysis** (20 points)
   - Analyzed by role, site, time (as appropriate)
   - Identified concerning concentration patterns
   - Drew appropriate conclusions from distribution

4. **Alternative Interpretations** (20 points)
   - Generated at least one plausible alternative for major claims
   - Alternatives are real threats (not straw men)
   - Explained how to address or acknowledge alternatives

**Passing threshold**: ≥70 points; must achieve ≥20 on Disconfirming Evidence Discovery

---

## What This Unlocks

| Level Achieved | TheoryForge Commands Unlocked |
|----------------|------------------------------|
| Level 3 | `/audit-claims`, `/verify-claims` |

**Prerequisite**: Must have passed Domain 5, Level 3

---

## The Audit Protocol (Reference)

From TheoryForge's `/audit-claims.md`:

### This Is NOT Transcription

You must search RAW DATA directly. Do NOT:
- Extract claims and find quotes already cited
- Reproduce the author's argument structure
- Assume claims are supported because they appear

You MUST:
- Read actual transcripts/data files
- For each claim, search ALL sources
- Actively look for DISCONFIRMING evidence
- Flag claims resting on thin evidence
- Identify alternative interpretations

### Disconfirmation Criteria

Before searching, define what would challenge each claim:
- "This claim would be challenged if informants describe [opposite experience]"
- "This claim would be weakened if the effect doesn't appear in [context]"
- "Alternative interpretation [X] would be supported if we see [evidence]"

### Evidence Distribution Tracking

| Source Category | Supporting | Challenging | Notes |
|-----------------|------------|-------------|-------|
| Managers | 10 | 2 | Strong support |
| Workers | 4 | 8 | Challenges concentrated |
| Site A | 12 | 1 | Very strong |
| Site B | 2 | 9 | Counter-evidence here |

---

## Common Misconceptions

**"I looked at all the data—I just didn't find contradictions"**
If you looked honestly, you'd find something. No claim is universally supported. Zero disconfirming evidence is a red flag.

**"Disconfirming evidence means my paper is weaker"**
Actually, documenting it makes your paper stronger. Reviewers trust researchers who acknowledge limitations.

**"The exceptions are just noise"**
Exceptions are data. They might reveal boundary conditions, moderators, or limitations of your mechanism.

**"Alternative interpretations are for Discussion section"**
They should inform your entire analysis. If an alternative is plausible, your evidence needs to address it.

**"My evidence supports my claim, so I'm done"**
Support is necessary but not sufficient. You also need to show you looked for challenges and didn't find MAJOR ones (or acknowledged those you did find).

---

## Readings & Resources

### Required
- TheoryForge `/audit-claims.md`, `/verify-claims.md` — Full specs
- TheoryForge `ADVERSARIAL_EVIDENCE.md` — Philosophy document
- One paper that exemplifies honest disconfirming evidence handling

### Recommended
- Popper (1959), "The Logic of Scientific Discovery" (on falsification)
- Greenwald (1975), "Consequences of Prejudice Against the Null Hypothesis"
- Kerr (1998), "HARKing: Hypothesizing After Results are Known"

---

## Self-Assessment Questions

Before taking the Level 3 assessment, you should be able to answer:

1. How do you actively search for disconfirming evidence (not just fail to find it)?
2. What would you do if you found evidence that contradicts your main claim?
3. How do you track evidence distribution across informant types?
4. What alternative interpretations could a hostile reviewer propose for your findings?
5. How do you know if your evidence base is concentrated vs. broad?

If you've never found significant disconfirming evidence in your own work, you haven't been looking hard enough.
