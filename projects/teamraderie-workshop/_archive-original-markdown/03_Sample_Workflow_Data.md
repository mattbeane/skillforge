# SAMPLE WORKFLOW DATA SET
## Software Feature Request to Customer Deployment

**Workshop: Measure Twice, Spend Once**

---

## PURPOSE OF THIS DOCUMENT

This sample workflow shows a realistic scenario with all the artifacts (emails, Slack messages, meeting notes) that teams generate during normal work. You can use this data to:

1. **Practice using the AI prompts** before analyzing your own workflows
2. **See what "workflow data" looks like** in practice
3. **Understand what insights are possible** from this type of analysis
4. **Demonstrate the workshop** to others

---

## SCENARIO OVERVIEW

**Context:** A mid-size SaaS company receives a feature request from an enterprise customer. This data set shows the workflow from initial request through deployment.

**Timeline:** Monday, September 25 → Tuesday, October 10 (15 days total)

**People involved:**
- Sarah Chen - Customer Success Manager
- Marcus Rodriguez - Product Manager
- Alex Kim - Senior Engineer
- Jordan Lee - Junior Engineer
- Jennifer & Tom - Customer (Acme Corp)

**Outcome:** Feature built and deployed, customer expansion secured

---

## ARTIFACT 1: Initial Email Thread

**From:** Sarah Chen (Customer Success Manager)  
**To:** Product Team <product@company.com>  
**Date:** Monday, September 25, 9:15 AM  
**Subject:** Enterprise Customer Feature Request - Dashboard Export

Hi team,

Acme Corp (our $500K account) is requesting the ability to export dashboard data to CSV. Their analyst team currently screenshots dashboards and manually re-enters data into Excel for their weekly executive reports.

They mentioned this is blocking a potential expansion to 50 more seats. Current contract renewal is in 90 days.

Priority level from my perspective: High

What's the feasibility and timeline?

Thanks,
Sarah

---

**From:** Marcus Rodriguez (Product Manager)  
**To:** Sarah Chen  
**Cc:** Product Team  
**Date:** Monday, September 25, 4:30 PM  

Sarah,

Thanks for this. Need to understand the requirement better. Can you set up a call with their analyst team so we can understand:
- What data specifically do they need
- What format works for them
- How often they do this
- What their downstream process looks like

Also looping in @Dev Team to start thinking about technical approach.

Marcus

---

**From:** Sarah Chen  
**To:** Marcus Rodriguez  
**Date:** Tuesday, September 26, 10:00 AM  

Call scheduled for Thursday 2 PM with their team. I'll send invite.

---

## ARTIFACT 2: Slack Conversation (Engineering Channel)

**Marcus** [Tuesday, September 26, 4:35 PM]  
Hey @Dev Team - got a customer request for dashboard CSV export. Thoughts on lift? Is this something we've architected for?

**Alex Kim (Senior Engineer)** [Tuesday, September 26, 5:20 PM]  
We talked about this 6 months ago but punted. Current dashboard rendering is all client-side React. We'd need to either:
1. Duplicate the query logic server-side to generate CSVs
2. Build an export service that can scrape the rendered dashboard
3. Refactor to have a shared data layer

Option 1 is probably a few days of work but creates tech debt (two places to maintain query logic). Option 3 is the "right" way but that's a 2-3 week project.

**Jordan Lee (Junior Engineer)** [Tuesday, September 26, 5:45 PM]  
I could take a first pass at option 1? I've been wanting to learn the query builder architecture.

**Alex Kim** [Tuesday, September 26, 6:10 PM]  
Let's wait til we hear what they actually need on Thursday. Might be simpler than we think.

**Marcus** [Tuesday, September 26, 6:15 PM]  
Agreed. I'll update after customer call.

---

## ARTIFACT 3: Meeting Notes (Customer Call)

**Date:** Thursday, September 28, 2:00 PM  
**Attendees:** Sarah (CS), Marcus (PM), Alex (Eng), Jennifer from Acme Corp (Data Analyst), Tom from Acme Corp (VP Operations)

**Marcus:** Can you walk us through your current process?

**Jennifer:** Every Monday I screenshot 8 dashboards, then manually type the numbers into an Excel template. Takes about 3 hours. Then I add some pivot tables and charts and email to Tom and his leadership team.

**Tom:** The issue is we can't audit the data or drill into it. If a number looks off, Jennifer has to go back to the dashboard, investigate, then send us an update. We also can't slice the data different ways without asking her to pull it again.

**Alex:** What if instead of CSV export, we gave you API access to pull the underlying data? You could automate the whole pipeline.

**Tom:** We don't have engineering resources. Our analyst team knows Excel, not APIs.

**Jennifer:** Could I get the raw data somehow? Even if it's ugly, I can clean it in Excel.

**Marcus:** What's your ideal state?

**Tom:** Click a button, download the data behind each dashboard as CSV, open in Excel, done. If you gave us that, we'd probably buy 50 more seats by end of quarter.

**Marcus:** Got it. Let us evaluate options and I'll get back to you by Monday with timeline.

---

## ARTIFACT 4: Slack Conversation (After Customer Call)

**Marcus** [Thursday, September 28, 3:45 PM]  
@Alex @Jordan - customer is pretty clear. Just wants CSV download from each dashboard. No API needed. Thoughts on implementation path?

**Alex** [Thursday, September 28, 4:10 PM]  
OK so actually simpler than the full export service. We just need a "download CSV" button on each dashboard that hits an endpoint. Endpoint would need to:
1. Accept dashboard ID + current filters
2. Run the same query the dashboard uses
3. Format as CSV
4. Return for download

That's probably 2-3 days of focused work. The tricky part is we'd be duplicating query logic from the frontend.

**Jordan** [Thursday, September 28, 4:25 PM]  
What if we extract the query builder into a shared module that both frontend and backend can use? Then we're not duplicating.

**Alex** [Thursday, September 28, 5:00 PM]  
That's actually smart. Adds maybe a day but solves the tech debt problem. You want to pair on this? I can show you the query architecture and we can refactor together, then you build the CSV endpoint.

**Jordan** [Thursday, September 28, 5:15 PM]  
Yes! When can we start?

**Alex** [Thursday, September 28, 5:20 PM]  
Tomorrow morning. Block your calendar 9-12, we'll get the refactor done. Then you can build the CSV endpoint Monday-Tuesday.

**Marcus** [Thursday, September 28, 5:25 PM]  
Perfect. So we're looking at done by Wednesday? I'll tell Sarah we can commit to end of next week to give us buffer.

**Alex** [Thursday, September 28, 5:30 PM]  
Yep, EOW is safe.

---

## ARTIFACT 5: Slack Conversation (Implementation Week)

**Jordan** [Friday, September 29, 3:30 PM]  
@Alex - got the shared query module refactored and working. Frontend tests passing. Ready to start the CSV endpoint Monday.

**Alex** [Friday, September 29, 4:00 PM]  
Nice work. One thing I noticed in your PR - you're loading all results into memory before writing CSV. If someone has a huge dataset that'll crash. Can you stream the results instead?

**Jordan** [Friday, September 29, 4:30 PM]  
Oh good catch. I'll look up streaming CSV in Node and revise.

**Alex** [Friday, September 29, 4:45 PM]  
Here's a library we use elsewhere: [link]. Check out the billing export feature for example usage. Ping me Monday if you get stuck.

---

**Jordan** [Monday, October 2, 2:15 PM]  
@Alex - CSV endpoint working with streaming. But I'm getting weird encoding issues with special characters. The test data with "café" comes out as "cafÃ©"

**Alex** [Monday, October 2, 2:45 PM]  
UTF-8 BOM issue. Add this to your response headers: [code snippet]

**Jordan** [Monday, October 2, 3:00 PM]  
That fixed it! Running through all the dashboards now to test.

---

**Jordan** [Tuesday, October 3, 11:00 AM]  
@Marcus @Alex - Feature deployed to staging. All 15 dashboards have working CSV export. Ready for Sarah to show the customer.

**Marcus** [Tuesday, October 3, 11:30 AM]  
Awesome. @Sarah can you demo this for Acme Corp today or tomorrow?

---

## ARTIFACT 6: Email Thread (Customer Demo)

**From:** Sarah Chen  
**To:** Tom (Acme Corp)  
**Date:** Wednesday, October 4, 9:00 AM  
**Subject:** Dashboard Export - Ready for Testing

Tom,

We've built the CSV export feature you requested. It's ready for you to test: [staging link]

Each dashboard now has a "Download CSV" button that gives you the raw data with all current filters applied.

Can you and Jennifer test it out and let me know if this meets your needs?

Thanks,
Sarah

---

**From:** Tom (Acme Corp)  
**To:** Sarah Chen  
**Date:** Wednesday, October 4, 2:15 PM  

Sarah,

Jennifer tested it - works perfectly. Exactly what we needed. How soon can this be in production?

If we can get this by end of month, I'll push through the expansion order for 50 seats.

Tom

---

**From:** Sarah Chen  
**To:** Marcus Rodriguez  
**Date:** Wednesday, October 4, 2:30 PM  

Marcus - customer loves it and will expand if we ship by EOM. Can we make that happen?

---

**From:** Marcus Rodriguez  
**To:** Sarah Chen, Alex Kim  
**Date:** Wednesday, October 4, 3:00 PM  

@Alex - can we ship this week?

---

**From:** Alex Kim  
**To:** Marcus Rodriguez, Sarah Chen  
**Date:** Wednesday, October 4, 4:00 PM  

Needs QA cycle and prod deploy approval. Earliest is Monday but probably Tuesday to be safe. Will that work?

---

**From:** Sarah Chen  
**To:** Tom (Acme Corp)  
**Date:** Wednesday, October 4, 4:30 PM  

Tom - we'll have this in production by Tuesday, Oct 10. Will that work for your timeline?

---

**From:** Tom (Acme Corp)  
**To:** Sarah Chen  
**Date:** Wednesday, October 4, 5:00 PM  

Perfect. I'll start the expansion paperwork now. Thanks for the quick turnaround.

---

## ARTIFACT 7: Slack Message (Deployment)

**Alex** [Tuesday, October 10, 10:30 AM]  
@Marcus @Sarah - CSV export is live in production. All dashboards tested and working.

**Sarah** [Tuesday, October 10, 10:45 AM]  
Customer notified. Thank you @Alex and @Jordan!

**Jordan** [Tuesday, October 10, 11:00 AM]  
🎉

---

## SUMMARY DATA

**Total elapsed time:** 15 calendar days (Sept 25 - Oct 10)

**Key milestones:**
- Initial request to PM response: 7 hours (wait time)
- PM response to customer call scheduled: 2 days (wait time)
- Customer call to implementation start: 1 day (decision time)
- Implementation (paired work): 3 days (active work)
- Staging deployment to customer test: 1 day (coordination)
- Customer test to production deployment: 6 days (QA + approval wait)

**People and roles:**
- Sarah: Customer interface, coordination
- Marcus: Requirements gathering, priority setting
- Alex: Senior technical guidance, code review, mentoring
- Jordan: Implementation, learning

---

## PRACTICE EXERCISE

Use the AI prompts from the Prompt Library on this data to answer:

**Process questions:**
1. What was the total cycle time breakdown (active vs. wait)?
2. What were the main bottlenecks?
3. Where was value created vs. where did work stall?

**Skill questions:**
1. How much time was spent in complex collaborative work?
2. Where did skill development happen?
3. Who learned what from whom?

**Strategic questions:**
1. Where could AI speed up this workflow without harming skill development?
2. What metrics would prove the intervention worked?

---

END OF SAMPLE DATA SET
