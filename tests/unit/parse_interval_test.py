import pytest
from libs.parse_interval import *


def test_get_sensors_parse_interval():
    count = get_sensors_parse_interval('30s')
    assert count == 30
    assert int(count) == 30

    count = get_sensors_parse_interval('-2s')
    assert count is None

    count = get_sensors_parse_interval('-3')
    assert count is None

    count = get_sensors_parse_interval('1m')
    assert count == 60
    assert int(count) == 60

    count = get_sensors_parse_interval('2m:3s')
    assert count == 123
    assert int(count) == 123

    count = get_sensors_parse_interval('0m:12s')
    assert count == 12
    assert int(count) == 12

    count = get_sensors_parse_interval('2h:3m:4s')
    assert count == 7384
    assert int(count) == 7384

    count = get_sensors_parse_interval('x')
    assert count is None

    count = get_sensors_parse_interval('xs')
    assert count is None
