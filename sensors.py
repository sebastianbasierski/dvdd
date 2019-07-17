#!/usr/bin/python
import sys
import signal
from libs.server import Server
from libs.storage import *
from threading import Thread
from libs.parse_config import Config
from libs.sensor_handling import Sensor


class Main():
    def __init__(self):
        self.storage = []
        self.server = None
        self.server_thread = None

    def sensor_thread(self, idx):
        self.storage[idx].get_sensor().handle_sensor()

    def local_server_thread(self):
        self.server.run_thread()

    def stop(self):
        for s in self.storage:
            s.get_sensor().stop()
            s.get_thread().join()

        self.server.stop()
        self.server_thread.join()

    def start(self):
        config = Config()
        ret = config.set_config('/etc/domoticz/domoticz.conf')
        if ret is False:
            print("Wrong config file set")
            return -1

        count = config.get_sensors_count()

        for idx in range(int(count)):
            try:
                sensor = Sensor(config.get_sensor_name(idx), config)
            except ValueError:
                sensor = None

            if sensor is not None:
                thread = Thread(target=self.sensor_thread, args=(idx,))
                self.storage.append(Storage(thread, sensor))

        for s in self.storage:
            s.get_thread().start()

        self.server = Server(config)
        self.server_thread = Thread(target=self.local_server_thread, args=())
        self.server_thread.start()
        return 0


if __name__ == '__main__':
    sensors = Main()
    ret = sensors.start()
    if ret == -1:
        exit(1)

    def signal_handler(*args):
        print("Your pressed ctrl + c")
        sensors.stop()
        print("stopped sensors")
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    while True:
        signal.pause()
