import pytest
from libs.parse_config import *


def test_get_sensors_count():
    count = get_sensors_count()
    assert count == '1'
    assert int(count) == 1

