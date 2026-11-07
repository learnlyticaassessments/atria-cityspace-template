# Day 22 — CityPulse: ensemble predictions and sliced error

**Scenario:** A CityPulse model card has to show not just one error number but where the model is weak - so the team averages an ensemble and slices error by station and hour.

## Your task
- `ensemble_mean(predictions)` - `predictions` is a list of equal-length lists, one per model. Return the element-wise mean across models, each rounded to 2 decimals.
- `residuals(actual, predicted)` - return the signed residuals `actual - predicted`, each rounded to 2 decimals.
- `mae_by_group(actual, predicted, groups)` - `groups[i]` labels row `i` (a station id or an hour). Return `{group: MAE rounded to 2 decimals}` with keys in sorted order.

**Example:**
```python
ensemble_mean([[40.0, 50.0], [44.0, 46.0], [46.0, 54.0]])  # [43.33, 50.0]
mae_by_group([50.0, 60.0, 70.0, 80.0], [48.0, 64.0, 69.0, 75.0], ["A","A","B","B"])
# {'A': 3.0, 'B': 3.0}
```


---
Edit `day22/solution.py`, commit & push, then click **Run Test** in the platform.
