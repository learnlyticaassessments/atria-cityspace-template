# Day 09 — Loading Readings into SQLite

**Scenario:** CityPulse is moving from flat files to a relational store; readings must land in a SQLite table that refuses duplicate samples for the same station, timestamp and pollutant.

## Your task
Use the stdlib `sqlite3` module. Implement:

- `load_readings(readings)` -> create an in-memory database with a `readings(station_id, ts, pollutant, value)` table that enforces a `UNIQUE(station_id, ts, pollutant)` constraint, insert every reading so that duplicates are silently ignored, and return the open `sqlite3.Connection`.
- `row_count(conn)` -> the number of rows actually stored (an `int`).
- `distinct_pollutants(conn)` -> a list of distinct pollutant names sorted ascending.
- `station_totals(conn)` -> a list of `(station_id, total_value)` tuples grouped by station, sorted by `station_id`, each total rounded to 2 decimals.

**Example:** the sample `READINGS` contains one exact duplicate of an `S1` PM25 sample, so `row_count(load_readings(READINGS))` returns `5` (not 6), and `distinct_pollutants(load_readings(READINGS))` returns `['NO2', 'O3', 'PM25']`.

---
Edit `day09/solution.py`, commit & push, then click **Run Test** in the platform.
