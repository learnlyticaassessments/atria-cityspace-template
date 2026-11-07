def validate_request(payload):
    """Return "OK" if the /predict payload has a non-empty string station_id, a
    pollutant in {"PM25","PM10","NO2","O3"}, and a non-negative numeric value.
    Otherwise return the first failing code: "MISSING_FIELD", then "BAD_POLLUTANT",
    then "BAD_VALUE"."""
    pass

def handle_predict(payload):
    """If validate_request != "OK" return {"status":400,"error":<code>}. Else return
    {"status":200,"pollutant":<name>,"prediction":round(value*1.05 + offset, 2)}
    with offsets PM25=2.0, PM10=1.5, NO2=1.0, O3=0.5."""
    pass
