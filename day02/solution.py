def grep(lines, pollutant):
    """Keep only CSV lines whose pollutant field equals `pollutant`."""
    pass

def cut(lines, idx):
    """Return the field at 0-based index `idx` from each comma-delimited line."""
    pass

def count_sorted(items):
    """Like `sort | uniq -c`: return (item, count) tuples sorted by item ascending."""
    pass

def station_counts(lines, pollutant):
    """Full pipeline: grep the pollutant, cut station_id, sort | uniq -c."""
    pass
