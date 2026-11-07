# Day 14 — Auditing the CityPulse EC2 Security Group

**Scenario:** The CityPulse ingest server runs on EC2, and you must audit its security-group inbound rules before go-live.

## Your task
Each rule is `{"from_port": int, "to_port": int, "cidr": str}`. Implement:

- `_in_range(rule, port)` -> `bool`: `True` if `port` is within the rule's inclusive `[from_port, to_port]`.
- `port_allowed(rules, port, source_cidr)` -> `bool`: `True` if some rule covers `port` **and** its `cidr` is `"0.0.0.0/0"` or exactly equals `source_cidr`.
- `world_open_ports(rules)` -> `list`: the **sorted** list of distinct ports exposed to `0.0.0.0/0`.
- `has_open_ssh(rules)` -> `bool`: `True` if port `22` is reachable from `0.0.0.0/0`.

**Example:**
```python
rules = [{"from_port": 22, "to_port": 22, "cidr": "0.0.0.0/0"}]
port_allowed(rules, 22, "203.0.113.7/32")  # -> True  (open to the world)
world_open_ports(rules)                     # -> [22]
has_open_ssh(rules)                         # -> True  (hardening red flag)
```

---
Edit `day14/solution.py`, commit & push, then click **Run Test** in the platform.
