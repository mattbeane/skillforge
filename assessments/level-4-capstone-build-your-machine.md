# Level 4: Alternative Capstone — Induce the Problem Space

## What This Is

An alternative capstone assessment (can be taken instead of or in addition to the AI Output Supervision capstone). Students prove they've internalized the deep structure of research craft by **inducing the categories of skill and judgment required** to do AI-assisted qualitative research well — from first principles, before seeing any existing decomposition.

Then they build a pipeline based on their own decomposition and defend it.

**Origin**: Paul Leonardi proposed the underlying insight: "Show me your machine, and we'll debrief about what you thought you knew about the scholarly process that led you to build it that way." But there's a problem with "build your own machine" as a test: anyone can copy someone else's. The deeper skill — and the harder test — is *can you derive what the machine should do before seeing how others built theirs?*

**The real test**: Given an unfamiliar dataset and no access to existing tools or domain decompositions, can you induce the areas where human judgment is essential, where automation is appropriate, and where supervision is required? That's the skill that makes a researcher irreplaceable in an AI-augmented world.

**Prerequisite**: Level 3 pass in all seven domains.

**Time**: 2-3 weeks (induction + build + defense)

**Attempts**: One. This is a qualifying exam.

---

## The Setup

### Materials Provided

1. **A dataset the student has NOT seen before**
   - Anonymized qualitative data from a faculty contributor
   - 15-30 interview transcripts + any available field notes or quantitative data
   - Brief context document (setting, research question, data collection timeline)

2. **Access to Claude Code (or equivalent)** with ability to create custom commands/agents

3. **Withheld until Part C**: The seven research-quals domains and any existing pipelines (e.g., theory-forge). The student must work without seeing these.

### What the Student Does NOT Get

- No access to the research-quals domain list
- No access to theory-forge or its command structure
- No examples of other researchers' analytical pipelines
- No hints about "what matters" beyond the dataset itself

**This constraint is the point.** The test is whether the student can derive what matters from engaging with the data and reflecting on the research process, not whether they can reproduce someone else's framework.

---

## The Task

### Part A: Induce the Problem Space (30%)

Before building anything, spend 3-5 days with the data and write a problem space analysis (2000-3000 words):

1. **What kinds of judgment does this research require?** (1000-1500 words)
   - Work through the data. Try to imagine producing a publishable paper from it.
   - As you go, notice: where does the work require *human* judgment? Where could a machine help? Where would machine output need supervision?
   - Derive a set of **categories of skill/judgment** that this work demands.
   - For each category: What makes it hard? What could go wrong? What does "good" look like?

2. **Your proposed decomposition** (500-1000 words)
   - Name your categories. Define them. Explain why these and not others.
   - How do they relate to each other? Is there a sequence? Dependencies?
   - What's the relationship between your categories and the specific dataset, vs. what you think would generalize to other datasets?

3. **Where you drew the automation line** (500 words)
   - For each category: what can be safely automated, what requires human judgment, what requires human supervision of AI output?
   - Why did you draw the line there?

**Evaluation emphasis**: The quality of the decomposition matters more than whether it matches any existing framework. We're looking for evidence that the student can think structurally about the research process, not that they can reproduce the "right" answer.

### Part B: Working Pipeline (40%)

Build a pipeline based on YOUR decomposition (not someone else's). Requirements:

1. **Your pipeline structure must follow from your Part A decomposition** — the agents/steps should map to your categories, not to some other framework
2. **Minimum 5 agents/steps** (most students will create 8-15)
3. **Each agent must have**:
   - Clear purpose statement tied to your decomposition
   - Specified inputs and outputs
   - Analytical logic (what to look for, how to evaluate)
   - Quality checks or failure modes
4. **At least one adversarial component** (something that tries to break the analysis)
5. **A sequencing mechanism** (soft or hard gates between steps)
6. **Run the pipeline on the provided data** and include the output

### Part C: Defense (30%)

Oral or written defense (45-60 minutes or 2000-3000 words):

1. **Your decomposition vs. ours** (15-20 min)
   The seven research-quals domains and any existing pipelines are now revealed. Address:
   - What did you identify that we identified? Different name, same idea?
   - What did you identify that we didn't? Is there something we're missing?
   - What did we identify that you didn't? Was it absent from your data, or did you miss something important?
   - Where do the decompositions diverge most? What does that reveal?

2. **Pipeline walkthrough** (15-20 min)
   - Demonstrate each step with the actual data
   - Show where your pipeline caught something important
   - Show where it missed something (self-awareness)

3. **Meta-reflection** (10-15 min)
   - What did this exercise teach you about research craft?
   - What tacit knowledge did you discover you had (or lacked)?
   - Would you change your decomposition now that you've seen ours? Why or why not?
   - If you were advising a junior researcher, what would you tell them matters most?

---

## Evaluation

### Part A: Problem Space Induction (30%)

| Criterion | Points |
|-----------|--------|
| Categories show genuine engagement with the data, not abstract speculation | 15 |
| Decomposition is coherent — categories are distinct, collectively meaningful | 15 |
| Automation line reflects real understanding of where AI helps vs. hurts | 10 |
| Reasoning is transparent — student shows their work, not just conclusions | 10 |
| **Subtotal** | **50** |

*Scaled to 30% of total*

### Part B: Working Pipeline (40%)

| Criterion | Points |
|-----------|--------|
| Pipeline structure follows from student's own decomposition (not borrowed) | 15 |
| Pipeline runs and produces structured output | 10 |
| Individual agents are well-specified (clear purpose, logic, quality checks) | 15 |
| Adversarial component is genuinely challenging | 10 |
| Pipeline output on test data is analytically useful | 15 |
| **Subtotal** | **65** |

*Scaled to 40% of total*

### Part C: Defense (30%)

| Criterion | Points |
|-----------|--------|
| Comparison to existing framework is honest and insightful | 15 |
| Identifies genuine contributions beyond existing decomposition | 10 |
| Identifies genuine gaps in own decomposition without defensiveness | 10 |
| Meta-reflection reveals insight about research craft, not just this exercise | 15 |
| **Subtotal** | **50** |

*Scaled to 30% of total*

### Passing Threshold

- **Overall**: ≥70%
- **Part A minimum**: ≥50% (must produce a coherent decomposition)
- **Part B minimum**: ≥50% (must produce a working pipeline)
- **Defense**: Must engage substantively with comparison — can't just say "mine is different"

---

## What This Tests

### First-Principles Thinking
Can you derive what matters from the work itself, rather than from a provided framework?

### Structural Reasoning About Research
Can you decompose a complex intellectual process into coherent categories that map to real judgment calls?

### Self-Awareness
Do you know what you know and what you don't? Can you draw appropriate boundaries for automation?

### Intellectual Honesty
Can you compare your decomposition to an existing one without defensiveness, identifying both contributions and gaps?

### Research Identity
Does your decomposition reflect a coherent scholarly perspective, or just a grab bag of techniques?

---

## Why This Matters

This capstone tests a different (and complementary) skill from the AI Output Supervision capstone:

| AI Output Supervision | Induce the Problem Space |
|----------------------|--------------------------|
| Can you catch what AI gets wrong? | Can you derive what AI should do right? |
| Evaluative judgment | Generative + structural judgment |
| Critic | Architect of the problem space itself |
| "This paper has problems" | "Here are the kinds of judgment this work requires" |

**Both skills matter.** Catching errors requires knowing what good looks like. Designing tools requires knowing what to check for. Ideally, students do both capstones.

The Induce the Problem Space capstone is especially valuable because:

1. **It can't be copied.** Unlike "build a pipeline" (where students can examine theory-forge and reproduce it), "derive the categories from first principles" requires original analytical work. The student's decomposition is their own intellectual contribution.

2. **It tests the deepest skill.** Knowing what the categories of judgment ARE is harder than being skilled within them. This is meta-competence — knowing what competence consists of.

3. **It makes the seven domains honestly provisional.** If a student derives a better decomposition, that's not a failure of the test — it's a contribution to the field. The capstone invites students to improve on the framework, not just reproduce it.

4. **It creates the richest conversation.** The defense — comparing decompositions — generates exactly the kind of mentorship dialogue that's hardest to create in traditional PhD training. "You identified X and I didn't — tell me why you think it matters."

---

## For Faculty: Creating Assessment Materials

### Selecting a Dataset

Choose data that:
- Is rich enough to support multiple framings (don't want one obvious answer)
- Contains common analytical traps (noise that looks like signal, mechanisms that seem simple but aren't)
- Has known expert analysis to compare against
- Is from a domain the student hasn't worked in (tests transferability)

### Building the Comparison Framework

Prepare YOUR decomposition of what matters for this dataset:
- What categories of judgment does this data demand?
- How does your decomposition relate to the seven domains? (exact match? different emphasis? additional categories?)
- What would you expect a strong student to identify?
- What would distinguish excellent from adequate inductions?

### Comparison Rubric

Create specific comparison points:
- "Expert identified the need for temporal analysis because data spans 2 years; student who misses temporal judgment is missing something important"
- "Expert separated 'pattern finding' from 'pattern evaluation'; student who collapses these may not understand robustness"
- "Expert drew the automation line at qualitative coding; if student puts coding fully in the 'automate' bucket, that's worth exploring in defense"

---

## The Leonardi Principle (Revised)

> "Show me your machine. And we're going to debrief about what you thought you knew about the scholarly process that led you to build it that way."

The original insight was about building machines. We've extended it: before you build the machine, derive what the machine *should* do. The scholarly process itself is what we're asking you to induce — the categories of craft that matter, the judgment calls that can't be automated, the places where supervision is essential.

If you can do that from first principles, you can build any machine. And more importantly, you can evaluate whether someone else's machine is any good.
