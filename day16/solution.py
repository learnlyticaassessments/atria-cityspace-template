from collections import deque

def dedup_latest(readings):
    # TODO: keep only the latest (max ts) reading per (station_id, pollutant);
    #       return a sorted list of (station_id, pollutant, value) tuples
    raise NotImplementedError

def rolling_max(values, k):
    # TODO: return the max of every length-k window, left to right
    #       (use a monotonic deque for O(n))
    raise NotImplementedError
