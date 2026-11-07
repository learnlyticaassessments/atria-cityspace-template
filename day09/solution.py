
import sqlite3

READINGS = [
    {"station_id": "S1", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 42.0},
    {"station_id": "S1", "ts": "2026-01-01T09:00:00", "pollutant": "PM25", "value": 50.0},
    {"station_id": "S2", "ts": "2026-01-01T08:00:00", "pollutant": "NO2",  "value": 18.0},
    {"station_id": "S1", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 42.0},
    {"station_id": "S3", "ts": "2026-01-01T08:00:00", "pollutant": "O3",   "value": 12.0},
    {"station_id": "S2", "ts": "2026-01-01T09:00:00", "pollutant": "NO2",  "value": 24.0},
]

def load_readings(readings):
    raise NotImplementedError

def row_count(conn):
    raise NotImplementedError

def distinct_pollutants(conn):
    raise NotImplementedError

def station_totals(conn):
    raise NotImplementedError
