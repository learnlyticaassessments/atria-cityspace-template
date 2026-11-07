ALLOWED = ("co", "no2", "o3", "pm10", "pm25", "so2")

def validate_reading(raw):
    # TODO: return a sorted list of error codes for the raw reading dict.
    # Codes: station_id_missing, ts_missing, pollutant_unknown,
    #        value_not_number, value_negative. Empty list means valid.
    pass

def normalize_reading(raw):
    # TODO: if valid, return a coerced dict with keys
    # station_id, ts, pollutant (lowercased), value (float round 2).
    # If invalid, return {}.
    pass
