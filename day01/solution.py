import fnmatch

def parse_oneline(text):
    """Parse `git log --oneline` text into a list of (short_hash, subject) tuples, in order."""
    raise NotImplementedError

def is_ignored(patterns, path):
    """Return True if `path` is covered by any .gitignore pattern."""
    raise NotImplementedError

def count_covered(patterns, paths):
    """Return how many of `paths` are ignored by the given patterns."""
    raise NotImplementedError
