# Domain 1: Quick Start & Diagnostic

**Time to value: 30 minutes**

After this, you'll read research papers differently. That's not hype—pattern recognition is the foundation skill that separates "I ran some regressions" from "I found something worth publishing."

## Before You Start: 5-Minute Diagnostic

Can you already do this? Take this diagnostic to find out. If you pass, you can fast-track to Level 2.

### The Diagnostic

Answer these 5 questions. You need 5/5 to fast-track.

**Q1.** A researcher finds that job satisfaction predicts turnover (β = -0.15, p < 0.01) in their data. What's their first question before writing anything?

- a) "How do I frame this for ASQ?"
- b) "Does this survive controlling for obvious confounds (pay, tenure, manager quality)?"
- c) "What theory does this support?"
- d) "Is this effect size large enough to matter?"

**Q2.** You're exploring a dataset and notice that experienced workers adopt new technology at *lower* rates than new workers. Your gut says experienced workers should adopt faster because they're competent. What do you do?

- a) Assume the data is wrong and check for coding errors
- b) Run more models to see if experience ever has a positive effect
- c) Treat this as a potential puzzle worth investigating—why might experience DECREASE adoption?
- d) Report it as a null finding (experience doesn't help with adoption)

**Q3.** You find a significant effect (p < 0.001) but the effect size is tiny (R² = 0.02). What does expert instinct tell you?

- a) Publishable! Statistical significance is what matters
- b) Needs more data to see if effect gets stronger
- c) Substantively meaningless—2% variance explained isn't enough to build a paper around
- d) Run more robustness checks to see if significance holds

**Q4.** Your hypothesis was that remote work increases productivity. Your data shows it increases productivity for some workers but decreases it for others (interaction effect). What's the expert move?

- a) Report the null overall effect and move on
- b) Report only the positive effect (ignore the negative subgroup)
- c) Investigate the heterogeneity—THAT'S the paper
- d) Conclude the relationship is "complex" and needs more study

**Q5.** You've spent 40 hours exploring a pattern that looked promising initially. You've now run 12 different specifications and only 2 show significant effects. What do you do?

- a) Report the 2 significant specifications and mention robustness in a footnote
- b) Keep running specifications until you get a consistent result
- c) Document the finding as fragile, kill it, and move to something else
- d) Combine the 12 specifications in a meta-analysis

---

### Answer Key

| Q | Answer | Why |
|---|--------|-----|
| 1 | b | Robustness first, always. No point framing a finding that dies with basic controls |
| 2 | c | Anomalies that violate expectation are often where papers live. Don't explain away—investigate |
| 3 | c | Significance ≠ importance. Effect size matters |
| 4 | c | Heterogeneity is usually more interesting than main effects |
| 5 | c | Research discipline. 2/12 significant = probably noise. Document and move on |

**Score:**
- 5/5: Fast-track to Level 2. You already have the instincts.
- 4/5: Review the one you missed, then proceed to Level 1 (abbreviated).
- 3 or below: Do the full Level 1. You're learning foundational skills.

---

## Level 1 (Streamlined): The Pattern Recognition Mindset

**Time: 1-2 hours**

This streamlined version covers the essentials. If you got 4/5 on the diagnostic, focus on the section corresponding to your missed question.

### Core Concept 1: Significance vs. Theoretical Interest

Most research training teaches you to find statistically significant results. This is necessary but not sufficient. A "p < 0.05" result is not a paper unless it:

1. **Violates or extends theory** — Someone smart believed the opposite, or believed the effect would be smaller/larger/different
2. **Is substantively meaningful** — The effect size matters in the real world, not just statistically
3. **Survives scrutiny** — Won't die with obvious controls or alternative specifications

**The mistake**: Treating your regression output as a finding rather than a starting point.

**The fix**: For every significant result, ask: "Who would be surprised by this, and why?"

### Core Concept 2: Anomaly as Opportunity

When data violates your expectation, don't explain it away—investigate it.

**Examples of productive anomalies:**
- Effect goes opposite direction from theory
- Effect exists in one subgroup but not another
- Two things that should correlate don't
- Distribution is bimodal when you expected normal

**The mistake**: Treating surprises as problems rather than potential papers.

**The fix**: When you see something unexpected, write it down. Ask: "Under what conditions would this make sense?"

### Core Concept 3: Heterogeneity Is Your Friend

"On average, X leads to Y" is rarely a paper. "X leads to Y when Z, but not otherwise" is often a paper.

**Why heterogeneity matters:**
- Main effects wash out real dynamics
- The "when" and "for whom" reveals mechanism
- Boundary conditions are theoretically interesting

**The mistake**: Reporting average effects and treating subgroup variation as noise.

**The fix**: Always check interactions. Split your sample. The effect that works for some but not others is usually more interesting.

### Core Concept 4: Kill Your Findings

Researchers who publish well kill more findings than they keep. This is discipline, not failure.

**Signs a finding should die:**
- Dies with first obvious control
- Only appears in 2 of 10 specifications
- Effect size is trivially small
- You can't articulate why it's theoretically interesting

**The mistake**: Emotional attachment to findings. "I've invested too much to kill it."

**The fix**: Keep a "killed findings" log. Document what you tried and why you moved on. This protects against p-hacking and helps you learn from dead ends.

---

## Quick Practice: Real Scenario

Read this scenario and answer the question.

> A PhD student is studying how AI coding tools affect programmer productivity. She finds that AI tool use is positively correlated with lines of code written (β = 0.23, p < 0.01). She also notices that senior programmers use AI tools *less* than junior programmers, even though the productivity benefit appears similar across experience levels.

**What should she investigate next?**

a) Why the positive effect is "only" β = 0.23
b) Whether the effect survives controlling for programmer ability
c) Why senior programmers use AI less despite similar productivity benefits—what explains the adoption gap?
d) Whether the finding generalizes to other coding tools

---

**Answer: c**

The anomaly (seniors use AI less despite similar benefits) is where the paper likely lives. The productivity finding is probably well-established; the adoption puzzle is fresh.

---

## What You Can Do Now

After completing Level 1, you have the conceptual vocabulary to:

1. **Read papers critically** — When you see a finding, ask: Is this robust? Is this theoretically interesting? Is the effect size meaningful?

2. **Evaluate your own early exploration** — Before getting attached to a pattern, run it through the checklist: significance, effect size, robustness, theoretical interest.

3. **Identify productive anomalies** — When data surprises you, recognize that as opportunity rather than problem.

4. **Practice research discipline** — Document killed findings. Move on from fragile patterns without guilt.

## Next: Level 2

Level 2 gives you hands-on practice with real data. You'll:
- Explore an actual dataset
- Identify patterns worth pursuing
- Get detailed comparison to expert analysis
- Learn from the gaps between your instincts and expert instincts

Run: `skill-forge take domain-1 --level 2`

---

## Quick Reference: The Pattern Recognition Checklist

Before pursuing any finding:

- [ ] **Robust?** — Does it survive obvious controls?
- [ ] **Meaningful?** — Is the effect size substantively important?
- [ ] **Surprising?** — Does it violate or extend theoretical expectation?
- [ ] **Heterogeneous?** — Does it vary by subgroup in interesting ways?
- [ ] **Articulate?** — Can you say why a smart person should care?

If you can't check all boxes, the finding probably isn't a paper.

---

*Domain 1 complete. You're now equipped to recognize patterns worth pursuing—and kill the ones that aren't.*
