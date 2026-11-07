# Day 01 — Ingest & profile the CityPulse feed

**Goal:** read the raw sensor feed, clean it, and produce a small profile summary.

## What to build

Edit `day01/solution.py`. Implement the two functions below. Do not rename them or change their
signatures — the grader calls them by name.

### `load_readings(path: str) -> pandas.DataFrame`
- Read the CSV at `path`.
- Parse the `ts` column as datetime.
- Drop rows where `value` is missing.
- Return the cleaned DataFrame, sorted by `ts` ascending.

### `summarize(df: pandas.DataFrame) -> dict`
Return a dict with:
- `"n_rows"` — number of rows (int)
- `"n_sensors"` — number of distinct `sensor_id` values (int)
- `"value_mean"` — mean of `value` rounded to 2 decimals (float)
- `"value_max"` — max of `value` (float)

## Run it

```bash
cd day01
python solution.py sample.csv
```

A `sample.csv` is included so you can try your code. The official grade uses a different, hidden
dataset with the same schema (`ts,sensor_id,value`).

## Submit

Commit your changes, push, then click **Run Test** in the platform.
