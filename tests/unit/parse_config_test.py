import pytest
from libs.parse_config import *


def test_get_sensors_count():
    count = get_sensors_count()
    assert count == '1'
    assert int(count) == 1

def test_get_sensor_name():
    name = get_sensor_name(1)
    assert name == 'rpi_cpu_temp'

    name = get_sensor_name(0)
    assert name == None

