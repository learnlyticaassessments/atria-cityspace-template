
import re
from collections import Counter

ALLOWED = {"PM25", "PM10", "NO2", "O3", "SO2", "CO"}
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$")

READINGS = [
    {"station_id": "S1", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 42.0},
    {"station_id": "S1", "ts": "2026-01-01T09:00:00", "pollutant": "XYZ",  "value": 10.0},
    {"station_id": "",   "ts": "2026-01-01T08:00:00", "pollutant": "NO2",  "value": 18.0},
    {"station_id": "S2", "ts": "2026-01-01T08:00:00", "pollutant": "NO2",  "value": -5.0},
    {"station_id": "S2", "ts": "01/01/2026 09:00",    "pollutant": "NO2",  "value": 24.0},
    {"station_id": "S3", "ts": "2026-01-01T08:00:00", "pollutant": "O3",   "value": 2000.0},
    {"station_id": "S3", "ts": "2026-01-01T09:00:00", "pollutant": "O3",   "value": 30.0},
    {"station_id": "S4", "ts": "2026-01-01T08:00:00", "pollutant": "CO",   "value": "bad"},
]

def clean_and_count(readings):
    raise NotImplementedError

def rejection_reasons(readings):
    raise NotImplementedError
