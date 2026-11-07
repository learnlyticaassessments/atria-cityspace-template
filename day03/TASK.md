# Day 03 — Reshape a CityPulse API payload like jq (APIs/JSON)

**Scenario:** You `curl` the **CityPulse** readings API and need to reshape its JSON the way you would with `jq`, but inside a Python client.

The response is a JSON string like `{"city": "Metroville", "readings": [{"station": "ST1", "pollutant": "pm25", "value": 42.0}, ...]}`.

## Your task
- `pluck(payload_json, key)` - parse the payload and return the list of `key` values from each entry of `readings`, in document order (the jq filter `.readings[].<key>`).
- `avg_value(payload_json)` - return the mean of every reading's `value`, rounded with `round(x, 2)`; return `0.0` when there are no readings.
- `worst_station(payload_json)` - return the `station` with the highest `value`; break ties by station id ascending. Return `None` when there are no readings.

## Example
```python
p = '{"city":"M","readings":[{"station":"ST1","value":10.0},{"station":"ST2","value":30.0}]}'
avg_value(p)       # -> 20.0
worst_station(p)   # -> 'ST2'
```

---
Edit `day03/solution.py`, commit & push, then click **Run Test** in the platform.
