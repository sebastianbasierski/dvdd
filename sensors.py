#!/usr/bin/python
import sys
import signal
from threading import Thread
from libs.parse_config import *
from libs.sensor_handling import *

thread = []
sensor = []

def signal_handler(sig, frame):
    global thread
    global sensor

    print "Your pressed ctrl + c"

    for s in sensor:
        s.hs_stop()

    for t in thread:
        t.join()

    sys.exit(0)

def sensor_thread(idx):
    global sensor

    s = sensor[idx].handle_sensor()

def main():
    global thread
    global sensor

    count = get_sensors_count()

    for idx in range(int(count)):
        print "idx " + str(idx)

        temp_sensor = Sensor(get_sensor_name(idx))
        sensor.append(temp_sensor)

        temp_thread = Thread(target=sensor_thread, args=(idx,))
        thread.append(temp_thread)

    for t in thread:
        t.start()
       
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    while True:
        signal.pause()

