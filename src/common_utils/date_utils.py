import datetime


def get_utc_now() -> datetime.datetime:
    return datetime.datetime.now(datetime.timezone.utc)
