import re

def parse_cron(line):
    """Split a crontab line into (minute, hour, dom, month, dow, command)."""
    raise NotImplementedError

def fires_at(line, minute, hour):
    """Return True if the line's minute+hour fields fire at the given minute/hour."""
    raise NotImplementedError

def valid_reading(reading):
    """Validate an ingest record (station_id ^ST\\d+$, known pollutant, value >= 0)."""
    raise NotImplementedError
