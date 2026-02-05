# Exercise 2: Heterogeneity Hunting

## Context

A pattern that varies by subgroup is often more interesting than a uniform effect. Heterogeneity can reveal mechanisms and boundary conditions.

## The Finding

The AI found that startup founders with MBA degrees raise 34% more funding than founders without MBAs (p < 0.001).

But wait—the AI also found significant heterogeneity:

| Subgroup | MBA Effect | 95% CI | p-value | N |
|----------|------------|--------|---------|---|
| Overall | +34% | [24%, 45%] | <0.001 | 4,521 |
| First-time founders | +52% | [38%, 68%] | <0.001 | 2,847 |
| Serial founders | +8% | [-5%, 22%] | 0.214 | 1,674 |
| Tech sector | +21% | [10%, 33%] | <0.001 | 2,103 |
| Non-tech sector | +49% | [34%, 66%] | <0.001 | 2,418 |
| Pre-seed/Seed stage | +41% | [28%, 55%] | <0.001 | 3,012 |
| Series A+ | +18% | [4%, 34%] | 0.012 | 1,509 |
| Founded 2015-2019 | +38% | [25%, 52%] | <0.001 | 2,156 |
| Founded 2020-2023 | +28% | [14%, 44%] | <0.001 | 2,365 |

## Your Task

### Part 1: Pattern Detection

Which heterogeneity patterns do you see? Identify at least 3 distinct patterns.

**Your answer:**

<!-- Describe the patterns you observe -->

### Part 2: Mechanism Hypotheses

For each pattern you identified, propose a mechanism that could explain it.

| Pattern | Proposed Mechanism |
|---------|-------------------|
| 1. | |
| 2. | |
| 3. | |

### Part 3: Which Heterogeneity Matters Most?

If you could only pursue ONE of these heterogeneity findings for a paper, which would you choose and why?

Consider:
- Theoretical novelty (does this violate or extend existing theory?)
- Practical importance (who cares about this distinction?)
- Robustness (is the subsample big enough to trust?)

**Your answer:**

<!-- Make your case for one heterogeneity finding -->

### Part 4: Mechanism Test

Design a specific test that could distinguish between two competing mechanisms for the first-time vs. serial founder heterogeneity:

**Mechanism A:** MBAs provide legitimacy signals that first-timers lack but serial founders already have

**Mechanism B:** MBA networks are more valuable for first-timers who don't have existing investor relationships

What data or analysis would distinguish these?

**Your answer:**

<!-- Design a test that could distinguish the mechanisms -->

---

## Completion Checklist

- [ ] Identified 3+ heterogeneity patterns
- [ ] Proposed mechanisms for each pattern
- [ ] Made a case for which heterogeneity to pursue
- [ ] Designed a mechanism-distinguishing test
