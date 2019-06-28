#!/usr/bin/python
import sys
import signal
from threading import Thread
from libs.parse_config import *
from libs.sensor_handling import *

thread = None

def signal_handler(sig, frame):
    print "Your pressed ctrl + c"
    hs_stop()
    thread.join()
    sys.exit(0)

def sensor_thread(idx):
    sensor = get_sensor_name(idx)
    done = handle_sensor(sensor)

def main():
    global thread
    count = get_sensors_count()

    thread = Thread(target=sensor_thread, args=(1,))
    thread.start()
       
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    while True:
        signal.pause()

