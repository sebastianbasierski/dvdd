#!/usr/bin/python
import sys
import signal
from threading import Thread
from libs.parse_config import *
from libs.sensor_handling import *

thread = None
sensor = None

def signal_handler(sig, frame):
    global sensor

    print "Your pressed ctrl + c"
    sensor.hs_stop()
    thread.join()
    sys.exit(0)

def sensor_thread(idx):
    global sensor

    sensor = sensor.handle_sensor()

def main():
    global thread
    global sensor

    count = get_sensors_count()

    sensor = Sensor(get_sensor_name(1))

    thread = Thread(target=sensor_thread, args=(1,))
    thread.start()
       
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    while True:
        signal.pause()

