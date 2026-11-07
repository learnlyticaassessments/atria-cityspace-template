
from collections import Counter
import statistics

READINGS = [
    {"station_id": "S1", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 42.0},
    {"station_id": "S1", "ts": "2026-01-01T09:00:00", "pollutant": "PM25", "value": 50.0},
    {"station_id": "S2", "ts": "2026-01-01T08:00:00", "pollutant": "NO2",  "value": 18.0},
    {"station_id": "S1", "ts": "2026-01-01T10:00:00", "pollutant": "NO2",  "value": 22.0},
    {"station_id": "S3", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 30.0},
    {"station_id": "S2", "ts": "2026-01-01T09:00:00", "pollutant": "NO2",  "value": 24.0},
]

def readings_per_station(readings):
    raise NotImplementedError

def average_value(readings, pollutant):
    raise NotImplementedError

def busiest_station(readings):
    raise NotImplementedError
