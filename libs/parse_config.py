class Config:
    def __init__(self):
        try:
            from configparser import ConfigParser
        except ImportError:
            from ConfigParser import ConfigParser # ver. > 3.0

        self.file = '/etc/domoticz/domoticz.conf'

        self.config = ConfigParser()
        self.config.read(self.file)

    def set_config(self, nfile):
        self.file = nfile

        self.config.read(nfile)

    def get_server_ip(self):
        return self.config.get('server' , 'ip')

    def get_server_port(self):
        # read values from a section
        return self.config.get('server', 'port')

    def get_sensors_count(self):
        return self.config.get('sensors', 'count')

    def get_sensor_name(self, idx):
        try:
            name = self.config.get('sensors', 'sensor' + str(idx))
        except:
            name = None

        return name

    def get_sensor_idx(self, name):
        try:
            idx = self.config.get(name, 'idx')
        except:
            idx = -1

        return idx

    def get_sensor_type(self, name):
        try:
            script = self.config.get(name, 'type')
        except:
            script = None

        return script

    def get_sensor_interval(self, name):
        try:
            interval = self.config.get(name, 'interval')
        except:
            interval = None

        return interval

