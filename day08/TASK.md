# Day 08 — Pollutant Wrangling Without Pandas

**Scenario:** A CityPulse data engineer must reshape raw readings into daily summaries, but the sandbox has no pandas, so the work is done with plain lists, dicts and the `statistics` module.

## Your task
Each reading is a dict `{"station_id", "ts", "pollutant", "value"}` where `ts` is an ISO timestamp `YYYY-MM-DDTHH:MM:SS`. Implement:

- `avg_by_pollutant(readings)` -> a list of `(pollutant, mean_value)` tuples sorted by `pollutant`, each mean rounded to 2 decimals.
- `median_value(readings, pollutant)` -> the median `value` for that pollutant rounded to 2 decimals; `0.0` if none match.
- `resample_daily_mean(readings, pollutant)` -> a list of `(date, mean_value)` tuples for that pollutant, one per calendar date (the first 10 chars of `ts`), sorted by date, means rounded to 2 decimals.

**Example:** for the sample `READINGS`, `resample_daily_mean(READINGS, 'PM25')` returns `[('2026-01-01', 40.0), ('2026-01-02', 20.0)]` (S1+S3 average 40.0 on day 1, 20.0 on day 2).

---
Edit `day08/solution.py`, commit & push, then click **Run Test** in the platform.
