# Day 18 — CityPulse: summarise and bin sensor readings

**Scenario:** CityPulse engineers open every new sensor feed by eyeballing its distribution before trusting it.

## Your task
Implement three pure functions over air-quality readings (each reading is a dict `{"station_id","ts","pollutant","value"}`).

- `summary(values)` - given a list of numbers, return a dict `{"count": int, "min": float, "max": float, "mean": float, "median": float}`. Round `min`, `max`, `mean` and `median` to 2 decimals.
- `per_station_average(readings)` - return a dict mapping each `station_id` to the mean of its `value`s rounded to 2 decimals, with keys inserted in **sorted** order.
- `histogram_bins(values, n_bins)` - split the range `[min, max]` into `n_bins` equal-width bins and return a list of `n_bins` integer counts. A value landing exactly on the top edge belongs to the last bin. If every value is identical, put them all in bin 0.

**Example:**
```python
summary([42.0, 55.0, 48.0, 61.0, 45.0])
# {'count': 5, 'min': 42.0, 'max': 61.0, 'mean': 50.2, 'median': 48.0}
histogram_bins([42.0, 55.0, 48.0, 61.0, 45.0], 3)  # [3, 0, 2]
```


---
Edit `day18/solution.py`, commit & push, then click **Run Test** in the platform.
