# Level 4: Alternative Capstone — Build Your Own Machine

## What This Is

An alternative capstone assessment (can be taken instead of or in addition to the AI Output Supervision capstone). Students prove they've internalized all seven domains by **building their own analytical pipeline** — a bespoke set of agents/prompts that encode their tacit knowledge about how to do rigorous research.

Then they defend their design choices.

**Origin**: Paul Leonardi proposed this approach: "Show me your machine, and we'll debrief about what you thought you knew about the scholarly process that led you to build it that way." The pedagogical insight is that building an analytical tool forces articulation of tacit knowledge — you can't automate what you can't describe.

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

3. **Expert pipeline** (revealed after submission): How a skilled researcher would build a pipeline for this specific dataset, and why

### What the Student Builds

A working analytical pipeline that:
- Takes the provided dataset as input
- Produces a structured analysis output
- Encodes the student's judgment about what analytical steps matter, in what order, and with what quality checks
- Is documented with design rationale for each component

**This is NOT about producing a paper.** It's about designing the machine that COULD produce a paper — and being able to defend every design choice.

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

3. **Design rationale for each component** (500-1000 words)
   - For each agent/step: why does this exist? What does it catch?
   - What alternative designs did you consider and reject?
   - What tacit knowledge are you encoding in each component?

4. **What your pipeline does NOT do** (250 words)
   - What analytical tasks remain human-only in your design?
   - Why did you draw the line there?

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
5. **Run the pipeline on the provided data** and include the output

### Part C: Defense (30%)

Oral or written defense (30-45 minutes or 1500-2000 words):

1. **Walk through your pipeline**
   - Demonstrate each step with the actual data
   - Show where your pipeline caught something important
   - Show where it missed something (self-awareness)

2. **Respond to expert comparison**
   After revealing the expert pipeline, address:
   - What did the expert include that you didn't? Why might they have?
   - What did you include that the expert didn't? Is your addition justified?
   - Where do your designs diverge most? What does that reveal about your analytical assumptions?

3. **Meta-reflection**
   - What did building this pipeline teach you about research?
   - What tacit knowledge did you discover you had (or lacked)?
   - What would you change if you rebuilt it?
   - How does your pipeline reflect your scholarly identity?

---

## Evaluation

### Part A: Design Document (30%)

| Criterion | Points |
|-----------|--------|
| Data assessment shows genuine engagement | 10 |
| Pipeline architecture is logically coherent | 15 |
| Design rationale reveals understanding of research process | 20 |
| "Does NOT do" section shows judgment about automation boundaries | 10 |
| **Subtotal** | **55** |

*Scaled to 30% of total*

### Part B: Working Pipeline (40%)

| Criterion | Points |
|-----------|--------|
| Pipeline runs and produces structured output | 10 |
| Individual agents are well-specified (clear purpose, logic, quality checks) | 20 |
| Adversarial component is genuinely challenging | 10 |
| Sequencing reflects understanding of analytical dependencies | 10 |
| Pipeline output on test data is analytically useful | 15 |
| Code quality and documentation | 5 |
| **Subtotal** | **70** |

*Scaled to 40% of total*

### Part C: Defense (30%)

| Criterion | Points |
|-----------|--------|
| Can explain and justify each design choice | 15 |
| Honest about pipeline's limitations and misses | 10 |
| Comparison to expert pipeline shows learning | 15 |
| Meta-reflection reveals genuine insight about research craft | 15 |
| **Subtotal** | **55** |

*Scaled to 30% of total*

### Passing Threshold

- **Overall**: ≥70%
- **Part B minimum**: ≥50% (must produce a working pipeline)
- **Defense minimum**: Must demonstrate understanding of at least 5 of 7 domains in design rationale

---

## What This Tests

### Articulation of Tacit Knowledge
Can you make your implicit understanding of research explicit enough to encode it?

### Architectural Judgment
Can you decompose a complex intellectual process into coherent, sequenced steps?

### Self-Awareness
Do you know what you know and what you don't? Can you draw appropriate boundaries for automation?

### Research Identity
Does your pipeline reflect a coherent scholarly perspective, not just a grab bag of techniques?

### Comparison Skill
Can you learn from seeing how an expert would approach the same problem differently?

---

## Why This Matters

This capstone tests a different (and complementary) skill from the AI Output Supervision capstone:

| AI Output Supervision | Build Your Own Machine |
|----------------------|----------------------|
| Can you catch what AI gets wrong? | Can you design what AI should do right? |
| Evaluative judgment | Constructive judgment |
| Critic | Architect |
| "This paper has problems" | "Here's how I'd build the system" |

**Both skills matter.** Catching errors requires knowing what good looks like. Building tools requires knowing what to check for. Ideally, students do both capstones.

The Build Your Own Machine capstone is especially valuable because:

1. **It forces articulation.** You can't automate "look for interesting patterns" — you have to specify WHAT patterns, defined HOW, evaluated AGAINST WHAT.

2. **It reveals gaps.** Students who don't understand adversarial evidence will build pipelines without it. Students who don't understand genre will build hypo-deductive pipelines for inductive papers. The pipeline IS the diagnostic.

3. **It creates conversation.** The defense — especially the comparison to an expert pipeline — generates exactly the kind of mentorship conversation that's hardest to create in traditional PhD training.

4. **It produces something useful.** Unlike an exam that's graded and forgotten, the student leaves with a working tool they can use, share, and iterate on.

---

## For Faculty: Creating Assessment Materials

### Selecting a Dataset

Choose data that:
- Is rich enough to support multiple framings (don't want one obvious answer)
- Contains common analytical traps (noise that looks like signal, mechanisms that seem simple but aren't)
- Has known expert analysis to compare against
- Is from a domain the student hasn't worked in (tests transferability)

### Building the Expert Pipeline

Document YOUR approach:
- What steps would you include?
- What order? What gates?
- What's unique about your approach to this data?
- What would you expect a strong student to include?
- What would distinguish excellent from adequate pipelines?

### Comparison Rubric

Create specific comparison points:
- "Expert included adversarial evidence at step 3; student who omits this is missing Domain 6"
- "Expert used temporal analysis because the data spans 2 years; student who ignores time is missing processual thinking"
- "Expert drew the automation line at coding — if student automates coding without manual verification, that's a red flag"

---

## The Leonardi Principle

> "I'll show you my supercharged table saw for making papers. It's unique to my style and taste. And then you have to go build your own. Show me your tool. And we're going to debrief about how you constructed that and what you thought you knew about the scholarly process that led you to build your machine that way."

This assessment operationalizes that principle. The student doesn't learn from using someone else's tool — they learn from building their own and defending it.
