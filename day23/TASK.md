# Day 23 — CityPulse: validate and handle a /predict request

**Scenario:** The CityPulse `/predict` FastAPI endpoint must reject bad payloads cleanly - so the validation and response logic lives in pure functions you can unit-test without a server.

## Your task
- `validate_request(payload)` - `payload` is a dict. Return `"OK"` when it has a non-empty **string** `station_id`, a `pollutant` in `{"PM25","PM10","NO2","O3"}`, and a **non-negative numeric** `value`. Otherwise return the first failing code, checked in this order: `"MISSING_FIELD"` (any required field absent, or station_id empty/not a string), then `"BAD_POLLUTANT"`, then `"BAD_VALUE"` (non-numeric or negative).
- `handle_predict(payload)` - if the payload is invalid, return `{"status": 400, "error": <code>}`. Otherwise return `{"status": 200, "pollutant": <name>, "prediction": round(value * 1.05 + offset, 2)}`, with offsets `PM25=2.0, PM10=1.5, NO2=1.0, O3=0.5`.

**Example:**
```python
handle_predict({"station_id": "A", "pollutant": "PM25", "value": 40.0})
# {'status': 200, 'pollutant': 'PM25', 'prediction': 44.0}
validate_request({"station_id": "A", "pollutant": "CO", "value": 40.0})  # 'BAD_POLLUTANT'
```


---
Edit `day23/solution.py`, commit & push, then click **Run Test** in the platform.
