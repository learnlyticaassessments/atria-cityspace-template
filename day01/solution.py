"""Day 01 — Ingest & profile the CityPulse feed.

Implement load_readings() and summarize(). See TASK.md for the spec.
The grader imports this module and calls these functions by name — keep the signatures.
"""
import sys

import pandas as pd


def load_readings(path: str) -> pd.DataFrame:
    # TODO: read the CSV, parse `ts` as datetime, drop rows with missing `value`,
    # return sorted by `ts` ascending.
    raise NotImplementedError


def summarize(df: pd.DataFrame) -> dict:
    # TODO: return {"n_rows", "n_sensors", "value_mean", "value_max"} per TASK.md.
    raise NotImplementedError


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "sample.csv"
    data = load_readings(src)
    print(summarize(data))
