
import sqlite3

READINGS = [
    {"station_id": "S1", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 10.0},
    {"station_id": "S1", "ts": "2026-01-01T09:00:00", "pollutant": "PM25", "value": 20.0},
    {"station_id": "S1", "ts": "2026-01-01T10:00:00", "pollutant": "PM25", "value": 60.0},
    {"station_id": "S1", "ts": "2026-01-01T11:00:00", "pollutant": "PM25", "value": 40.0},
    {"station_id": "S2", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 5.0},
    {"station_id": "S2", "ts": "2026-01-01T09:00:00", "pollutant": "PM25", "value": 35.0},
    {"station_id": "S2", "ts": "2026-01-01T10:00:00", "pollutant": "PM25", "value": 15.0},
]

def top_n_per_station(readings, n):
    raise NotImplementedError

def rolling_avg(readings, station_id, pollutant, window):
    raise NotImplementedError
