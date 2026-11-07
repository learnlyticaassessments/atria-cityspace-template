def run_order(jobs):
    """Return a deterministic topological run order, or [] on a cycle/unknown need."""
    raise NotImplementedError

def has_cycle(jobs):
    """Return True if the needs-graph cannot be fully ordered."""
    raise NotImplementedError

def ready_jobs(jobs, completed):
    """Return the sorted list of jobs whose needs are all completed and are not yet done."""
    raise NotImplementedError
