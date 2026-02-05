# Exercise 1: Run Your Own Robustness Checks

## Context

You have access to a dataset and an AI research assistant. The AI has found an initial pattern. Your job is to design and interpret robustness checks.

## The Finding

The AI reports:
> "In our hospital dataset, I found that nurses who received AI-assisted scheduling had 18% fewer medication errors (p = 0.008, OR = 0.82). This suggests AI scheduling tools improve patient safety."

**Dataset details:**
- 12 hospitals, 3 years of data (2021-2023)
- AI scheduling rolled out to 6 hospitals in mid-2022
- N = 2,847 nurses, 142,000 medication administration events
- Medication errors = any deviation from prescribed protocol

## Your Task

### Part 1: Design Robustness Checks

List 5 specific robustness checks you would run. For each:
- What variable(s) are you adding or how are you subsetting?
- What would it mean if the effect survives this check?
- What would it mean if the effect disappears?

**Your robustness check design:**

| # | Check Description | If Survives | If Disappears |
|---|-------------------|-------------|---------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

### Part 2: Interpret These Results

The AI ran your checks (simulated). Here are the results:

| Specification | OR | 95% CI | p-value |
|--------------|-----|--------|---------|
| Base model | 0.82 | [0.71, 0.95] | 0.008 |
| + Nurse experience (years) | 0.84 | [0.72, 0.97] | 0.021 |
| + Hospital fixed effects | 0.79 | [0.67, 0.93] | 0.004 |
| + Patient acuity controls | 0.85 | [0.73, 0.99] | 0.041 |
| + Time trend (month FE) | 0.91 | [0.77, 1.08] | 0.274 |
| Pre-2022 hospitals only | 0.88 | [0.71, 1.09] | 0.238 |
| Post-rollout period only | 0.76 | [0.62, 0.93] | 0.007 |

**Interpretation questions:**

1. Which check is most concerning and why?

**Your answer:**

<!-- Write your answer here -->

2. What does the time trend control (row 5) suggest about the mechanism?

**Your answer:**

<!-- Write your answer here -->

3. How do you reconcile rows 6 and 7?

**Your answer:**

<!-- Write your answer here -->

4. What's your overall assessment: pursue or kill? What additional analysis would change your mind?

**Your answer:**

<!-- Write your answer here -->

---

## Completion Checklist

- [ ] Designed 5 robustness checks with clear rationale
- [ ] Interpreted the most concerning result
- [ ] Explained what time trend control reveals
- [ ] Made a pursue/kill recommendation with conditions
