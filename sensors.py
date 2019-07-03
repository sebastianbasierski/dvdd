#!/usr/bin/python
import sys
import signal
from libs.storage import *
from threading import Thread
from libs.parse_config import *
from libs.sensor_handling import *

storage = []

def signal_handler(sig, frame):
    global storage

    print "Your pressed ctrl + c"

    for s in storage:
        s.get_sensor().stop()
        s.get_thread().join()

    sys.exit(0)

def sensor_thread(idx):
    global storage

    s = storage[idx].get_sensor().handle_sensor()

def main():
    global storage

    count = get_sensors_count()

    for idx in range(int(count)):
        sensor = Sensor(get_sensor_name(idx))
        thread = Thread(target=sensor_thread, args=(idx,))
        storage.append(Storage(thread, sensor))

    for s in storage:
        s.get_thread().start()
       
if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    while True:
        signal.pause()

