import pytest
from libs.parse_config import *
from libs.sensor_handling import *


def test_handle_sensor():
    config = Config()
    count = config.get_sensors_count()
    assert count == '3'
    assert int(count) == 3

    name = config.get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    sensor = Sensor(name, config)
    assert sensor is not None

    done = sensor.handle_sensor(True)
    assert done is True


def test_get_json():
    config = Config()
    count = config.get_sensors_count()
    assert count == '3'
    assert int(count) == 3

    name = config.get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 1
    sensor.stype = "temperature"
    json = sensor.get_json()
    assert json is not None


def test_get_ds1820_json():
    config = Config()
    count = config.get_sensors_count()
    assert count == '3'
    assert int(count) == 3

    name = config.get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 1
    json = sensor.get_ds1820_temperature_json()
    assert json is not None


def test_get_cpu_json():
    config = Config()
    count = config.get_sensors_count()
    assert count == '3'
    assert int(count) == 3

    name = config.get_sensor_name(0)
    assert name == 'rpi_cpu_temp'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 1
    json = sensor.get_cpu_temperature_json()
    assert json is not None


def test_get_button_json():
    config = Config()
    count = config.get_sensors_count()
    assert count == '3'
    assert int(count) == 3

    name = config.get_sensor_name(2)
    assert name == 'rpi_button'

    sensor = Sensor(name, config)
    assert sensor is not None

    sensor.idx = 6
    json = sensor.get_button_json()
    assert json is not None
