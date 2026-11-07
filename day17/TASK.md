# Day 17 — Routing and Ranking on the CityPulse Station Graph

**Scenario:** CityPulse models its sensor stations as a weighted graph (relay latency on each link) and needs both the cheapest route between stations and the most-polluted readings.

## Your task
Implement:

- `shortest_path_cost(graph, src, dst)` -> `int`: run Dijkstra over `graph`, a dict `{node: [(neighbor, weight), ...]}` with non-negative weights. Return the minimum total cost from `src` to `dst`, or `-1` if `dst` is unreachable (cost from a node to itself is `0`).
- `top_k_stations(readings, k)` -> `list`: return the `k` highest-`value` readings as `(station_id, value)` tuples, ordered by `value` descending and then `station_id` descending; if `k` exceeds the number of readings, return them all (use `heapq`).

**Example:**
```python
graph = {"A": [("B", 4), ("C", 1)], "C": [("B", 2)], "B": [("D", 5)], "D": []}
shortest_path_cost(graph, "A", "D")  # -> 8  (A->C->B->D)
top_k_stations([
    {"station_id": "S1", "ts": 1, "pollutant": "pm25", "value": 40},
    {"station_id": "S2", "ts": 1, "pollutant": "pm25", "value": 90},
], 1)                                 # -> [("S2", 90)]
```

---
Edit `day17/solution.py`, commit & push, then click **Run Test** in the platform.
