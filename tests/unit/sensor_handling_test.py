import pytest
from libs.parse_config import *
from libs.sensor_handling import *


def test_handle_sensor():
        
    count = get_sensors_count()
    assert count == '1'
    assert int(count) == 1

    name = get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    sensor = Sensor(name)
    assert sensor != None

    done = sensor.handle_sensor(True)
    assert done == True



