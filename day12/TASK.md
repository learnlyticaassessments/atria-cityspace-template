# Day 12 — IAM Policy Evaluator for the CityPulse Data Lake

**Scenario:** The CityPulse data-lake team guards the `citypulse-raw` S3 bucket with IAM-style policies, and you must decide whether each API request is permitted.

## Your task
Implement three module-level functions:

- `_match(pattern, value)` -> `bool`: return `True` when the wildcard `pattern` matches `value` (use `fnmatch.fnmatch`, so `*` and prefix wildcards like `s3:Get*` work).
- `statement_matches(statement, request)` -> `bool`: return `True` when the statement's `action` **and** `resource` patterns both match the request's `action` and `resource`.
- `evaluate_policy(statements, request)` -> `str`: return `"Allow"` or `"Deny"`. Each statement is `{"effect": "Allow"|"Deny", "action": ..., "resource": ...}`. Apply AWS precedence: an **explicit Deny** that matches always wins; otherwise `"Allow"` only if some matching `Allow` exists; otherwise the implicit **`"Deny"`**.

**Example:**
```python
statements = [
    {"effect": "Allow", "action": "s3:*", "resource": "*"},
    {"effect": "Deny",  "action": "s3:DeleteObject", "resource": "*"},
]
evaluate_policy(statements, {"action": "s3:DeleteObject", "resource": "arn:aws:s3:::citypulse-raw/x"})  # -> "Deny"
```

---
Edit `day12/solution.py`, commit & push, then click **Run Test** in the platform.
