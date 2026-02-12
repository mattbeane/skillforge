# Potential Tool Integration Notes

> **Status: Speculative / Work-in-Progress**
>
> This document captures early thinking about how research competency development and AI-assisted research tooling (like TheoryForge) might relate to each other. Nothing here is implemented, tested, or validated. These are hypotheses about potential links, preserved for future exploration.

---

## The Relationship (As We Currently Understand It)

ResearchKit Quals and TheoryForge are independent projects that share a common concern: helping researchers produce rigorous work.

- **ResearchKit Quals** tries to name and assess the tacit skills researchers need.
- **TheoryForge** provides AI-assisted tooling for the data-to-paper pipeline.

We believe these projects can inform each other — the competency work helps us think about what skills matter when using AI tools, and the tooling work surfaces which skills are hardest to replace with AI assistance. But the nature of these links is far from settled.

**What we are NOT claiming:**
- That the current domain list is correct or complete
- That we know the right mapping between competencies and tool access
- That gating tool use on formal assessments is the right approach
- That these two projects need to be tightly coupled

---

## Speculative Links Between Competencies and Tool Use

The table below captures our *intuition* about which competencies might matter most for which kinds of AI-assisted research tasks. These are hypotheses, not prescriptions.

| Research Competency | AI Tool Tasks Where It Might Matter | Why We Think So |
|--------------------|------------------------------------|-----------------|
| Pattern Recognition | Evaluating AI-surfaced patterns, deciding what to pursue | AI finds patterns indiscriminately; judgment about what's *interesting* is human |
| Theoretical Positioning | Assessing AI-generated theory connections | AI can find citations but can't judge what constitutes a real contribution |
| Qual Mechanism Extraction | Supervising AI coding of qualitative data | AI coding without understanding produces plausible-looking but shallow analysis |
| Theoretical Framing | Evaluating AI-generated framings | AI generates many framings; choosing wisely requires deep theoretical knowledge |
| Epistemological Genre | Catching genre mismatches in AI-generated text | AI defaults to hypothesis-testing language even for discovery papers |
| Adversarial Evidence | Auditing AI-surfaced evidence for completeness | AI tends toward confirmation; adversarial instincts are human |
| Claim Verification | Verifying AI-generated claims against actual data | AI confabulates; verification discipline is essential |
| Argument Construction | Evaluating and revising AI-drafted prose | AI produces structurally flat prose; recognizing good argument architecture is human |

---

## Open Questions

These are genuine unknowns we're working through:

1. **Should competency status affect tool behavior at all?** Maybe it's better to let anyone use the tools and focus on training separately. Or maybe some form of progressive disclosure helps prevent overreliance.

2. **If so, how?** Options range from hard access gates (can't run the command) to soft guidance (extra scaffolding and warnings) to pure documentation (here's what you should know before using this).

3. **Is the relationship directional?** We initially assumed quals-then-tools, but maybe tool use *develops* competencies. Students might learn pattern recognition by seeing what AI finds and comparing it to their own instincts.

4. **How idiosyncratic is this mapping?** The current competency list reflects one research tradition (qualitative/mixed-methods organizational studies). Different fields would need different competency-tool mappings.

5. **What's the right granularity?** The current 7-domain structure might be too coarse or too fine. Tool use might reveal natural skill clusters we haven't identified yet.

---

## Historical Context

Earlier versions of this document contained detailed command-to-competency unlock maps and implementation code for gating TheoryForge commands based on competency levels. We removed that coupling because:

- The competency framework itself is still a draft — locking tool behavior to an unstable framework creates false precision
- The right relationship between skill development and tool access is an empirical question we haven't answered yet
- Premature coupling would make both projects harder to evolve independently
- Different advisors and programs will have different views on when students are ready for AI assistance

The unlock map and gating code are preserved in git history if we ever want to revisit that approach.
