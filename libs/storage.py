class Storage:
    def __init__(self, thread, sensor):
        self.thread = thread
        self.sensor = sensor

    def get_thread(self):
        return self.thread

    def get_sensor(self):
        return self.sensor
