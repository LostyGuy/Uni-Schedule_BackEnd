import datetime as dt

def current_time() -> dt:
    return dt.datetime.now()

def current_timestamp() -> float:
    return dt.datetime.now(tz=dt.timezone.utc).timestamp()
    