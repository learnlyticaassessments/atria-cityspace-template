# Day 28 — Ground and redact a CityPulse LLM reply

**Scenario:** A CityPulse assistant answers air-quality questions from an LLM; before showing a reply you must flag any number it invented and redact PII from the text.

## Your task
Implement four module-level functions (regex-based, standard library only):

- `extract_numbers(text: str) -> list[float]` — every integer or decimal in the text, as floats, in order of appearance.
- `unsupported_numbers(answer: str, allowed: list) -> list[float]` — the **sorted** unique numbers in `answer` that are **not** in `allowed` (the facts the model was given).
- `is_grounded(answer: str, allowed: list) -> bool` — `True` iff there are no unsupported numbers.
- `redact_pii(text: str) -> str` — replace any email with `[EMAIL]` and any phone number (`ddd-ddd-dddd`, with optional `-`/`.` separators or none) with `[PHONE]`. Redact emails before phones.

**Example:**
```python
unsupported_numbers("The AQI was 95 at station 7.", [42, 7])  # -> [95.0]
redact_pii("contact me at jo@airteam.io or 555-123-4567")
# -> 'contact me at [EMAIL] or [PHONE]'
```

---
Edit `day28/solution.py`, commit & push, then click **Run Test** in the platform.
