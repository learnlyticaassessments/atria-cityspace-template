# Day 13 — A Tiny In-Memory S3 for CityPulse Readings

**Scenario:** Before wiring up `boto3`, the CityPulse team prototypes an S3 bucket as a plain Python `dict` that maps object keys to stored data.

## Your task
Implement four module-level functions:

- `s3_uri(bucket, key)` -> `str`: return `"s3://<bucket>/<key>"`. A leading `/` on `key` must be stripped first.
- `put_object(store, key, value)` -> `dict`: return a **new** dict (copy of `store`) with `key` set to `value`; do **not** mutate `store`.
- `get_object(store, key)` -> value or `None`: return the value for `key`, or `None` if absent.
- `list_prefix(store, prefix)` -> `list`: return the **sorted** list of keys that start with `prefix`.

**Example:**
```python
bucket = put_object({}, "readings/d1.json", 42)
get_object(bucket, "readings/d1.json")                 # -> 42
s3_uri("citypulse-raw", "/readings/d1.json")           # -> "s3://citypulse-raw/readings/d1.json"
list_prefix({"logs/a": 1, "data/b": 2}, "logs/")       # -> ["logs/a"]
```

---
Edit `day13/solution.py`, commit & push, then click **Run Test** in the platform.
