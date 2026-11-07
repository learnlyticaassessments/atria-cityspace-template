# Day 15 — Costing the CityPulse Ingest Lambda

**Scenario:** CityPulse ingests sensor readings through an AWS Lambda, and finance wants the monthly bill and the cheapest memory setting.

## Your task
Use `REQUEST_PRICE = 0.0000002` USD/request and `GBS_PRICE = 0.0000166667` USD/GB-second. Implement:

- `gb_seconds(invocations, duration_ms, memory_mb)` -> `float`: `invocations * (memory_mb/1024) * (duration_ms/1000)`.
- `lambda_cost(invocations, duration_ms, memory_mb)` -> `float`: request cost **plus** compute cost (`gb_seconds * GBS_PRICE`), returned as `round(total, 2)`.
- `cheapest_memory(invocations, configs)` -> `int`: given `configs` of `{"memory_mb": int, "duration_ms": int}`, return the `memory_mb` with the lowest `lambda_cost`. On a tie, return the smaller memory.

**Example:**
```python
lambda_cost(1_000_000, 200, 512)   # -> 1.87
cheapest_memory(1_000_000, [
    {"memory_mb": 128, "duration_ms": 1000},
    {"memory_mb": 512, "duration_ms": 200},
])                                  # -> the cheaper of the two memory sizes
```

---
Edit `day15/solution.py`, commit & push, then click **Run Test** in the platform.
