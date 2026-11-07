# Day 04 — Cron schedule & ingest validation (Bash/cron)

**Scenario:** The **CityPulse** ingest script runs from cron; you are porting its schedule check and its record-validation logic into Python so both can be tested.

## Your task
- `parse_cron(line)` - split a crontab line into the tuple `(minute, hour, dom, month, dow, command)`. The first five are the schedule fields; the command is everything after the fifth field (it may contain spaces).
- `fires_at(line, minute, hour)` - return `True` if the line's **minute** and **hour** fields both match the given `minute`/`hour`. Support these field forms: `*`, a plain number, a `a-b` range, a `*/n` step, and comma-separated lists of those. Assume day-of-month, month and day-of-week always match.
- `valid_reading(reading)` - return `True` only if `reading` is a dict whose `station_id` matches `^ST\d+$`, whose `pollutant` is one of `{'pm25','pm10','no2','o3'}`, and whose `value` is a non-negative number (reject booleans).

## Example
```python
line = "*/15 0-6 * * * /opt/citypulse/ingest.sh"
fires_at(line, 30, 3)  # -> True   (minute 30 is a 15-multiple, hour 3 is in 0-6)
fires_at(line, 7, 3)   # -> False  (minute 7 is not a 15-multiple)
```

---
Edit `day04/solution.py`, commit & push, then click **Run Test** in the platform.
