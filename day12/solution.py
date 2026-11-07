import fnmatch

def _match(pattern, value):
    # TODO: return True if the wildcard pattern matches value (use fnmatch.fnmatch)
    raise NotImplementedError

def statement_matches(statement, request):
    # TODO: return True if this statement's action AND resource both match the request
    raise NotImplementedError

def evaluate_policy(statements, request):
    # TODO: apply explicit-deny precedence; default to "Deny"
    raise NotImplementedError
