# Day 25 — Lint a CityPulse Dockerfile

**Scenario:** Before a CityPulse service image ships, a pre-commit check scans its Dockerfile for common security and reproducibility anti-patterns.

## Your task
Implement two module-level functions that treat the Dockerfile as plain text:

- `parse_instructions(text: str) -> list[tuple]` — return a list of `(INSTRUCTION, argument)` tuples, one per line, skipping blank lines and `#` comment lines. The instruction keyword is uppercased; the argument is the rest of the line, stripped (empty string if none).
- `lint_dockerfile(text: str) -> list[str]` — return a **sorted** list of anti-pattern codes:
  - `unpinned_base` — a `FROM` image whose tag is missing or is `latest`
  - `runs_as_root` — no `USER` instruction, or the last `USER` is `root`
  - `no_healthcheck` — no `HEALTHCHECK` instruction anywhere
  - `secret_in_env` — an `ENV` whose key contains `KEY`, `SECRET`, `TOKEN`, or `PASSWORD` (case-insensitive)

**Example:**
```python
parse_instructions("# base image\nFROM python:3.11\nUSER app\n")
# -> [('FROM', 'python:3.11'), ('USER', 'app')]

lint_dockerfile("FROM python:latest\nENV API_KEY=abc123\nRUN pip install flask\nCOPY . /app")
# -> ['no_healthcheck', 'runs_as_root', 'secret_in_env', 'unpinned_base']
```

---
Edit `day25/solution.py`, commit & push, then click **Run Test** in the platform.
