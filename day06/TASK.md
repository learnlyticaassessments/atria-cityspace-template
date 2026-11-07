# Day 06 — Order the CI jobs DAG / detect a cycle (GitHub Actions)

**Scenario:** A **CityPulse** GitHub Actions workflow wires jobs together with `needs:`. Before running, the scheduler must put the jobs in a valid order and refuse a workflow whose `needs` form a cycle.

A workflow is modeled as a dict mapping each job name to the list of jobs it `needs`, e.g. `{'lint': [], 'test': ['lint'], 'build': ['lint'], 'deploy': ['test', 'build']}`.

## Your task
- `run_order(jobs)` - return a deterministic topological order (Kahn's algorithm; when several jobs are ready at once, take them in alphabetical order). Return `[]` if the graph has a cycle or any `needs` names a job that is not defined.
- `has_cycle(jobs)` - return `True` if a non-empty workflow cannot be fully ordered.
- `ready_jobs(jobs, completed)` - return the sorted list of jobs whose every dependency is in `completed` and which are not themselves already in `completed`.

## Example
```python
jobs = {'lint': [], 'test': ['lint'], 'build': ['lint'], 'deploy': ['test', 'build']}
run_order(jobs)            # -> ['lint', 'build', 'test', 'deploy']
ready_jobs(jobs, ['lint']) # -> ['build', 'test']
```

---
Edit `day06/solution.py`, commit & push, then click **Run Test** in the platform.
