# Workflow Analysis Platform
**Statistical Consensus Approach to Workflow Measurement**

## Overview

Production-grade system for analyzing organizational workflows using AI with statistical rigor. Goes beyond the Teamraderie workshop's manual copy-paste approach to provide defensible, confidence-bounded metrics.

## Core Problem

**Workshop approach:** Run prompt once, get one answer, hope it's right
→ Non-reproducible, non-defensible, fragile

**Production approach:** Run analysis N times, aggregate with statistics, report confidence intervals
→ Reproducible, defensible to CFOs, reveals data quality issues

## Key Innovation: Statistical Consensus

Instead of single execution:
```
Cycle time: 15 days  (could be anything - no confidence)
```

Provide aggregated statistics:
```
Cycle time: 14.7 days (±1.2 SD, 95% CI: 13.5-15.9 days, n=50)
Stability: HIGH (CV=8%)
```

High variance flags ambiguous data needing human review.

## Architecture

See `ARCHITECTURE.md` for technical design.

## Pilot Plan

See `PILOT_PLAN.md` for experimental design and validation approach.

## Status

**Current:** Concept documented
**Next:** Determine optimal N, build core consensus engine
**Target:** Pilot with 2-3 Skillbench customers Q1 2026

## Related Work

- **Teamraderie workshop:** Demo/marketing version (manual prompts)
- **This platform:** Production/product version (automated with statistics)
- **Skillbench:** Natural integration point for workflow + skill measurement
