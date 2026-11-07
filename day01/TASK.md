# Day 01 — CityPulse repo hygiene: git log & .gitignore (Git)

**Scenario:** You are tidying the **CityPulse** `citypulse` repo and must audit its commit history and confirm secrets never get committed.

## Your task
Implement three module-level functions:

- `parse_oneline(text)` - given the raw text of `git log --oneline`, return a list of `(short_hash, subject)` tuples in the order they appear. Each line is the short hash, a single space, then the commit subject. Blank lines are skipped; an empty string yields `[]`.
- `is_ignored(patterns, path)` - return `True` if `path` is covered by any `.gitignore` pattern in the list `patterns`. Support three forms: an exact name or full path, a glob with `*`/`?` matched against the file's basename (e.g. `*.env`), and a directory pattern ending in `/` (e.g. `__pycache__/`) that matches any file whose path contains that directory. Lines that are blank or start with `#` are ignored.
- `count_covered(patterns, paths)` - return the integer count of how many entries of `paths` are ignored.

## Example
```python
parse_oneline("a1b2c3d Add ingest\n9f8e7d6 Fix parser")
# -> [('a1b2c3d', 'Add ingest'), ('9f8e7d6', 'Fix parser')]
is_ignored(["*.env", "__pycache__/"], "ingest/.env")  # -> True
```

---
Edit `day01/solution.py`, commit & push, then click **Run Test** in the platform.
