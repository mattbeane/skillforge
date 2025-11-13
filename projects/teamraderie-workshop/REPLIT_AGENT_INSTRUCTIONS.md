# Replit Agent Instructions: Update Measure Twice Spend Once Website
**Site:** measuretwicespendonce.com  
**Task:** Improve prompt consistency and add usage guidelines

---

## Overview

The workshop prompts need four critical additions to improve consistency across users:
1. **Setup Protocol** - Instructions to reduce LLM output variance
2. **Multi-Run Protocol** - Method for running 3-5 iterations to measure variance and improve result confidence
3. **Constraint Instructions** - Tighter prompt specifications
4. **Verification & Troubleshooting** - Post-analysis validation

---

## File to Modify

**File:** `prompts.html`
**Sections to update:** 2 prompts (Cycle Time + Collaboration Pattern)
**New sections to add:** Setup Protocol, Multi-Run Protocol, Verification Checklist, Troubleshooting

---

## PART 1: Add Setup Protocol Section

**Location:** Insert AFTER line 98 (after the "How to Use These Prompts" section) and BEFORE the section-nav div (line 100)

**HTML to add:**

```html
        <section class="setup-protocol" style="background: #FFF3CD; border-left: 4px solid #FFC107; padding: 1.5rem; margin: 2rem 0; border-radius: 4px;">
            <h3 style="color: #856404; margin-top: 0;">⚠️ Setup Protocol (Read This First!)</h3>
            <p style="color: #856404;"><strong>To ensure consistent results across your team:</strong></p>
            <ol style="color: #856404;">
                <li><strong>Start a NEW conversation</strong> (Don't use existing chat with prior context)</li>
                <li><strong>First, paste this system message:</strong>
                    <div style="background: white; padding: 1rem; border-radius: 4px; margin: 0.5rem 0; border: 1px solid #ddd;">
                        <code style="display: block; white-space: pre-wrap;">You are a workflow analyst providing quantitative metrics.
Rules:
- Provide EXACT numbers only (no ranges like "2-3 days" - pick one)
- Show your date/time calculations explicitly (e.g., "Sept 25 to Oct 10 = 15 days")
- If data is ambiguous, state your assumption and proceed
- Follow the output format template exactly</code>
                    </div>
                </li>
                <li><strong>Then paste your chosen prompt</strong> (Process or Skill)</li>
                <li><strong>Then paste the workflow data</strong></li>
                <li><strong>Verify your output</strong> using the checklist at the bottom of this page</li>
            </ol>
        </section>
```

---

## PART 2: Add Multi-Run Protocol Section

**Location:** Insert AFTER the Setup Protocol section (after the yellow warning box from Part 1) and BEFORE the section-nav div

**Why this matters:** Running prompts 3-5 times reveals natural variance in AI outputs and provides more defensible results for business decisions.

**HTML to add:**

```html
        <section class="multi-run-protocol" style="background: #E8F4F8; border-left: 4px solid #0288D1; padding: 1.5rem; margin: 2rem 0; border-radius: 4px;">
            <h3 style="color: #01579B; margin-top: 0;">🔄 Recommended: Run Analysis 3-5 Times</h3>
            <p style="color: #01579B;"><strong>Why run multiple times?</strong></p>
            <ul style="color: #01579B;">
                <li><strong>See variance in real-time:</strong> AI outputs vary even with identical inputs - you'll observe this firsthand</li>
                <li><strong>Get more defensible results:</strong> "Cycle time averaged 14.7±1.2 days across 5 runs" beats "Cycle time is 15 days"</li>
                <li><strong>Catch outliers:</strong> If one run gives wildly different results, you'll spot data interpretation issues</li>
                <li><strong>Build confidence:</strong> Consistent results across runs = trustworthy metrics</li>
            </ul>

            <h4 style="color: #01579B; margin-top: 1.5rem;">How to do it:</h4>
            <ol style="color: #01579B;">
                <li>Complete your first analysis following the Setup Protocol above</li>
                <li>Record results in the comparison template below</li>
                <li>Click "New Conversation" in your AI tool</li>
                <li>Repeat steps 1-3 for a total of 3-5 runs</li>
                <li>Compare results - look for consistency and outliers</li>
            </ol>

            <div style="background: white; padding: 1.5rem; border-radius: 6px; margin-top: 1rem;">
                <h4 style="margin-top: 0;">Results Comparison Template</h4>
                <p>Copy this table and fill in your results from each run:</p>
                <pre style="background: #f5f5f5; padding: 1rem; border-radius: 4px; overflow-x: auto; font-size: 0.9em;">
<strong>PROCESS METRICS (Cycle Time Analysis):</strong>

| Metric                    | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Average | Notes |
|---------------------------|-------|-------|-------|-------|-------|---------|-------|
| Total cycle time (days)   |       |       |       |       |       |         |       |
| Active work %             |       |       |       |       |       |         |       |
| Wait time %               |       |       |       |       |       |         |       |
| Handoff count             |       |       |       |       |       |         |       |
| Time to first resp (hrs)  |       |       |       |       |       |         |       |

<strong>SKILL METRICS (Collaboration Analysis):</strong>

| Metric                    | Run 1 | Run 2 | Run 3 | Run 4 | Run 5 | Average | Notes |
|---------------------------|-------|-------|-------|-------|-------|-------|-------|
| Mentoring instances       |       |       |       |       |       |         |       |
| Knowledge transfer moments|       |       |       |       |       |         |       |
| Complex collaborative %   |       |       |       |       |       |         |       |
| Complex solo %            |       |       |       |       |       |         |       |
| Routine work %            |       |       |       |       |       |         |       |

<strong>VARIANCE CHECK:</strong>
- Highest cycle time: ___ days
- Lowest cycle time: ___ days
- Range: ___ days (if >20% of average, investigate why)

<strong>WHAT THIS TELLS YOU:</strong>
- Low variance (values cluster tightly) = Metric is clear in your data
- High variance (values spread out) = Metric is ambiguous or AI is interpreting differently each time
- Outliers = Possible data quality issue or AI misinterpretation to investigate
                </pre>
            </div>

            <div style="background: #FFF9C4; padding: 1rem; border-radius: 4px; margin-top: 1rem; border: 1px solid #FBC02D;">
                <p style="margin: 0; color: #F57F17;"><strong>💡 Workshop Tip:</strong> Have team members compare their results. If variance <em>within</em> one person's runs is low but variance <em>between</em> people is high, that points to different data interpretations (not AI variance).</p>
            </div>
        </section>
```

**Note for Replit Agent:** This section teaches participants basic statistical thinking about AI variance while giving them a practical method to improve result quality during the workshop.

---

## PART 3: Update Prompt #1 (Cycle Time Extraction)

**Location:** Lines 115-143 (inside `id="prompt1"`)

**Replace existing prompt text with:**

```
Analyze this workflow data and extract QUANTIFIED cycle time metrics:

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

Here is the workflow data to analyze:

[PASTE YOUR WORKFLOW DATA HERE]
```

---

## PART 4: Update Prompt #3 (Collaboration Pattern Analysis)

**Location:** Lines 380-415 (inside `id="prompt3"`)

**Replace existing prompt text with:**

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

Here is the workflow data:

[PASTE YOUR WORKFLOW DATA HERE]
```

---

## PART 5: Add Verification & Troubleshooting Section

**Location:** Insert BEFORE the `<section class="cta-section">` (around line 752)

**HTML to add:**

```html
        <section class="content-section" style="background: #E8F4F8; padding: 2rem; border-radius: 8px; margin-top: 3rem;">
            <h2>Verification Checklist</h2>
            <p><strong>Before sharing your results, verify your AI output includes:</strong></p>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 1.5rem;">
                <div>
                    <h3 style="color: var(--skill-navy);">For Process Analysis (Cycle Time):</h3>
                    <ul class="checklist">
                        <li>☐ Total cycle time in DAYS (specific number, not range)</li>
                        <li>☐ Date calculation shown (e.g., "Sept 25 to Oct 10 = 15 days")</li>
                        <li>☐ Active work as BOTH percentage AND days</li>
                        <li>☐ Wait time as BOTH percentage AND days</li>
                        <li>☐ Active % + Wait % = 100%</li>
                        <li>☐ Handoff count as INTEGER (not "approximately")</li>
                        <li>☐ Time to first response in HOURS</li>
                    </ul>
                </div>
                
                <div>
                    <h3 style="color: var(--skill-navy);">For Skill Analysis (Collaboration):</h3>
                    <ul class="checklist">
                        <li>☐ Cross-level mentoring count as INTEGER</li>
                        <li>☐ Each mentoring instance cited with timestamp</li>
                        <li>☐ Knowledge transfer moments listed with specific examples</li>
                        <li>☐ All percentages add to 100%</li>
                        <li>☐ Complex collaborative % + Complex solo % + Routine % = 100%</li>
                    </ul>
                </div>
            </div>
            
            <div style="background: white; padding: 1.5rem; margin-top: 2rem; border-radius: 6px;">
                <h3 style="margin-top: 0;">If anything is missing or ambiguous:</h3>
                <p><strong>Re-prompt:</strong> "Please provide [specific metric] as [specific format with units]"</p>
                <p><strong>Example:</strong> "Please provide the total cycle time as an exact number of days with date calculation shown."</p>
            </div>
        </section>
        
        <section class="content-section" style="margin-top: 2rem;">
            <h2>Troubleshooting Common Issues</h2>
            
            <div class="troubleshooting-grid" style="display: grid; gap: 1.5rem; margin-top: 1.5rem;">
                <div style="background: #f8f9fa; padding: 1.5rem; border-left: 4px solid var(--skill-blue); border-radius: 4px;">
                    <h4 style="color: var(--skill-navy); margin-top: 0;">Problem: Output says "approximately" or gives ranges</h4>
                    <p><strong>Solution:</strong> Re-prompt: "Provide exact numbers only. Pick the single most likely value."</p>
                </div>
                
                <div style="background: #f8f9fa; padding: 1.5rem; border-left: 4px solid var(--skill-blue); border-radius: 4px;">
                    <h4 style="color: var(--skill-navy); margin-top: 0;">Problem: Output is narrative/paragraph format</h4>
                    <p><strong>Solution:</strong> Re-prompt: "Use the KPI format template from the original prompt exactly."</p>
                </div>
                
                <div style="background: #f8f9fa; padding: 1.5rem; border-left: 4px solid var(--skill-blue); border-radius: 4px;">
                    <h4 style="color: var(--skill-navy); margin-top: 0;">Problem: Calculations don't match the dates in your data</h4>
                    <p><strong>Solution:</strong> Show the AI the error: "The data shows Sept 25 to Oct 10, which is 15 days, not 14 days. Please recalculate."</p>
                </div>
                
                <div style="background: #f8f9fa; padding: 1.5rem; border-left: 4px solid var(--skill-blue); border-radius: 4px;">
                    <h4 style="color: var(--skill-navy); margin-top: 0;">Problem: Different team members got very different numbers</h4>
                    <p><strong>Solution:</strong> Compare your data inputs - did you paste the same workflow data? Check if one person's AI missed key sections.</p>
                </div>
            </div>
        </section>
```

---

## PART 6: Add CSS for New Elements

**Location:** Add to the `<style>` section in the `<head>` (after line 75, before `</style>`)

**CSS to add:**

```css
        .checklist {
            list-style: none;
            padding-left: 0;
        }
        .checklist li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #ddd;
        }
        .checklist li:last-child {
            border-bottom: none;
        }
```

---

## Testing Instructions

After making changes:

1. **Test Setup Protocol visibility:** Ensure yellow warning box appears prominently after "How to Use" section
2. **Test Multi-Run Protocol:** Verify blue box appears with comparison template table properly formatted
3. **Test prompt updates:** Copy Prompt #1 and #3 - verify IMPORTANT CONSTRAINTS section is included
4. **Test verification section:** Scroll to bottom - ensure checklists display in 2-column grid
5. **Test troubleshooting:** Verify all 4 problem/solution boxes display correctly
6. **Test on mobile:** Ensure 2-column layouts and tables stack appropriately on narrow screens

---

## Expected Outcome

Users will see:
1. Clear setup instructions BEFORE they start (reduces variance from context contamination)
2. Multi-run protocol with comparison template (teaches variance awareness, improves result defensibility)
3. Tighter prompt constraints (forces exact numbers, explicit calculations)
4. Post-analysis validation checklist (catches missing/ambiguous outputs)
5. Troubleshooting guidance (helps debug divergent results)

This provides a **3-tier approach to reproducibility:**
- **Tier 1 (Single run):** Setup protocol + constraints = reduced variance
- **Tier 2 (3-5 runs):** Multi-run protocol = measured variance + averaged results
- **Tier 3 (Production):** Automated N=50 platform (see workflow-analysis-platform project)

Workshop participants get immediate value from Tier 1-2 without backend infrastructure, while understanding the path to production-grade analysis.

---

## Notes for Replit Agent

- Preserve all existing HTML structure and navigation
- Don't modify other prompts (#2, #4-18) - only update #1 and #3 as specified
- Keep all existing CSS classes and styling
- Maintain existing JavaScript for copy functionality
- Test that "Copy Prompt" buttons still work after changes
