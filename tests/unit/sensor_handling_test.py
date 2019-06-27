import pytest
from libs.parse_config import *
from libs.sensor_handling import *


def test_handle_sensor():
        
    count = get_sensors_count()
    assert count == '1'
    assert int(count) == 1

    sensor = get_sensor_name(1)
    assert sensor == 'rpi_cpu_temp'

    done = handle_sensor(sensor, True)
    assert done == True



