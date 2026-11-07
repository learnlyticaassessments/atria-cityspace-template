# Day 24 — Validate a CityPulse sensor reading

**Scenario:** CityPulse ingests raw sensor payloads from the field; before a reading reaches the database it must be validated and coerced the way a Pydantic model would enforce it.

## Your task
Implement two module-level functions:

- `validate_reading(raw: dict) -> list[str]` — return a **sorted** list of error codes for the reading. An empty list means the reading is valid. Codes:
  - `station_id_missing` — `station_id` absent or blank
  - `ts_missing` — `ts` absent or blank
  - `pollutant_unknown` — `pollutant` (case-insensitive) is not one of `co, no2, o3, pm10, pm25, so2`
  - `value_not_number` — `value` cannot be coerced to `float`
  - `value_negative` — `value` coerces to a number below 0
- `normalize_reading(raw: dict) -> dict` — if the reading is valid, return a coerced dict with keys `station_id` (string, stripped), `ts` (string, stripped), `pollutant` (lowercased), `value` (float rounded to 2 dp). If the reading is invalid, return `{}`.

**Example:**
```python
validate_reading({"station_id": "S2", "ts": "t", "pollutant": "NO2", "value": -3})
# -> ['value_negative']   (NO2 is a known pollutant; the value is negative)

normalize_reading({"station_id": " S3 ", "ts": "t", "pollutant": "PM10", "value": "7.004"})
# -> {'station_id': 'S3', 'ts': 't', 'pollutant': 'pm10', 'value': 7.0}
```

---
Edit `day24/solution.py`, commit & push, then click **Run Test** in the platform.
