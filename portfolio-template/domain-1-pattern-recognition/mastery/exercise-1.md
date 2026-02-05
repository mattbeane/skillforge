# Mastery Exercise: The Full Pattern Hunt

## Context

You're the lead researcher. An AI assistant has done initial exploration of a dataset. Now you must make strategic decisions about what to pursue.

## The Dataset

**Source:** Administrative data from a large university system (8 campuses)
**Period:** 2018-2024
**Units:** 12,000 faculty members, 180,000 course sections

**Available variables:**
- Faculty: rank, tenure status, gender, race, department, hire year, PhD institution
- Courses: enrollment, student ratings, grade distributions, time slot, modality (in-person/hybrid/online)
- Research: publications, citations, grants, co-authorship networks
- Service: committee assignments, advising load, administrative roles

## The AI's Initial Findings

The AI ran exploratory analyses and reports:

> **Finding 1:** Female faculty receive student ratings 0.3 points lower than male faculty (p < 0.001), but this gap disappears when controlling for course difficulty and field.
>
> **Finding 2:** Faculty hired during COVID (2020-2021) have 40% fewer publications than cohorts hired 2018-2019, even controlling for career stage.
>
> **Finding 3:** Courses taught in the 8am slot have 0.4 higher average grades than afternoon sections of the same course by the same instructor.
>
> **Finding 4:** Faculty with more co-authors have higher citation counts, but the relationship is non-linear—it flattens after ~5 regular co-authors.
>
> **Finding 5:** Online courses have bimodal grade distributions (many As, many Fs) compared to unimodal in-person distributions.

## Your Task

### Part 1: Triage

Rank these 5 findings by their potential for a publishable paper. For each, give:
- Rank (1-5, where 1 = most promising)
- One-sentence rationale
- Key threat to validity

| Finding | Rank | Rationale | Key Threat |
|---------|:----:|-----------|------------|
| 1. Gender ratings gap | | | |
| 2. COVID cohort publications | | | |
| 3. 8am grade inflation | | | |
| 4. Co-authorship diminishing returns | | | |
| 5. Online bimodal grades | | | |

### Part 2: Deep Dive

Choose your #1 ranked finding. Design a complete pattern-hunting strategy:

**The finding I'm pursuing:**

**Robustness checks I would run (list 5-7):**

1.
2.
3.
4.
5.

**Heterogeneity I would explore:**

- By what subgroups?
- What would each pattern tell us?

**Kill conditions (what results would make me abandon this):**

1.
2.
3.

**What theory might this violate or extend?**

### Part 3: The Hard Call

Your AI assistant runs additional analysis and reports:

> "The [your chosen finding] is robust to 4 of 5 checks, but when I control for [plausible confounder], the effect drops by 60% and becomes marginally significant (p = 0.07)."

Write a 200-word memo to your co-author arguing either:
- A) Why you should pursue this finding despite the concerning control, OR
- B) Why you should kill it and pivot to your #2 ranked finding

**Your memo:**

<!-- Write your 200-word memo here -->

---

## Completion Checklist

- [ ] Ranked all 5 findings with clear rationale
- [ ] Designed complete strategy for top finding
- [ ] Specified kill conditions
- [ ] Wrote substantive memo defending a hard call
