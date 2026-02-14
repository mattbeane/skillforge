# Research-Quals: A Faculty Guide

**Your PhD students are going to use AI for research. Here's the middle path between banning it and hoping for the best.**

---

## The Problem You're Facing

AI tools can now generate polished research outputs: literature reviews, data analysis, theoretical framings, even full manuscript drafts. Your students know this. Some are already using these tools, with or without guidance.

You have three options:

1. **Ban AI entirely.** Unenforceable, and it leaves students unprepared for the research world they're entering.

2. **Allow AI with no guardrails.** Produces students who can generate papers but can't evaluate whether those papers are any good. The hallucination risk alone should give you pause — one researcher recently discovered his AI co-author had fabricated quotes, informant identifiers, and data files that didn't exist, all consistent enough to be believable.

3. **Gate AI behind demonstrated competency.** Students prove they understand the research process — by doing it — before they're allowed to accelerate with AI tools. This is what research-quals provides.

---

## What Research-Quals Is

A competency-based training system for mixed-methods management research. Seven domains. Three levels. Real data.

| Domain | What It Tests |
|--------|--------------|
| 1. Pattern Recognition | Can you tell signal from noise? |
| 2. Theoretical Positioning | Can you frame a contribution? |
| 3. Research Design | Can you match design to question? |
| 4. Qualitative Rigor | Can you code defensibly? |
| 5. Literature Synthesis | Can you position in a conversation? |
| 6. Adversarial Evidence | Can you find disconfirming data? |
| 7. Claim Verification | Do your claims match your evidence? |

### Three Levels Per Domain

**Foundation**: Can you identify good practice when you see it? Conceptual exercises. Unlimited retakes — this is learning.

**Practice**: Given real data, can you do it yourself? Work on actual research problems. Detailed feedback against expert baselines.

**Mastery**: Can you do it independently and defend your choices? Single attempt. This is where it counts.

### The Capstone: Prove You Can Supervise AI

Two options (students can do one or both):

**AI Output Supervision**: Review an AI-generated paper and catch all the issues. The AI draft is deliberately produced without safeguards — genre violations, overclaimed contributions, hallucinated evidence, buried disconfirmation. Can the student find what's wrong?

**Build Your Own Machine**: Design and build a bespoke analytical pipeline for an unfamiliar dataset. Then defend every design choice against an expert comparison. This forces articulation of tacit knowledge — you can't automate what you can't describe.

---

## Why This Matters for Your Program

### The Apprenticeship Model Is Failing

Most PhD training in research craft happens through osmosis: watch your advisor, absorb tacit knowledge, hope you pick up the pattern recognition. Some students get great mentorship. Many don't. Luck plays too large a role.

Research-quals makes the implicit explicit. The seven domains capture what expert researchers do intuitively — the robustness checks they run first, the disconfirming evidence they hunt for, the overclaims they catch. Making this learnable doesn't replace mentorship; it gives mentorship structure.

### AI Changes the Stakes

A student who can't recognize a hallucinated quote when they see one shouldn't be using tools that routinely hallucinate. A student who doesn't understand genre conventions shouldn't be using tools that default to hypothesis-testing framing for every paper. A student who's never manually coded data can't evaluate whether AI coding is any good.

Research-quals establishes the floor. Once a student demonstrates competency, they can use AI tools productively — and you can trust their output.

### What Your Students Want

In a recent CSS Lab session at UCSB (February 2025), PhD students consistently expressed two things:

1. They want explicit instruction on research craft. One student said: "I've been begging for explicit instruction on how to do these things for years."

2. They want permission to use AI responsibly, not a blanket ban.

Research-quals gives them both.

---

## How to Use It

### For an Individual Advisor

1. **Point your student at the system.** Have them run `research-quals status` to see the domains.
2. **Start with Domain 1 (Foundation).** Takes 2-4 hours. Low stakes, unlimited retakes.
3. **Review their Practice and Mastery work.** The system provides expert baselines for comparison, but your domain expertise adds irreplaceable context.
4. **Use the capstone as a milestone.** "Before you use theory-forge on your dissertation data, complete the AI Supervisor capstone."

### For a PhD Program

1. **Adopt as a methods supplement.** Research-quals complements existing methods courses — it doesn't replace them. It focuses on the applied judgment that courses often can't teach.
2. **Set program-level expectations.** "All students complete Domains 1-4 (Foundation level) by end of Year 1."
3. **Use capstone for AI policy.** "Students who pass the capstone are certified to use AI research tools in their dissertation work. Others must use them under advisor supervision only."
4. **Contribute expert baselines.** The system improves with more expert perspectives. Faculty can contribute anonymized data from their research — all processing runs locally, data never leaves your machine.

### Timeline

| Stage | Time | What Happens |
|-------|------|-------------|
| Foundation (all 7) | 2-4 weeks | Conceptual understanding |
| Practice (all 7) | 4-8 weeks | Applied skill on real data |
| Mastery (all 7) | 4-8 weeks | Independent demonstration |
| Capstone | 1-3 weeks | Integration + AI supervision |
| **Total** | **3-6 months** | Full competency |

Students with prior qualitative methods training can test out of Foundation immediately.

---

## What It Connects To

Research-quals is part of an ecosystem:

- **[Theory-forge](https://github.com/mattbeane/theory-forge)**: AI-assisted pipeline for producing theory-building papers. Research-quals badges gate access to theory-forge capabilities. Students who pass Domain 1 Practice can use pattern discovery (guided). Students who pass all seven Mastery badges get full access.

- **Living Paper**: Verification system that creates auditable links between claims and evidence. Used in theory-forge's verification stage. Addresses the "how do I know your data is real?" concern that reviewers will increasingly raise.

Both are open source (MIT license). Both are works in progress. Both benefit from faculty feedback and contribution.

---

## Common Objections

**"My students should learn by struggling, not by following a checklist."**
Agreed — and research-quals IS struggle. Practice and Mastery levels require students to do real analysis on unfamiliar data, not follow instructions. The checklist is the domains; the struggle is doing the work within them.

**"I don't trust AI-based assessment."**
Foundation assessments are auto-scored (multiple choice + short answer). Practice and Mastery work is designed for advisor review. The system provides rubrics and expert baselines, but you make the judgment call. AI assists scoring at Levels 2-3 but faculty certification is the gold standard.

**"This will slow down my students."**
A student who can't catch hallucinated data will produce papers that get desk-rejected — or worse, published and later retracted. Three to six months of structured competency building saves years of wasted effort.

**"Why seven domains? Who decided these?"**
The domains emerged from operationalizing what expert researchers actually do when producing papers — induced from three months of building AI research tools and finding every way they fail. The list is provisional and open to revision. If your experience suggests different or additional domains, that's a conversation worth having.

---

## Get Started

```bash
git clone https://github.com/mattbeane/research-quals.git
cd research-quals
```

Start by reading the domain descriptions in `competencies/` and the assessment specs in `assessments/` to see if this fits your program.

> **Note**: The `research-quals` CLI (for taking and submitting assessments) is in development. The curriculum content, assessment rubrics, and expert baselines are complete and usable now. CLI automation is coming.

**Questions?** Open an issue or contact mattbeane@ucsb.edu

---

*Research-quals: Because "I took a methods course" isn't the same as "I can do research." And "I can prompt an AI" isn't the same as "I can supervise one."*
