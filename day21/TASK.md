# Day 21 — CityPulse: a feature pipeline by hand

**Scenario:** CityPulse models need numeric features, so raw readings pass through a scale-then-encode pipeline - the same idea as a scikit-learn `Pipeline`, built here from pure functions.

## Your task
- `fit_scaler(values)` - return `(min, max)`, the learned min-max parameters.
- `scale(values, scaler)` - apply a fitted `(min, max)` scaler as `(v - min) / (max - min)`, each result rounded to 2 decimals. If `max == min`, every output is `0.0`.
- `one_hot(value, vocab)` - return a one-hot list for `value` over `sorted(vocab)` (sorted so the vector is stable); an unknown value gives all zeros.
- `build_features(readings, vocab)` - return a list of feature rows `[scaled_value, *one_hot(pollutant)]`, where the value column is min-max scaled with the scaler fitted on these readings.

**Example:**
```python
scale([10.0, 20.0, 30.0], (10.0, 30.0))   # [0.0, 0.5, 1.0]
one_hot("NO2", ["PM25", "NO2", "O3"]) # [1, 0, 0]  (sorted vocab: NO2, O3, PM25)
```


---
Edit `day21/solution.py`, commit & push, then click **Run Test** in the platform.
