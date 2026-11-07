def station_day_kpis(readings, station_id, date):
    """Return {"count","avg_value","max_value","min_value","pollutants"} for the
    readings of `station_id` whose ts starts with `date`. When nothing matches,
    return {"count":0,"avg_value":0.0,"max_value":None,"min_value":None,"pollutants":[]}.
    avg/max/min rounded to 2dp; pollutants a sorted list of unique names."""
    pass
