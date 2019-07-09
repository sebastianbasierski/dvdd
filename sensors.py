#!/usr/bin/python
import sys
import signal
from libs.server import *
from libs.storage import *
from threading import Thread
from libs.parse_config import *
from libs.sensor_handling import *

storage = []
server = None
server_thread = None


def signal_handler(sig, frame):
    global storage
    global server

    print "Your pressed ctrl + c"

    for s in storage:
        s.get_sensor().stop()
        s.get_thread().join()

    server.stop()
    server_thread.join()

    sys.exit(0)


def sensor_thread(idx):
    global storage

    s = storage[idx].get_sensor().handle_sensor()


def server_thread():
    global server

    s = server.run_thread()


def main():
    global server_thread
    global storage
    global server

    config = Config()
    ret = config.set_config('/domoticz/domoticz.conf')
    if ret is False:
        print "Wrong config file set"
        exit (1)

    count = config.get_sensors_count()

    for idx in range(int(count)):
        sensor = Sensor(config.get_sensor_name(idx), config)
        thread = Thread(target=sensor_thread, args=(idx,))
        storage.append(Storage(thread, sensor))

    for s in storage:
        s.get_thread().start()

    server = Server(int(config.get_local_port()))
    server_thread = Thread(target=server_thread, args=())
    server_thread.start()


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()
    while True:
        signal.pause()
