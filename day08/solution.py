
import statistics

READINGS = [
    {"station_id": "S1", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 40.0},
    {"station_id": "S1", "ts": "2026-01-01T20:00:00", "pollutant": "PM25", "value": 60.0},
    {"station_id": "S1", "ts": "2026-01-02T08:00:00", "pollutant": "PM25", "value": 20.0},
    {"station_id": "S2", "ts": "2026-01-01T08:00:00", "pollutant": "NO2",  "value": 10.0},
    {"station_id": "S2", "ts": "2026-01-02T08:00:00", "pollutant": "NO2",  "value": 30.0},
    {"station_id": "S3", "ts": "2026-01-01T08:00:00", "pollutant": "PM25", "value": 10.0},
    {"station_id": "S3", "ts": "2026-01-01T09:00:00", "pollutant": "PM25", "value": 50.0},
]

def avg_by_pollutant(readings):
    raise NotImplementedError

def median_value(readings, pollutant):
    raise NotImplementedError

def resample_daily_mean(readings, pollutant):
    raise NotImplementedError
