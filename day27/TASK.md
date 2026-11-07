# Day 27 — CityPulse SLO: availability, error budget, p95

**Scenario:** The CityPulse API publishes an SLO dashboard; from a window of request records you must compute availability, remaining error budget, and p95 latency.

## Your task
Each record is `{"status": int, "latency_ms": number}`. Implement:

- `availability(records) -> float` — percent of records whose `status` is below 500, `round(..., 2)`. Empty input returns `0.0`.
- `error_budget_remaining(records, slo) -> float` — `slo` is the target availability percent (e.g. `99.0`). The allowed error budget is `100 - slo`; the actual error rate is `100 - availability`. Return the percent of the budget still remaining, i.e. `round((allowed - error_rate) / allowed * 100, 2)` (may be negative if overspent). If `allowed <= 0`, return `0.0`.
- `p95_latency(records) -> float` — the 95th-percentile `latency_ms` using the **nearest-rank** method: sort ascending, take index `ceil(0.95 * n) - 1`, `round(..., 2)`. Empty input returns `0.0`.

**Example:**
```python
recs = [{"status": 200, "latency_ms": 10}, {"status": 503, "latency_ms": 20}]
availability(recs)   # -> 50.0
p95_latency(recs)    # -> 20.0  (ceil(0.95*2)-1 = index 1)
```

---
Edit `day27/solution.py`, commit & push, then click **Run Test** in the platform.
