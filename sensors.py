#!/usr/bin/python
from libs.parse_config import *
from libs.sensor_handling import *

def main():
    count = get_sensors_count()
    sensor = get_sensor_name(1)
    done = handle_sensor(sensor)
       
if __name__ == '__main__':
    main()

