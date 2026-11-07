# Day 10 — Window Analytics on Air Quality

**Scenario:** The CityPulse analytics team wants the worst spikes per station and a smoothed trend line, computed in SQL using window functions rather than in Python loops.

## Your task
Use the stdlib `sqlite3` module and SQL window functions. Implement:

- `top_n_per_station(readings, n)` -> for each station, the top `n` readings by `value` (descending), returned as `(station_id, ts, value)` tuples ordered by `station_id` ascending then `value` descending then `ts` ascending; use `ROW_NUMBER() OVER (PARTITION BY station_id ...)`. Values rounded to 2 decimals.
- `rolling_avg(readings, station_id, pollutant, window)` -> for the given station and pollutant, a list of `(ts, avg)` tuples ordered by `ts`, where `avg` is the moving average over the current row and the `window-1` rows before it (`AVG(value) OVER (ORDER BY ts ROWS BETWEEN ... PRECEDING AND CURRENT ROW)`), rounded to 2 decimals.

**Example:** for the sample `READINGS`, `top_n_per_station(READINGS, 2)` returns `[('S1', '2026-01-01T10:00:00', 60.0), ('S1', '2026-01-01T11:00:00', 40.0), ('S2', '2026-01-01T09:00:00', 35.0), ('S2', '2026-01-01T10:00:00', 15.0)]`.

---
Edit `day10/solution.py`, commit & push, then click **Run Test** in the platform.
