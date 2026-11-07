# Day 05 — Is this CityPulse PR mergeable? (PR review rules)

**Scenario:** The **CityPulse** team automates its PR gate - a bot summarizes the diff and decides whether a pull request may merge.

## Your task
- `summarize(changes)` - `changes` is a list of dicts `{'path', 'additions', 'deletions'}`. Return the tuple `(files_changed, total_additions, total_deletions)` of ints.
- `review_decision(reviews)` - `reviews` is a list of review states (`'approve'`, `'request_changes'`, `'comment'`). Return `'blocked'` if any reviewer requested changes; otherwise `'approved'` if at least one approved; otherwise `'pending'`.
- `is_mergeable(pr)` - `pr` is a dict with keys `draft`, `conflicts`, `ci_passed`, `changes_requested`, `approvals`, `required_approvals`. Return `True` only if the PR is not a draft, has no conflicts, CI passed, has no outstanding change requests, and `approvals >= required_approvals`.

## Example
```python
summarize([{"path": "a.py", "additions": 40, "deletions": 5}])  # -> (1, 40, 5)
review_decision(["approve", "request_changes"])                 # -> 'blocked'
```

---
Edit `day05/solution.py`, commit & push, then click **Run Test** in the platform.
