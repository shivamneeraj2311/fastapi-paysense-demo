import pytest
import datetime
from src.common_utils.date_utils import get_utc_now


def test_get_utc_now():
    assert get_utc_now().strftime("%Y-%m-%d %H:%M:%S %Z") == datetime.datetime.now(
        datetime.timezone.utc
    ).strftime("%Y-%m-%d %H:%M:%S %Z")
