# Day 19 — CityPulse: KPI data layer behind a dashboard

**Scenario:** Behind the CityPulse Streamlit dashboard, a selector picks a station and a day; the UI just renders the KPIs your function returns.

## Your task
Implement `station_day_kpis(readings, station_id, date)`. Each reading is `{"station_id","ts","pollutant","value"}`; `ts` looks like `"2026-11-03T08:00"` and `date` looks like `"2026-11-03"`.

Keep only readings whose `station_id` equals the argument **and** whose `ts` starts with `date`, then return a dict:
- `"count"` - number of matching readings (int)
- `"avg_value"`, `"max_value"`, `"min_value"` - over matching `value`s, rounded to 2 decimals
- `"pollutants"` - sorted list of the distinct pollutant names

If nothing matches, return `{"count": 0, "avg_value": 0.0, "max_value": None, "min_value": None, "pollutants": []}`.

**Example:**
```python
station_day_kpis(readings, "A", "2026-11-03")
# {'count': 3, 'avg_value': 37.0, 'max_value': 51.0, 'min_value': 18.0, 'pollutants': ['NO2', 'PM25']}
```


---
Edit `day19/solution.py`, commit & push, then click **Run Test** in the platform.
