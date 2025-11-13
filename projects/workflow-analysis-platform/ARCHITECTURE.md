# Workflow Analysis Platform - Technical Architecture

## System Components

### 1. Parallel Execution Engine
**Purpose:** Run N analyses concurrently, manage API calls efficiently

**Technology Stack:**
- Python asyncio for concurrent execution
- OpenAI Batch API (50% cost reduction) or concurrent API calls
- Rate limiting and retry logic

**Key Function:**
```python
async def analyze_workflow(
    workflow_data: str,
    prompt: str,
    n_iterations: int = 50,
    model: str = "gpt-4o-mini"
) -> AggregatedMetrics
```

### 2. Metric Extraction Layer
**Purpose:** Parse LLM responses into structured data for statistical analysis

**Approach:**
- Regex patterns for common metrics (cycle time, percentages, counts)
- Fallback: Secondary LLM call to extract structured JSON
- Validation: Check units, ranges, internal consistency

**Key Function:**
```python
def extract_metrics(llm_response: str) -> Dict[str, float]:
    """Parse response into {metric_name: value} dict."""
```

### 3. Statistical Aggregation Engine
**Purpose:** Compute mean, SD, confidence intervals, stability scores

**Outputs:**
- Mean and median
- Standard deviation
- 95% confidence intervals
- Coefficient of variation (stability metric)
- Stability classification (HIGH/MEDIUM/LOW)

**Key Function:**
```python
def aggregate_with_confidence(
    metrics_list: List[Dict],
    confidence_level: float = 0.95
) -> AggregatedMetrics
```

### 4. Variance Interpretation System
**Purpose:** Flag ambiguous data for human review

**Rules:**
- CV < 10%: HIGH stability (clear signal)
- CV 10-25%: MEDIUM stability (moderate confidence)
- CV > 25%: LOW stability (ambiguous data - flag for review)

**Outputs:**
- Stability ratings per metric
- Flags for metrics needing human review
- Suggested clarifying questions for users

## Delivery Options

### Option A: API Service
RESTful service for programmatic access

**Endpoint:**
```
POST /api/analyze-workflow
Body: {
  "workflow_data": "...",
  "analysis_type": "process" | "skill",
  "n_iterations": 50
}

Response: {
  "metrics": {...},
  "flags": [...],
  "cost": "$1.23",
  "execution_time": "8.2s"
}
```

### Option B: Streamlit Application
Web UI for interactive analysis (similar to embeddings demo)

**Tabs:**
1. Upload Workflow Data (paste or upload)
2. Run Analysis (select type, set N, execute)
3. Results (metrics with CIs, stability ratings, visualizations)
4. Raw Outputs (view all N responses, drill into variance)
5. Export (CSV with full statistics)

**Advantages:**
- Lower barrier to entry (no API integration needed)
- Visual feedback (distribution plots, stability indicators)
- Immediate value demonstration

### Option C: Hybrid
- API for Skillbench integration
- Streamlit for workshops and standalone use

## Cost Optimization

**Using GPT-4o-mini + OpenAI Batch API:**

Per workflow analysis (50 iterations):
- Tokens: ~65,000 (1,300 per run × 50)
- Batch API cost: ~$0.01 (50% savings)
- Execution time: 10-15 seconds

**Annual cost for active customer (50 workflows/month):**
- $0.01 × 50 = $0.50/month
- $6/year per customer

**Conclusion:** Negligible marginal cost; can run 100+ iterations if needed

## Data Flow

```
1. User uploads workflow data (emails, Slack, etc.)
   ↓
2. System selects prompts (process + skill)
   ↓
3. Parallel execution: N concurrent LLM calls
   ↓
4. Metric extraction: Parse each response
   ↓
5. Statistical aggregation: Compute means, CIs, stability
   ↓
6. Variance interpretation: Flag ambiguous metrics
   ↓
7. Output: Metrics with confidence + flags for review
```

## Technology Decisions

### Language
**Python** - Rich ecosystem for async, LLM APIs, data analysis

### LLM Provider
**OpenAI** (GPT-4o-mini) - Best cost/performance, Batch API support

### Compute
**Cloud Functions or Render** - Serverless execution, auto-scaling

### Storage
**PostgreSQL or SQLite** - Store analysis history, prompts, results

### Frontend (if Streamlit)
**Streamlit + Plotly** - Rapid development, good visualizations

## Security Considerations

- Workflow data may contain sensitive information
- Need: Data encryption at rest and in transit
- Need: User authentication and access control
- Need: Audit logging of all analyses
- Consider: On-premise deployment option for enterprise

## Next Steps

See `PILOT_PLAN.md` for validation approach.
