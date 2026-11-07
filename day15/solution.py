REQUEST_PRICE = 0.0000002      # USD per request
GBS_PRICE = 0.0000166667       # USD per GB-second

def gb_seconds(invocations, duration_ms, memory_mb):
    # TODO: invocations * (memory in GB) * (duration in seconds)
    raise NotImplementedError

def lambda_cost(invocations, duration_ms, memory_mb):
    # TODO: request cost + compute cost (GB-seconds * GBS_PRICE), rounded to 2 dp
    raise NotImplementedError

def cheapest_memory(invocations, configs):
    # TODO: return the memory_mb of the lowest-cost config (tie -> smaller memory)
    raise NotImplementedError
