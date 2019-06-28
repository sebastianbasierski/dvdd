import pytest
from libs.parse_config import *


def test_get_sensors_count():
    count = get_sensors_count()
    assert count == '1'
    assert int(count) == 1

def test_get_sensor_name():
    name = get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    name = get_sensor_name(1)
    assert name == None

def test_get_sensor_idx():
    idx = get_sensor_idx('rpi_cpu_temp')
    assert idx == '0'
    assert int(idx) == 0

    idx = get_sensor_idx('rpi_cppu_temp')
    assert int(idx) == -1

def test_get_sensor_script():
    script = get_sensor_script('rpi_cpu_temp')
    assert script == 'cpu_temp.py'

    script = get_sensor_script('rpi_cppu_temp')
    assert script == None

def test_get_sensor_interval():
    interval = get_sensor_interval('rpi_cpu_temp')
    assert interval == '30s'

    interval = get_sensor_interval('rpi_cppu_temp')
    assert interval == None

