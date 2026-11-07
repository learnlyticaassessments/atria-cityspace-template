# Day 26 — CityPulse deploy gate and semver bump

**Scenario:** The CityPulse CI/CD pipeline must only release the API when every stage is green, and each release gets a semantic-version bump.

## Your task
Implement three module-level functions:

- `should_deploy(stages: list[dict]) -> bool` — each stage is `{"name": str, "status": str}`. Return `True` only when the list is non-empty **and** every stage's `status` is `"pass"`.
- `bump_version(current: str, level: str) -> str` — `current` is `"MAJOR.MINOR.PATCH"`. For `level` `"major"` increment major and reset minor/patch to 0; `"minor"` increment minor and reset patch; `"patch"` increment patch. Return the new version string.
- `pipeline_result(stages, current, level) -> str` — if `should_deploy(stages)`, return `bump_version(current, level)`; otherwise return `"BLOCKED"`.

**Example:**
```python
bump_version("1.4.9", "minor")      # -> '1.5.0'
pipeline_result([{"name": "build", "status": "pass"}], "2.0.0", "patch")  # -> '2.0.1'
```

---
Edit `day26/solution.py`, commit & push, then click **Run Test** in the platform.
