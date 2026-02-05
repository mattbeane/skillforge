# Exercise 2: Reading Robustness Tables

## Context

A research AI has run robustness checks on a finding about mentorship and career advancement. Your job is to interpret the results.

## The Finding

Original claim: "Having a senior mentor increases promotion likelihood by 23%"

## Robustness Check Results

| Specification | Effect (OR) | 95% CI | p-value | Notes |
|--------------|-------------|--------|---------|-------|
| Base model | 1.23 | [1.08, 1.41] | 0.002 | No controls |
| + Demographics | 1.19 | [1.03, 1.37] | 0.018 | Age, gender, education |
| + Tenure | 1.14 | [0.98, 1.33] | 0.089 | Years at company |
| + Department FE | 1.21 | [1.04, 1.41] | 0.014 | Department fixed effects |
| + Performance rating | 1.08 | [0.91, 1.28] | 0.367 | Prior year rating |
| High performers only | 1.31 | [1.09, 1.57] | 0.004 | Top 25% performers |
| Low performers only | 0.97 | [0.78, 1.21] | 0.793 | Bottom 25% performers |

## Your Task

### Question 1: Pattern Stability

Looking at specifications 1-5, how stable is this finding? Use specific numbers from the table to support your assessment.

**Your answer:**

<!-- Write your answer here -->

### Question 2: The Performance Control

What happened when "Performance rating" was added as a control (row 5)? What does this suggest about the mechanism?

**Your answer:**

<!-- Write your answer here -->

### Question 3: Heterogeneity

Compare rows 6 and 7. What does this heterogeneity tell you? Is this good or bad for the paper?

**Your answer:**

<!-- Write your answer here -->

### Question 4: Bottom Line

If you had to advise a researcher: pursue this finding or kill it? What's your specific recommendation and why?

**Your answer:**

<!-- Write your answer here -->

---

## Completion Checklist

- [ ] Referenced specific numbers from the table
- [ ] Identified what the performance control reveals
- [ ] Interpreted the heterogeneity finding
- [ ] Made a clear pursue/kill recommendation with reasoning
