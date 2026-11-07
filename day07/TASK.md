# Day 07 — Station Reading Profiler

**Scenario:** CityPulse ingests raw air-quality sensor readings and the ops team needs a quick profile of which stations are reporting and how dirty the air is.

## Your task
Each reading is a dict `{"station_id", "ts", "pollutant", "value"}`. Implement three functions over a list of such readings:

- `readings_per_station(readings)` -> a list of `(station_id, count)` tuples sorted ascending by `station_id`.
- `average_value(readings, pollutant)` -> the mean `value` of all readings for that `pollutant`, rounded to 2 decimals; return `0.0` if none match.
- `busiest_station(readings)` -> the `station_id` with the most readings; break ties by the lexicographically smallest id.

**Example:** for the sample `READINGS`, `readings_per_station(READINGS)` returns `[('S1', 3), ('S2', 2), ('S3', 1)]`, `average_value(READINGS, 'NO2')` returns `21.33`, and `busiest_station(READINGS)` returns `'S1'`.

---
Edit `day07/solution.py`, commit & push, then click **Run Test** in the platform.
