import json

def pluck(payload_json, key):
    """Return the list of `key` values from each reading (jq: .readings[].<key>)."""
    raise NotImplementedError

def avg_value(payload_json):
    """Return the mean of every reading's 'value', rounded to 2 decimals."""
    raise NotImplementedError

def worst_station(payload_json):
    """Return the station with the highest 'value'; ties break by station id ascending."""
    raise NotImplementedError
