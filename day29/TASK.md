# Day 29 — MoSCoW-prioritise the CityPulse backlog

**Scenario:** With a fixed sprint capacity, the CityPulse team must decide which backlog items to commit to by value, effort, and must-have status.

## Your task
Each backlog item is `{"id": str, "value": int, "effort": int, "must": bool}`. Implement:

- `moscow_bucket(item) -> str` — return `"Must"` if `item["must"]` is truthy. Otherwise use the ratio `value / effort`: `>= 3` -> `"Should"`, `>= 1.5` -> `"Could"`, else `"Wont"`.
- `prioritise(items) -> list[str]` — return the item ids sorted by `(bucket rank, value/effort descending, id)`, where bucket rank is `Must < Should < Could < Wont`.
- `fit_capacity(items, capacity) -> list[str]` — walk the items in priority order and greedily keep each whose effort still fits the remaining `capacity`; return the chosen ids in the order taken.

**Example:**
```python
moscow_bucket({"id": "A", "value": 10, "effort": 2, "must": False})  # -> 'Should'
# Backlog A(10/2),E(8/2),D must,B(3/2),C(1/2), capacity 8:
#   prioritise -> ['D', 'A', 'E', 'B', 'C']
#   fit_capacity(..., 8) -> ['D', 'A', 'E']
```

---
Edit `day29/solution.py`, commit & push, then click **Run Test** in the platform.
