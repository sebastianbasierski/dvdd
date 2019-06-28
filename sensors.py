#!/usr/bin/python
from threading import Thread
from libs.parse_config import *
from libs.sensor_handling import *

def sensor_thread(idx):
    sensor = get_sensor_name(idx)
    done = handle_sensor(sensor)

def main():
    count = get_sensors_count()

    t = Thread(target=sensor_thread, args=(1,))
    t.start()
       
if __name__ == '__main__':
    main()

