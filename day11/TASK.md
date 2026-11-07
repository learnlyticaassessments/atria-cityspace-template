# Day 11 — Quarantining Dirty Readings

**Scenario:** Before any analytics run, the CityPulse ingestion pipeline must separate trustworthy readings from malformed ones and report why rows were quarantined.

## Your task
A reading is a dict `{"station_id", "ts", "pollutant", "value"}`. A row is REJECTED for the first failing rule, checked in this order: empty/missing `station_id` -> `"bad_station"`; `pollutant` not in `{PM25, PM10, NO2, O3, SO2, CO}` -> `"bad_pollutant"`; `value` not an int/float (booleans count as invalid) -> `"bad_value"`; `value` `< 0` or `> 1000` -> `"out_of_range"`; `ts` not matching `YYYY-MM-DDTHH:MM:SS` -> `"bad_ts"`. Implement:

- `clean_and_count(readings)` -> a tuple `(clean_count, rejected_count)` of ints.
- `rejection_reasons(readings)` -> a list of `(reason, count)` tuples sorted ascending by reason, covering only rejected rows.

**Example:** for the sample `READINGS`, `clean_and_count(READINGS)` returns `(2, 6)` and `rejection_reasons(READINGS)` returns `[('bad_pollutant', 1), ('bad_station', 1), ('bad_ts', 1), ('bad_value', 1), ('out_of_range', 2)]`.

---
Edit `day11/solution.py`, commit & push, then click **Run Test** in the platform.
