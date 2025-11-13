# Replit Agent Instructions: Update Measure Twice Spend Once Website
**Site:** measuretwicespendonce.com  
**Task:** Improve prompt consistency and add usage guidelines

---

## Overview

The workshop prompts need three critical additions to improve consistency across users:
1. **Setup Protocol** - Instructions to reduce LLM output variance
2. **Constraint Instructions** - Tighter prompt specifications
3. **Verification & Troubleshooting** - Post-analysis validation

---

## File to Modify

**File:** `prompts.html`  
**Sections to update:** 2 prompts (Cycle Time + Collaboration Pattern)  
**New sections to add:** Setup Protocol, Verification Checklist, Troubleshooting

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

## PART 2: Update Prompt #1 (Cycle Time Extraction)

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

## PART 3: Update Prompt #3 (Collaboration Pattern Analysis)

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

## PART 4: Add Verification & Troubleshooting Section

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

## PART 5: Add CSS for New Elements

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
2. **Test prompt updates:** Copy Prompt #1 and #3 - verify IMPORTANT CONSTRAINTS section is included
3. **Test verification section:** Scroll to bottom - ensure checklists display in 2-column grid
4. **Test troubleshooting:** Verify all 4 problem/solution boxes display correctly
5. **Test on mobile:** Ensure 2-column layouts stack appropriately on narrow screens

---

## Expected Outcome

Users will see:
1. Clear setup instructions BEFORE they start (reduces variance from context contamination)
2. Tighter prompt constraints (forces exact numbers, explicit calculations)
3. Post-analysis validation checklist (catches missing/ambiguous outputs)
4. Troubleshooting guidance (helps debug divergent results)

This should dramatically improve consistency across workshop participants without requiring any backend infrastructure.

---

## Notes for Replit Agent

- Preserve all existing HTML structure and navigation
- Don't modify other prompts (#2, #4-18) - only update #1 and #3 as specified
- Keep all existing CSS classes and styling
- Maintain existing JavaScript for copy functionality
- Test that "Copy Prompt" buttons still work after changes
