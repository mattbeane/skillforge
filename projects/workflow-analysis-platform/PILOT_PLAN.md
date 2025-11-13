# Pilot Plan: Workflow Analysis Platform

## Goals

1. **Determine optimal N** - Find point where confidence intervals stabilize
2. **Validate metric extraction** - Ensure parsing works reliably
3. **Measure cost and time** - Confirm economic viability
4. **Test with real workflows** - Use Skillbench customer data
5. **Assess business value** - Do customers find this more credible?

## Phase 1: Experimental Design (2 weeks)

### Experiment: Optimal Sample Size

**Method:**
1. Select 5 representative workflows (vary length, complexity)
2. Run each with N = 1, 5, 10, 25, 50, 100, 200
3. Measure for each N:
   - Confidence interval width
   - Coefficient of variation
   - Execution time
   - Cost

**Analysis:**
- Plot CI width vs N (find elbow/plateau)
- Calculate diminishing returns point
- Determine production default (likely N=50)

**Deliverable:** Jupyter notebook with analysis + recommendation

### Experiment: Metric Extraction Reliability

**Method:**
1. Run 100 analyses on sample workflow
2. Measure extraction success rate per metric type
3. Identify metrics needing regex refinement
4. Test fallback LLM extraction on failures

**Success Criteria:**
- >95% extraction success for all metrics
- <2% requiring manual intervention

**Deliverable:** Extraction accuracy report + updated regexes

## Phase 2: MVP Development (4 weeks)

### Core Components

**Week 1-2: Backend**
- Parallel execution engine (asyncio + OpenAI API)
- Metric extraction layer (regex + fallback)
- Statistical aggregation (numpy/scipy)
- Unit tests (>80% coverage)

**Week 3-4: Frontend**
- Streamlit app (4-tab structure)
- Upload/paste workflow data
- Progress indicators
- Results visualization (tables, distribution plots)
- Export functionality

**Deliverable:** Working Streamlit app deployable to Render/Streamlit Cloud

## Phase 3: Pilot with Customers (6 weeks)

### Pilot Participants (3-5 companies)

**Criteria:**
- Willing to share workflow data
- Currently deploying or considering AI
- Open to experimental tooling
- Represent different industries

**Candidates:**
1. Skillbench internal (dogfood first)
2. 2-3 Teamraderie workshop alumni
3. 1-2 Skillbench customers

### Pilot Structure

**Week 1: Onboarding**
- 30-min demo and training
- Help select workflows to analyze
- Set up access (Streamlit app link)

**Weeks 2-4: Active Use**
- Analyze 3-5 workflows each
- Weekly check-in calls
- Gather qualitative feedback
- Log issues/feature requests

**Weeks 5-6: Debrief**
- Structured feedback sessions
- Compare to their current measurement approach
- Assess willingness to pay
- Identify must-have features for production

### Success Metrics

**Technical:**
- Avg stability score: >75% metrics HIGH or MEDIUM
- Extraction success rate: >95%
- Avg execution time: <30 seconds (N=50)
- Cost per analysis: <$0.05

**Business:**
- Customer satisfaction: >8/10
- Perceived value vs. workshop approach: Significantly better
- Willingness to pay: >50% would pay $20-50/month
- Feature requests: <10 must-haves for v1

### Risk Mitigation

**Risk:** LLM output too inconsistent for reliable metrics
**Mitigation:** Start with N=100 if needed; refine prompts; add more constraints

**Risk:** Customers unwilling to share workflow data
**Mitigation:** Use anonymized/synthetic data; offer on-premise deployment

**Risk:** Extraction fails on edge cases
**Mitigation:** Flag for human review; iteratively improve regexes

## Phase 4: Production Readiness (4 weeks)

Based on pilot feedback:

**Features to Add:**
- User authentication
- Workflow storage/history
- Custom prompt library
- Comparison view (before/after AI deployment)
- API access for Skillbench integration

**Refinements:**
- UI polish based on feedback
- Performance optimization
- Error handling improvements
- Documentation

**Go-to-Market:**
- Pricing model ($25-75/month tiered)
- Marketing site
- Demo video
- Integration with Skillbench

## Timeline Summary

- **Weeks 1-2:** Experimental design
- **Weeks 3-6:** MVP development
- **Weeks 7-12:** Customer pilot
- **Weeks 13-16:** Production readiness

**Total: 16 weeks (~4 months) to production launch**

## Budget Estimate

**Development:**
- Matt's time: 40 hours (design + oversight)
- Engineer: 200 hours @ $150/hr = $30,000
- Or: Matt builds MVP solo (80 hours)

**Pilot:**
- Customer incentives: $500 × 5 = $2,500
- API costs (testing + pilot): ~$500

**Total: $3,000 (if Matt builds) or $33,000 (if outsourced)**

## Decision Points

**Go/No-Go After Experimental Design:**
- If optimal N > 100 → Too expensive/slow
- If metric extraction < 90% → Needs more work

**Go/No-Go After Pilot:**
- If satisfaction < 7/10 → Not ready
- If willingness to pay < 30% → Business model problem
- If must-have features > 15 → Scope too large

## Success Definition

**Pilot success =** 
- 3+ customers complete analysis of 3+ workflows
- >80% of metrics achieve MEDIUM or HIGH stability
- >50% would pay $25-50/month
- <5 critical bugs or usability issues

**Production success =**
- 10+ paying customers within 6 months
- 50+ workflows analyzed/month
- NPS > 40
- Integrated with Skillbench platform
