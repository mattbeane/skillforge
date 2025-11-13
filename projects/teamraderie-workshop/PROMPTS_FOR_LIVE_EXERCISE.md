# PROMPTS FOR LIVE EXERCISE
**Copy-paste these into Claude/ChatGPT along with the sample workflow data**

---

## SETUP PROTOCOL (READ THIS FIRST!)

**To ensure consistent results across your team:**

1. **Start a NEW conversation** (Don't use existing chat with prior context)
2. **First, paste this system message:**

```
You are a workflow analyst providing quantitative metrics.
Rules:
- Provide EXACT numbers only (no ranges like "2-3 days" - pick one)
- Show your date/time calculations explicitly (e.g., "Sept 25 to Oct 10 = 15 days")
- If data is ambiguous, state your assumption and proceed
- Follow the output format template exactly
```

3. **Then paste your chosen prompt** (Process or Skill)
4. **Then paste the workflow data**
5. **Verify your output** using the checklist at the bottom

---

## OPTION A: PROCESS ANALYSIS

### Prompt #1: Cycle Time Extraction (Quantified KPIs)

```
Analyze this workflow data and extract QUANTIFIED metrics:

1. Total elapsed time from start to completion (IN DAYS)
2. Active work time vs wait time (AS PERCENTAGES and IN DAYS)
3. Number of handoffs (COUNT - each time work passes between people/teams)
4. Approval/decision delays (IN DAYS for each delay)
5. Time to first response (IN HOURS - initial request to first action)

IMPORTANT CONSTRAINTS:
- Show date calculations explicitly (e.g., "Sept 25 to Oct 10 = 15 days")
- Provide EXACT numbers, not ranges
- If multiple interpretations exist, pick the most conservative
- Percentages must add to 100%
- Use this EXACT output format:

CYCLE TIME METRICS:
- Total cycle time: X days [show calculation: start date to end date]
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

---

## OPTION B: SKILL ANALYSIS

### Prompt #1: Collaboration Pattern Analysis (Quantified)

```
Analyze this workflow data to identify SKILL DEVELOPMENT patterns.

Extract these QUANTIFIED metrics:

1. Collaboration instances (COUNT - how many times did people work together on complex problems)
2. Cross-level mentoring (COUNT - senior helping junior on technical challenges)
3. Knowledge transfer moments (LIST specific examples with timestamps)
4. Complex problem-solving (vs routine work) - estimate PERCENTAGE of time
5. Solo vs collaborative time - AS PERCENTAGES

IMPORTANT CONSTRAINTS:
- Provide EXACT counts (not "several" or "multiple")
- Cite specific timestamps/quotes from the data for each example
- Percentages must add to 100%
- Use this EXACT output format:

COLLABORATION METRICS:
- Cross-level mentoring instances: N count [cite each: timestamp, who → who]
- Knowledge transfer moments: M count [list below with timestamps]
- Complex collaborative work: X% of total time
- Complex solo work: Y% of total time
- Routine work: Z% of total time

SKILL DEVELOPMENT SIGNALS:
1. [Person A] → [Person B]: [What was learned] [Timestamp]
2. [Person A] → [Person B]: [What was learned] [Timestamp]

SKILL YIELD ASSESSMENT:
- High skill yield time (complex + collaborative): X%
- Medium skill yield time (complex + solo): Y%
- Low skill yield time (routine): Z%

KPI TARGETS:
- High skill yield time: >30% (optimal for skill development)
- Cross-level mentoring: >2 instances per workflow
- Knowledge transfer: >3 teaching moments per workflow
```

---

## HOW TO USE

**Step 1:** Copy the workflow data from "SAMPLE_DATA_FOR_PARTICIPANTS.md"

**Step 2:** Open Claude.ai or ChatGPT

**Step 3:** Paste this structure:

```
[PASTE YOUR CHOSEN PROMPT HERE]

Here is the workflow data to analyze:

[PASTE THE SAMPLE WORKFLOW DATA HERE]
```

**Step 4:** Hit enter and extract 2-3 key metrics to share

**Step 5:** Verify your output using the checklist below

**You have 10 minutes!**

---

## VERIFICATION CHECKLIST

**Before sharing your results, verify your AI output includes:**

### For Process Analysis (Cycle Time):
- [ ] Total cycle time in DAYS (specific number, not range)
- [ ] Date calculation shown (e.g., "Sept 25 to Oct 10 = 15 days")
- [ ] Active work as BOTH percentage AND days
- [ ] Wait time as BOTH percentage AND days
- [ ] Active % + Wait % = 100%
- [ ] Handoff count as INTEGER (not "approximately")
- [ ] Time to first response in HOURS

### For Skill Analysis (Collaboration):
- [ ] Cross-level mentoring count as INTEGER
- [ ] Each mentoring instance cited with timestamp
- [ ] Knowledge transfer moments listed with specific examples
- [ ] All percentages add to 100%
- [ ] Complex collaborative % + Complex solo % + Routine % = 100%

### If anything is missing or ambiguous:
**Re-prompt:** "Please provide [specific metric] as [specific format with units]"

**Example:** "Please provide the total cycle time as an exact number of days with date calculation shown."

---

## TROUBLESHOOTING

**Problem:** Output says "approximately" or gives ranges
**Solution:** Re-prompt: "Provide exact numbers only. Pick the single most likely value."

**Problem:** Output is narrative/paragraph format
**Solution:** Re-prompt: "Use the KPI format template from the original prompt exactly."

**Problem:** Calculations don't match the dates in your data
**Solution:** Show the AI the error: "The data shows Sept 25 to Oct 10, which is 15 days, not 14 days. Please recalculate."

**Problem:** Different team members got very different numbers
**Solution:** Compare your data inputs - did you paste the same workflow data? Check if one person's AI missed key sections.
