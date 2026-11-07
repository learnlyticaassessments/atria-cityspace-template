# Day 16 — Deduplicating and Smoothing CityPulse Readings

**Scenario:** The CityPulse pipeline must de-duplicate noisy sensor readings and compute a rolling peak for the dashboard.

## Your task
Readings are dicts `{"station_id", "ts", "pollutant", "value"}`. Implement:

- `dedup_latest(readings)` -> `list`: keep only the **latest** (maximum `ts`) reading for each `(station_id, pollutant)` pair, then return a **sorted** list of `(station_id, pollutant, value)` tuples.
- `rolling_max(values, k)` -> `list`: return the maximum of every contiguous length-`k` window, left to right, using a monotonic deque for `O(n)`.

**Example:**
```python
dedup_latest([
    {"station_id": "S1", "ts": 1, "pollutant": "pm25", "value": 10},
    {"station_id": "S1", "ts": 3, "pollutant": "pm25", "value": 22},
])  # -> [("S1", "pm25", 22)]
rolling_max([5, 3, 8, 2, 7, 1], 3)  # -> [8, 8, 8, 7]
```

---
Edit `day16/solution.py`, commit & push, then click **Run Test** in the platform.
