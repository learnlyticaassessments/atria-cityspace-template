# Day 20 — CityPulse: split the data and score a baseline

**Scenario:** Before fitting any model, CityPulse establishes a fair test set and a mean baseline to beat.

## Your task
Implement four pure functions (standard library only):
- `train_test_split(data, test_fraction)` - time series must not be shuffled, so split **by index**: `test_size = int(len(data) * test_fraction)`, the last `test_size` rows are the test set. Return the tuple `(train, test)` as two lists.
- `mean_baseline(train)` - return the mean of the training targets, rounded to 2 decimals. This constant is the baseline prediction.
- `mae(actual, predicted)` - mean absolute error, rounded to 2 decimals.
- `rmse(actual, predicted)` - root mean squared error, rounded to 2 decimals.

**Example:**
```python
train_test_split([10, 20, 30, 40, 50], 0.4)  # ([10, 20, 30], [40, 50])
mae([50.0, 50.0], [48.0, 55.0])              # 3.5
rmse([50.0, 50.0], [48.0, 55.0])             # 3.81
```


---
Edit `day20/solution.py`, commit & push, then click **Run Test** in the platform.
