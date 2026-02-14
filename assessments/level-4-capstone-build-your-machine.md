# Level 4: Alternative Capstone — Build Your Own Machine

## What This Is

An alternative capstone assessment (can be taken instead of or in addition to the AI Output Supervision capstone). Students prove they've internalized research craft by **building their own analytical pipeline** for an unfamiliar dataset and defending every design choice.

**Origin**: Paul Leonardi proposed this approach: "Show me your machine, and we'll debrief about what you thought you knew about the scholarly process that led you to build it that way." The pedagogical insight is that building an analytical tool forces articulation of tacit knowledge — you can't automate what you can't describe.

**The copy problem and why it doesn't matter**: Theory-forge is an open repository. Students can look at every command. That's fine — encouraged, even. The test is designed so that *having seen theory-forge doesn't help much*, because:

1. The dataset is unfamiliar. Theory-forge's pipeline reflects one researcher's priorities for one kind of data. A different dataset demands different choices.
2. The defense is where it counts. You must defend every choice as *yours* — why this step, why this order, why this quality check, for *this* data. Parroting someone else's rationale collapses under questioning.
3. The hardest part is what you *leave out* and what you *add*. Anyone can copy the full command list. The skill is knowing what this specific dataset needs and doesn't need.

**Prerequisite**: Level 3 pass in all seven domains.

**Time**: 2-3 weeks (design + build + defense)

**Attempts**: One. This is a qualifying exam.

---

## The Setup

### Materials Provided

1. **A dataset the student has NOT seen before**
   - Anonymized qualitative data from a faculty contributor
   - 15-30 interview transcripts + any available field notes or quantitative data
   - Brief context document (setting, research question, data collection timeline)

2. **Access to Claude Code (or equivalent)** with ability to create custom commands/agents

3. **Full access to theory-forge, research-quals, and any other publicly available tools**
   - Students are encouraged to study existing pipelines
   - The test is not whether they've seen these tools — it's whether they can adapt, extend, or depart from them with judgment

4. **Expert pipeline** (revealed after submission): How a skilled researcher would build a pipeline for this specific dataset, and why

### What Makes This Hard Even With Full Access

The dataset is deliberately chosen so that theory-forge's default pipeline is a poor fit. Possible mismatches:

- Data that's primarily processual (theory-forge's core pipeline is cross-sectional)
- Data where the "finding" is a phenomenon, not a theory violation (Zuckerman gates don't apply)
- Data with unusual structure (all field notes, no interviews; or longitudinal with multiple sites)
- Data where the interesting thing is an absence, not a presence
- Data that demands integration with a domain-specific literature theory-forge knows nothing about

A student who just copies theory-forge's commands will produce a pipeline that *runs* but misses what matters about *this* data. That gap is what the defense exposes.

---

## The Task

### Part A: Pipeline Design Document (30%)

Before building anything, write a design document (2000-3000 words):

1. **Initial data assessment** (500 words)
   - What did you notice in a first pass through the data?
   - What kind of paper could this become?
   - What contribution type does this suggest? (violation, elaboration, phenomenon, etc.)

2. **Pipeline architecture** (1000 words)
   - What analytical steps does your pipeline include?
   - In what order? Why this sequence?
   - What are the dependencies between steps?
   - What quality gates exist? What must pass before proceeding?
   - **Where you departed from existing tools and why** — if you borrowed from theory-forge, say so and explain your adaptation. If you built something new, explain what existing tools lack.

3. **Design rationale for each component** (500-1000 words)
   - For each agent/step: why does this exist? What does it catch?
   - What alternative designs did you consider and reject?
   - What tacit knowledge are you encoding in each component?

4. **What your pipeline does NOT do** (250 words)
   - What analytical tasks remain human-only in your design?
   - What did you see in existing tools that you deliberately excluded, and why?
   - Why did you draw the automation line there?

### Part B: Working Pipeline (40%)

Build the pipeline as a set of executable agents/prompts. Requirements:

1. **Minimum 5 agents/steps** (most students will create 8-15)
2. **Each agent must have**:
   - Clear purpose statement
   - Specified inputs and outputs
   - Analytical logic (what to look for, how to evaluate)
   - Quality checks or failure modes
3. **At least one adversarial component** (something that tries to break the analysis)
4. **A sequencing mechanism** (soft or hard gates between steps)
5. **At least one component that doesn't exist in theory-forge** — something this data demands that the existing toolkit doesn't provide
6. **Run the pipeline on the provided data** and include the output

### Part C: Defense (30%)

Oral or written defense (45-60 minutes or 2000-3000 words):

1. **Walk through your pipeline** (15-20 min)
   - Demonstrate each step with the actual data
   - Show where your pipeline caught something important
   - Show where it missed something (self-awareness)

2. **Respond to expert comparison** (15-20 min)
   After revealing the expert pipeline, address:
   - What did the expert include that you didn't? Why might they have?
   - What did you include that the expert didn't? Is your addition justified?
   - Where do your designs diverge most? What does that reveal about your analytical assumptions?
   - **If you borrowed from theory-forge**: What did you keep, what did you change, and what did the changes reveal about your understanding?

3. **Meta-reflection** (10-15 min)
   - What did building this pipeline teach you about research?
   - What tacit knowledge did you discover you had (or lacked)?
   - What would you change if you rebuilt it?
   - How does your pipeline reflect your scholarly identity — as distinct from the tools you studied?

---

## Evaluation

### Part A: Design Document (30%)

| Criterion | Points |
|-----------|--------|
| Data assessment shows genuine engagement — not generic boilerplate | 15 |
| Pipeline architecture is tailored to THIS data, not copy-pasted | 15 |
| Design rationale reveals understanding of research process | 15 |
| "Does NOT do" section shows judgment about automation boundaries | 10 |
| **Subtotal** | **55** |

*Scaled to 30% of total*

### Part B: Working Pipeline (40%)

| Criterion | Points |
|-----------|--------|
| Pipeline runs and produces structured output | 10 |
| Individual agents are well-specified (clear purpose, logic, quality checks) | 15 |
| Adversarial component is genuinely challenging | 10 |
| At least one novel component not found in existing tools | 10 |
| Sequencing reflects understanding of analytical dependencies | 10 |
| Pipeline output on test data is analytically useful | 15 |
| **Subtotal** | **70** |

*Scaled to 40% of total*

### Part C: Defense (30%)

| Criterion | Points |
|-----------|--------|
| Can explain and justify each design choice as THEIR OWN | 15 |
| Honest about pipeline's limitations and misses | 10 |
| Comparison to expert pipeline shows learning, not defensiveness | 15 |
| Meta-reflection reveals genuine insight about research craft | 15 |
| **Subtotal** | **55** |

*Scaled to 30% of total*

### Passing Threshold

- **Overall**: ≥70%
- **Part B minimum**: ≥50% (must produce a working pipeline)
- **Defense minimum**: Must demonstrate understanding of at least 5 of 7 domains in design rationale

### How Copying Gets Caught

The rubric is designed so that verbatim copying produces a mediocre score:

- "Pipeline architecture tailored to THIS data" (15 pts) — a generic theory-forge copy scores low
- "Novel component not found in existing tools" (10 pts) — zero if nothing new
- "Can explain and justify each design choice as THEIR OWN" (15 pts) — collapses when questioned about borrowed choices
- The expert pipeline is built *for this specific dataset* — divergence from theory-forge's generic structure is expected and rewarded

A student who studies theory-forge, understands it deeply, and adapts it thoughtfully for novel data? That's exactly what we want. That's genuine learning. The problem isn't seeing someone else's work — it's failing to make it your own.

---

## What This Tests

### Articulation of Tacit Knowledge
Can you make your implicit understanding of research explicit enough to encode it?

### Architectural Judgment
Can you decompose a complex intellectual process into coherent, sequenced steps — tailored to specific data, not generic?

### Adaptation vs. Imitation
Can you study someone else's approach and produce something that's genuinely yours — not just a copy, but a response?

### Self-Awareness
Do you know what you know and what you don't? Can you draw appropriate boundaries for automation?

### Research Identity
Does your pipeline reflect a coherent scholarly perspective, not just a grab bag of techniques borrowed from available tools?

---

## Why This Matters

This capstone tests a different (and complementary) skill from the AI Output Supervision capstone:

| AI Output Supervision | Build Your Own Machine |
|----------------------|----------------------|
| Can you catch what AI gets wrong? | Can you design what AI should do right? |
| Evaluative judgment | Constructive judgment |
| Critic | Architect |
| "This paper has problems" | "Here's how I'd build the system for THIS data" |

**Both skills matter.** Catching errors requires knowing what good looks like. Building tools requires knowing what to check for. Ideally, students do both capstones.

The Build Your Own Machine capstone is especially valuable because:

1. **It forces articulation.** You can't automate "look for interesting patterns" — you have to specify WHAT patterns, defined HOW, evaluated AGAINST WHAT.

2. **It reveals gaps.** Students who don't understand adversarial evidence will build pipelines without it. Students who don't understand genre will build hypo-deductive pipelines for inductive papers. The pipeline IS the diagnostic.

3. **It creates conversation.** The defense — especially the comparison to an expert pipeline — generates exactly the kind of mentorship conversation that's hardest to create in traditional PhD training.

4. **It produces something useful.** Unlike an exam that's graded and forgotten, the student leaves with a working tool they can use, share, and iterate on.

5. **It's robust to open-source tools.** Having access to theory-forge makes the exercise more interesting, not easier. The student must grapple with someone else's choices and decide what to keep, adapt, or reject. That's a higher-order skill than building from scratch.

---

## Bonus Exercise: Induce the Problem Space

For students who want an additional challenge (or programs that want to add it):

Before Part A, give the student the dataset and ask: **What categories of skill and judgment does this research require?** Have them derive their own decomposition of the problem space — what are the areas where human judgment is essential? — before they start designing a pipeline.

Then compare their induced categories to the seven research-quals domains. Where do they overlap? Where do they diverge? If the student identifies something we missed, that's a contribution.

This exercise pairs well with the capstone but is genuinely optional. The core test remains: build your machine and defend it.

---

## For Faculty: Creating Assessment Materials

### Selecting a Dataset

Choose data that:
- Is rich enough to support multiple framings (don't want one obvious answer)
- **Doesn't fit neatly into theory-forge's default pipeline** (this is what makes copying insufficient)
- Contains common analytical traps (noise that looks like signal, mechanisms that seem simple but aren't)
- Has known expert analysis to compare against
- Is from a domain the student hasn't worked in (tests transferability)

### Building the Expert Pipeline

Document YOUR approach:
- What steps would you include?
- What order? What gates?
- **Where would you depart from theory-forge and why?** (This is the comparison material)
- What's unique about your approach to this data?
- What would you expect a strong student to include?
- What would distinguish excellent from adequate pipelines?

### Comparison Rubric

Create specific comparison points:
- "Expert included adversarial evidence at step 3; student who omits this is missing Domain 6"
- "Expert used temporal analysis because the data spans 2 years; student who ignores time is missing processual thinking"
- "Expert drew the automation line at coding — if student automates coding without manual verification, that's a red flag"
- "Expert departed from theory-forge's Zuckerman gate because this paper is phenomenon-driven — student who keeps the gate uncritically hasn't read the data"

---

## The Leonardi Principle

> "I'll show you my supercharged table saw for making papers. It's unique to my style and taste. And then you have to go build your own. Show me your tool. And we're going to debrief about how you constructed that and what you thought you knew about the scholarly process that led you to build your machine that way."

This assessment operationalizes that principle. The student doesn't learn just from using someone else's tool — they learn from building their own and defending it. Having seen theory-forge enriches this process. It doesn't shortcut it.
