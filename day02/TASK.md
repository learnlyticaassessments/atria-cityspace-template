# Day 02 — Reimplement a grep|cut|sort|uniq pipeline (Linux)

**Scenario:** On a **CityPulse** ingest box you pull station counts out of raw sensor lines with a classic `grep ... | cut -d, -f1 | sort | uniq -c` shell pipeline - now reimplement it in Python so it can be unit-tested.

Each line is CSV: `station_id,ts,pollutant,value` (e.g. `ST3,2026-01-01T00:00,pm25,42.0`).

## Your task
- `grep(lines, pollutant)` - return the list of lines whose pollutant field (index 2) equals `pollutant`, preserving order.
- `cut(lines, idx)` - return the field at 0-based index `idx` from each comma-delimited line (like `cut -d, -f`).
- `count_sorted(items)` - like `sort | uniq -c`: return a list of `(item, count)` tuples sorted by item ascending.
- `station_counts(lines, pollutant)` - chain them: grep the pollutant, cut the `station_id` (field 0), then `count_sorted`.

## Example
```python
lines = ["ST3,t,pm25,42.0", "ST1,t,pm10,30.0", "ST3,t,pm25,51.0"]
station_counts(lines, "pm25")  # -> [('ST3', 2)]
```

---
Edit `day02/solution.py`, commit & push, then click **Run Test** in the platform.
