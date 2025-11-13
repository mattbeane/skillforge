# AI PROMPT LIBRARY
## Process Efficiency & Skill Development Analysis

**Workshop: Measure Twice, Spend Once**

---

## THE KEY INSIGHT: FROM DESCRIPTION TO MEASUREMENT

**The problem with most analysis:** It describes what happened but doesn't give you trackable metrics.

**What you need:** Quantifiable KPIs you can measure month-over-month to track both efficiency gains AND skill development.

**These prompts are designed to extract numbers, not just narratives** - so you can establish baselines before deploying AI, then measure actual impact (not surveys) afterward.

---

## HOW TO USE THESE PROMPTS

### Basic Workflow

1. **Gather your workflow data** (emails, Slack conversations, meeting notes, project artifacts)
2. **Copy a prompt** from below
3. **Paste it into Claude, ChatGPT, or your preferred AI tool**
4. **Provide your workflow data** in the same conversation
5. **Extract the quantified metrics** for your KPI dashboard

### Getting Quantified Outputs

**What makes a good metric:**
- ✅ **Specific unit**: Days, hours, percentage, count
- ✅ **Trackable over time**: Can measure monthly/quarterly
- ✅ **Actionable**: Points to where to improve

**Example of qualitative (not useful for KPIs):**
> "There were some delays in the approval process and the team had to wait."

**Example of quantitative (ready for KPI tracking):**
> "Approval delay: 6 days (40% of total cycle time). Target: <3 days."

### Building Your KPI Dashboard

After analyzing 2-3 workflows, create a tracking table:

```
Metric                    | Baseline | Month 1 | Month 2 | Target
--------------------------|----------|---------|---------|-------
Cycle Time (days)         | 15       | ?       | ?       | <10
Wait Time %               | 74%      | ?       | ?       | <50%
High Skill Yield Time %   | 65%      | ?       | ?       | >60%
Cross-Level Collab (count)| 3        | ?       | ?       | >2
```

**This lets you measure:** Did AI reduce cycle time? Did it preserve skill development? Where did it help vs. harm?

---

## PROCESS EFFICIENCY PROMPTS (8 prompts)

### 1. Cycle Time Extraction (with Quantified KPIs)

```
Analyze this workflow data and extract QUANTIFIED metrics:

1. Total elapsed time from start to completion (IN DAYS)
2. Active work time vs wait time (AS PERCENTAGES and IN DAYS)
3. Number of handoffs (COUNT - each time work passes between people/teams)
4. Approval/decision delays (IN DAYS for each delay)
5. Time to first response (IN HOURS - initial request to first action)

Present in this KPI-ready format:

CYCLE TIME METRICS:
- Total cycle time: X days
- Active work: Y% (Z days)
- Wait time: W% (V days)
- Handoffs: N count
- Time to first response: H hours

BOTTLENECK BREAKDOWN:
- [Stage name]: X days (Y% of total cycle time)
- [Stage name]: X days (Y% of total cycle time)

TARGET RECOMMENDATIONS:
- Reduce wait time to <50% of cycle time
- Reduce handoff count to <5 per workflow
- Reduce time to first response to <4 hours
```

**Example Output (Quantified):**

```
CYCLE TIME METRICS:
- Total cycle time: 15 days
- Active work: 26% (4 days)
- Wait time: 74% (11 days)
- Handoffs: 8 count
- Time to first response: 7 hours

BOTTLENECK BREAKDOWN:
- QA/Production Approval: 6 days (40% of total cycle time) ← BIGGEST BOTTLENECK
- Scheduling customer call: 2 days (13%)
- Initial PM response: 7 hours (3%)

Monthly KPI Tracking:
Cycle Time: 15 days → Target: <10 days
Wait Time %: 74% → Target: <50%
Handoff Count: 8 → Target: <5
```

---

### 2. Bottleneck Identification (Quantified)

```
From this workflow data, identify the top 3 bottlenecks where work slows down or stops.

For EACH bottleneck, extract these QUANTIFIED metrics:
- Time lost (IN DAYS or HOURS)
- Percentage of total cycle time consumed
- Estimated frequency (times per month this occurs)
- Cost if measurable (revenue delay, resource waste)

Present in KPI-ready format:

BOTTLENECK #1: [Name]
- Time lost: X days (Y% of cycle time)
- Cause: [approval wait / handoff / missing info / etc]
- Frequency: Z times per month (estimated)
- People/systems involved: [list]
- Monthly impact: W days total

BOTTLENECK #2: [Name]
...

PRIORITY: Attack #1 first (highest time cost)
```

**Example Output:**

```
BOTTLENECK #1: QA + Production Approval Process
- Time lost: 6 days (40% of 15-day cycle time)
- Cause: Waiting for QA cycle + production deployment approval
- Frequency: Every workflow (estimated 4 per month)
- People involved: QA team, DevOps lead approval
- Monthly impact: 24 days wasted waiting (6 days × 4 workflows)

KPI to track: Approval delay (days)
Baseline: 6 days
Target: <3 days
```

---

### 3. Handoff Analysis (Quantified)

```
Map ALL handoffs in this workflow (every time work passes from one person/team to another).

For EACH handoff, extract:
- Duration (time between handoff sent and received: IN HOURS or DAYS)
- Information loss (YES/NO - did context get lost?)
- Rework caused (YES/NO - did handoff cause backtracking?)

Present as:

HANDOFF COUNT: N total handoffs

HANDOFF DETAILS:
1. [Person A] → [Person B]: X hours delay, [info loss: Y/N], [rework: Y/N]
2. [Person B] → [Person C]: X hours delay, [info loss: Y/N], [rework: Y/N]
...

HANDOFF METRICS (KPIs):
- Average handoff delay: X hours
- Handoffs with information loss: Y count (Z%)
- Handoffs causing rework: W count (V%)

TARGET: <5 handoffs per workflow, <4 hours average delay
```

---

### 4. Decision Point Mapping (Quantified)

```
Identify every decision point in this workflow.

For EACH decision, extract QUANTIFIED data:
- Decision delay (time from question raised to decision made: IN HOURS/DAYS)
- Information gathering time (time spent collecting data to decide)
- Downstream impact (did decision cause delays or rework? IN DAYS if yes)

Present as:

DECISION COUNT: N total decisions

DECISION METRICS:
Decision #1: [What was decided]
- Who decided: [person/role]
- Decision delay: X hours/days
- Info gathering time: Y hours
- Downstream delay caused: Z days (or "none")

AGGREGATE KPIs:
- Total decision time: X days (Y% of cycle time)
- Average decision delay: Z hours
- Decisions causing rework: N count

TARGET: <24 hours average decision delay
```

---

### 5. Value vs. Waste (Quantified Breakdown)

```
Categorize EVERY step in this workflow and calculate TIME SPENT in each category:

- VALUE CREATION: directly moves toward end goal (IN DAYS or HOURS)
- COORDINATION: necessary communication/alignment (IN DAYS or HOURS)
- WAIT: delays for approval, response, availability (IN DAYS or HOURS)
- REWORK: fixing errors or revisiting decisions (IN DAYS or HOURS)

Present as percentages AND absolute time:

TIME ALLOCATION (15-day workflow example):
- Value creation: X days (Y%)
- Coordination: X days (Y%)
- Wait: X days (Y%)
- Rework: X days (Y%)

KPI DASHBOARD:
- Value-add ratio: X% (target: >40%)
- Wait time ratio: Y% (target: <30%)
- Rework ratio: Z% (target: <5%)

List top 3 waste opportunities:
1. [Activity]: X days wasted → Could be eliminated/automated
2. [Activity]: Y days wasted → Could be parallelized
3. [Activity]: Z days wasted → Could be delegated
```

---

### 6. Information Flow (Quantified)

```
Track how information moves through this workflow and QUANTIFY information problems:

Count these specific issues:
- Repeated questions (COUNT - same question asked multiple times)
- Information hunt instances (COUNT - someone had to search for context)
- Missing handoff context (COUNT - incomplete information transferred)
- Communication channel switches (COUNT - email→Slack→meeting→doc)

Present as:

INFORMATION FLOW METRICS:
- Repeated questions: N count
- Information hunts: M count
- Incomplete handoffs: P count
- Channel switches: Q count

INFORMATION GAPS (specific instances):
1. [Question X] asked Y times (wasted Z hours hunting)
2. [Context Y] missing at handoff (caused W hours delay)

KPI: Information efficiency score = 100 - (gaps + hunts)
Current: X score
Target: >90 score
```

---

### 7. Exception vs. Standard Path (Quantified)

```
Analyze whether this workflow followed standard process or required exceptions.

Categorize each step and QUANTIFY time:
- Standard/routine steps: X hours (Y% of time)
- Exception/custom problem-solving: Z hours (W% of time)

For exceptions, extract:
- Count of exceptions: N total
- Time consumed by exceptions: X days
- Whether exceptions took more time than standard path (YES/NO)

Present as:

PROCESS ADHERENCE:
- Standard path time: X days (Y%)
- Exception handling: Z days (W%)
- Exception count: N instances

EXCEPTION BREAKDOWN:
1. [What broke]: Required X hours workaround
2. [What broke]: Required Y hours escalation

KPI: Exception ratio = Z% (target: <20%)
```

---

### 8. Executive Approval Overhead (Quantified)

```
Identify ALL points where work waited for executive/leadership approval.

For EACH approval point, extract:
- Wait time (IN DAYS or HOURS)
- Percentage of total cycle time spent waiting
- Value add assessment (DID the approval change direction significantly? YES/NO)
- Parallel work opportunities (what COULD have progressed? IN DAYS)

Present as:

APPROVAL OVERHEAD:
- Total approval wait time: X days (Y% of Z-day cycle time)
- Number of approval gates: N count
- Approvals that changed direction: M count (P%)
- Approvals that were perfunctory: Q count (R%)

APPROVAL BREAKDOWN:
1. [Approval type]: X days wait, value-add: Y/N
2. [Approval type]: Z days wait, value-add: Y/N

KPI: Approval overhead ratio = Y% (target: <15% of cycle time)
```

---

## SKILL DEVELOPMENT PROMPTS (10 prompts)

### 1. Problem Complexity Assessment (Quantified)

```
Analyze ALL problems/tasks in this workflow and categorize:
- COMPLEX: expertise, judgment, novel problem-solving, ambiguity (rate 2-3 on complexity scale)
- ROUTINE: established patterns, clear answers, procedural (rate 1 on complexity scale)

For EACH person, calculate PERCENTAGES:
- Complex work: X%
- Routine work: Y%

Also rate average problem complexity on 1-3 scale:
- 1 = Routine (following procedures)
- 2 = Moderate (some judgment required)
- 3 = Novel (significant problem-solving)

Present as:

COMPLEXITY DISTRIBUTION:
[Person A]:
- Complex work: X% of time
- Routine work: Y% of time
- Average problem complexity: Z (scale 1-3)

[Person B]:
- Complex work: X% of time
- Routine work: Y% of time
- Average problem complexity: Z (scale 1-3)

TEAM AGGREGATE KPI:
- Team avg complexity score: X (target: >2.0 for skill development)
- % time in complex work: Y% (target: >40%)
```

**Example Output:**

```
Jordan (Junior Engineer):
- Complex work: 70% of time
- Routine work: 30% of time
- Average problem complexity: 2.3 (moderate-to-novel)

Alex (Senior Engineer):
- Complex work: 90% of time
- Routine work: 10% of time
- Average problem complexity: 2.8 (novel/challenging)

TEAM KPI: Avg complexity = 2.6 (target: >2.0) ✓ HEALTHY
```

---

### 2. Collaboration Pattern Detection (Quantified)

```
Map who worked with whom and QUANTIFY collaboration time.

For EACH interaction, categorize and time:
- Solo work: X hours (person working alone)
- Collaborative work: Y hours (multiple people actively engaged on same problem)
- Cross-level collaboration: Z hours (junior + senior working together)

Present as:

COLLABORATION TIME BREAKDOWN:
[Person A]:
- Solo: X hours (Y% of time)
- Collaborative: Z hours (W% of time)
- Cross-level: V hours (U% of time)

TEAM COLLABORATION KPIs:
- Total collaborative hours: X
- Cross-level collaborative hours: Y
- Collaboration ratio: Z% of total time (target: >30%)

Count of collaboration instances: N (target: >5 per workflow)
```

---

### 3. Skill Yield Analysis (Quantified - CRITICAL KPI)

```
For EACH person's work, categorize time spent and calculate PERCENTAGES:

- HIGH SKILL YIELD: Complex + Collaborative = X% of time
- MEDIUM SKILL YIELD: Complex + Solo = Y% of time
- LOW SKILL YIELD: Routine + Collaborative = Z% of time
- MINIMAL SKILL YIELD: Routine + Solo = W% of time

Also extract:
- Hours in high-yield work (for monthly tracking)
- Count of distinct learning opportunities

Present as KPI-ready format:

[Person Name]:
- HIGH yield: X% (Y hours)
- MEDIUM yield: Z% (W hours)
- LOW yield: V% (U hours)
- MINIMAL yield: T% (S hours)

Learning opportunities: N count

SKILL DEVELOPMENT SCORE: X% high + (0.5 × Y% medium) = Z%
Target: >60% for skill development

TEAM AGGREGATE:
- Avg skill development score: X%
- Total high-yield hours: Y hours
- Learning opportunities per person: Z count
```

**Example Output (Quantified for KPIs):**

```
Jordan (Junior Engineer):
- HIGH yield: 70% (3.5 hours)
- MEDIUM yield: 20% (1 hour)
- LOW yield: 5% (0.25 hours)
- MINIMAL yield: 5% (0.25 hours)

Learning opportunities: 3 count (pairing, UTF-8 bug, streaming issue)

Skill development score: 70% + (0.5 × 20%) = 80% ✓ EXCELLENT

Monthly KPI tracking:
Jordan's high-yield %: 70% (target: >60%) ✓
Learning moments/workflow: 3 (target: >2) ✓
```

---

### 4. Expertise Application (Quantified)

```
Identify moments where someone applied specialized expertise.

For EACH instance, extract:
- Duration (time spent applying expertise: IN HOURS or MINUTES)
- Complexity rating (1-3 scale)
- Solo vs. collaborative (TAG)
- Impact (did it unblock work, prevent errors, accelerate delivery?)

Present as:

EXPERTISE EVENTS:
[Person A] applied [expertise type]:
- Duration: X hours
- Complexity: Y (scale 1-3)
- Mode: Solo / Collaborative
- Impact: [describe + quantify if possible]

EXPERTISE METRICS:
- Total expertise application time: X hours
- Average complexity: Y (scale 1-3)
- Collaborative expertise %: Z%

KPI: Expertise utilization = X hours / total work hours = Y%
Target: >50% for senior roles
```

---

### 5. Collaboration Across Experience Levels (Quantified - KEY KPI)

```
Find ALL instances where people of different experience levels worked together on same problem.

For EACH instance, extract QUANTIFIED data:
- Duration (IN HOURS or MINUTES - for time investment tracking)
- Problem complexity (RATE 1-3)
- Response time if async (IN MINUTES - for mentor availability KPI)
- Mode (paired/async review/real-time problem-solving)

Present as:

CROSS-LEVEL COLLABORATION INSTANCES:
Instance #1: [Senior] + [Junior]
- Problem: [description]
- Duration: X hours
- Complexity: Y (scale 1-3)
- Mode: [Paired work / Async review / Real-time Slack]
- Response time: Z minutes (if async)

AGGREGATE KPIs:
- Cross-level collab count: N instances (target: >2 per workflow)
- Total pairing time: X hours
- Avg problem complexity: Y (scale 1-3)
- Avg response time: Z minutes (target: <30 min for teaching moments)
- Senior time investment: W hours (X% of senior's time)

MONTHLY TRACKING:
Cross-level collaborations: N count
Junior learning hours: X hours
Senior teaching investment: Y% of time (target: >10%)
```

**Example Output (Quantified):**

```
Instance #1: Alex (Senior) + Jordan (Junior)
- Problem: Query architecture refactoring
- Duration: 3 hours (paired programming session)
- Complexity: 3 (novel architecture problem)
- Mode: Synchronous pairing

Instance #2: Alex + Jordan
- Problem: CSV streaming memory issue
- Duration: 15 minutes
- Complexity: 2 (moderate technical problem)
- Mode: Async Slack + code review
- Response time: 25 minutes

Instance #3: Alex + Jordan
- Problem: UTF-8 encoding bug
- Duration: 15 minutes
- Complexity: 2
- Mode: Real-time Slack problem-solving
- Response time: 15 minutes

AGGREGATE KPIs:
- Cross-level collab count: 3 instances ✓ (target: >2)
- Total pairing time: 3.5 hours
- Avg complexity: 2.3 (moderate-to-complex)
- Avg response time: 20 minutes ✓ (target: <30 min)
- Senior teaching investment: 3.5 hours (30% of Alex's time on this workflow)

Monthly tracking shows: Healthy senior→junior knowledge transfer
```

---

### 6. Problem-Solving vs. Execution (Quantified)

```
Distinguish between problem-solving (figuring out what to do) and execution (implementing what's decided).

For EACH person, calculate TIME SPENT:
- Problem-solving: X hours (Y% of time)
- Execution: Z hours (W% of time)

When problem-solving occurred, was it:
- Solo: X hours
- Collaborative: Y hours

Present as:

[Person A]:
- Problem-solving: X hours (Y%)
  - Solo: Z hours
  - Collaborative: W hours
- Execution: V hours (U%)

PROBLEM-SOLVING RATIO KPI: Y% (target varies by role)
- Seniors: target >60% problem-solving
- Mid-level: target 40-60%
- Juniors: target 20-40% (learning through execution)

TEAM AGGREGATE:
Avg problem-solving time: X% (track monthly)
```

---

### 7. Routine Work Allocation (Quantified)

```
Identify ALL routine, low-complexity work in this workflow.

For EACH routine task, extract:
- Who did it + their role/seniority
- Time consumed (IN HOURS)
- Automation potential (HIGH / MEDIUM / LOW)
- Opportunity cost (could this person's time be better spent?)

Present as:

ROUTINE WORK INVENTORY:
Task #1: [description]
- Who: [Person + role]
- Time: X hours
- Automation potential: HIGH/MEDIUM/LOW
- Appropriate allocation? YES/NO

ROUTINE WORK KPIs:
- Total routine work time: X hours (Y% of workflow)
- Senior time on routine work: Z hours (W% of senior capacity) ← WASTE METRIC
- Automatable routine work: V hours (U% of total)

TARGET: <30% of senior time on routine work
TARGET: >50% of routine work automatable
```

---

### 8. Knowledge Integration Points (Quantified)

```
Find moments where different types of expertise/knowledge had to be integrated.

For EACH integration point, extract:
- Types of expertise involved (list)
- Duration of integration (IN HOURS)
- Mode: Implicit (one person with multiple skills) vs. Explicit (people collaborating)
- Problem complexity (RATE 1-3)
- Integration success (was knowledge actually integrated or did gaps remain?)

Present as:

KNOWLEDGE INTEGRATION EVENTS:
Event #1:
- Expertise types: [e.g., Frontend + Backend + Product]
- Duration: X hours
- Mode: Explicit collaboration
- Complexity: Y (scale 1-3)
- Success: YES/NO

INTEGRATION KPIs:
- Integration event count: N (target: >2 per complex workflow)
- Avg integration time: X hours
- Successful integrations: Y count (Z%)
- Failed/missing integrations: W count (opportunity for improvement)
```

---

### 9. Challenge Level Assessment (Quantified)

```
For EACH person, assess whether work was appropriately challenging.

Categorize their time:
- STRETCHED: X% (working at edge of capability - high learning)
- COASTING: Y% (working well within capability - low learning)
- OVERWHELMED: Z% (beyond capability without support - risky)

Use these signals:
- Requests for help (COUNT)
- Errors/rework (COUNT)
- Time spent on tasks relative to experience
- Problem complexity vs. skill level

Present as:

[Person A]:
- STRETCHED: X% of time (Y hours)
- COASTING: Z% of time (W hours)
- OVERWHELMED: V% of time (U hours)

Evidence:
- Help requests: N count
- Errors requiring rework: M count
- Avg problem complexity: P (vs. skill level Q)

OPTIMAL CHALLENGE KPI: X% stretched (target: 30-50% for growth)

TEAM AGGREGATE:
- Avg stretched time: X% (track monthly)
- Overwhelmed instances: Y count (target: 0)
```

---

### 10. Collaboration Quality (Quantified)

```
For collaborative work (multiple people on same problem), assess quality and QUANTIFY.

For EACH collaboration, extract:
- Duration (IN HOURS)
- Problem complexity (RATE 1-3)
- Expertise diversity (COUNT: how many different types involved?)
- Engagement level (HIGH/MEDIUM/LOW - based on evidence of joint problem-solving)

Calculate:
- High-value collaborations: X count (complex problem + diverse expertise)
- Low-value collaborations: Y count (routine coordination)
- Wasted collaboration time: Z hours (low-value meetings/discussions)

Present as:

COLLABORATION QUALITY:
High-value collaborations: N count
- Total time: X hours
- Avg complexity: Y (scale 1-3)
- Avg expertise diversity: Z types per collaboration

Low-value collaborations: M count
- Total time: W hours (opportunity to eliminate)

COLLABORATION EFFICIENCY KPI:
High-value time / Total collab time = X% (target: >60%)

Monthly tracking: Are collaborations meaningful or just coordination overhead?
```

---

## EXAMPLE: BEFORE vs. AFTER (Qualitative vs. Quantitative)

### ❌ Qualitative Analysis (NOT useful for KPIs):

**Process:**
> "The workflow took a while and there were some delays waiting for approvals. People had to hand work off multiple times which slowed things down."

**Skills:**
> "The junior engineer learned from the senior engineer. They worked together on some complex problems."

**Problem:** No numbers. Can't track month-over-month. Can't set targets. Can't measure AI impact.

---

### ✅ Quantitative Analysis (READY for KPI dashboard):

**Process:**
> - Cycle time: 15 days
> - Wait time: 74% (11 days)
> - Active work: 26% (4 days)
> - Approval bottleneck: 6 days (40% of cycle)
> - Handoffs: 8 count
> - Target: Reduce approval delay to <3 days, reduce wait time to <50%

**Skills:**
> - Jordan (Junior): 70% high skill yield, 3 learning moments
> - Cross-level collaboration: 3 instances, 3.5 hours
> - Avg problem complexity: 2.3/3.0
> - Senior teaching investment: 30% of Alex's time
> - Target: Maintain >60% high skill yield after AI deployment

**This enables KPI tracking:** Measure these numbers monthly. Deploy AI. Measure again. Did efficiency improve WITHOUT degrading skill development?

---

## TIPS FOR EFFECTIVE QUANTIFIED ANALYSIS

**Start with baseline establishment:**
1. Analyze 2-3 workflows BEFORE any changes
2. Extract quantified metrics from each
3. Average them to establish baseline KPIs
4. Set improvement targets

**Track consistently:**
- Use same prompts monthly (don't change wording)
- Analyze similar workflow types (apples-to-apples)
- Document any process changes that might affect metrics

**Combine quantitative + qualitative:**
- Numbers show WHERE problems are
- Qualitative context explains WHY
- Together they reveal WHAT to do

**Compare to surveys:**
- Surveys: "Do you feel productive?" → 8/10
- Data: "Cycle time unchanged, but work shifted routine" → Reality check
- THIS is why measurement matters

---

## BUILDING YOUR KPI DASHBOARD

After using these prompts on 2-3 workflows, create your tracking dashboard:

### Process Efficiency KPIs

| Metric | Baseline | Month 1 | Month 2 | Month 3 | Target |
|--------|----------|---------|---------|---------|--------|
| Avg Cycle Time (days) | 15 | ? | ? | ? | <10 |
| Wait Time % | 74% | ? | ? | ? | <50% |
| Handoff Count | 8 | ? | ? | ? | <5 |
| Approval Delay (days) | 6 | ? | ? | ? | <3 |
| Time to First Response (hrs) | 7 | ? | ? | ? | <4 |

### Skill Development KPIs

| Metric | Baseline | Month 1 | Month 2 | Month 3 | Target |
|--------|----------|---------|---------|---------|--------|
| Team Avg High Skill Yield % | 65% | ? | ? | ? | >60% |
| Cross-Level Collab (count) | 3 | ? | ? | ? | >2 |
| Junior Learning Hours/Week | 3.5 | ? | ? | ? | >3 |
| Avg Problem Complexity (1-3) | 2.3 | ? | ? | ? | >2.0 |
| Senior Teaching Investment % | 30% | ? | ? | ? | >10% |

**Before deploying AI:** Establish baselines
**After deploying AI:** Measure monthly
**The question:** Did we gain efficiency WITHOUT sacrificing skill development?

---

## COMMON INSIGHTS TO LOOK FOR

**Process red flags (QUANTIFIED):**
- Wait time > 50% of cycle time
- Handoff count > 5 per workflow
- Approval overhead > 15% of cycle time
- Response time > 4 hours

**Skill red flags (QUANTIFIED):**
- High skill yield time < 40%
- Cross-level collaboration < 2 instances per workflow
- Avg problem complexity < 1.5 (work too routine)
- Senior time on routine work > 30%

---

END OF PROMPT LIBRARY
