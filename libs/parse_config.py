import os


class Config:
    def __init__(self):
        try:
            from configparser import ConfigParser
        except ImportError:
            from ConfigParser import ConfigParser  # ver. > 3.0

        self.config_file_set = False
        self.config = ConfigParser()

        self.set_config('/etc/domoticz/domoticz.conf')

    def set_config(self, nfile):
        self.file = nfile

        ret = os.path.isfile(self.file)
        if ret is False:
            self.config_file_set = False
            return False

        self.config.read(nfile)
        self.config_file_set = True

        return True

    def read_config(self, section, key):
        if self.config_file_set is False:
            return None
        return self.config.get(section, key)

    def get_server_ip(self):
        return self.read_config('server', 'ip')

    def get_server_port(self):
        # read values from a section
        return self.read_config('server', 'port')

    def get_sensors_count(self):
        return self.read_config('sensors', 'count')

    def get_sensor_name(self, idx):
        try:
            name = self.read_config('sensors', 'sensor' + str(idx))
        except:
            name = None

        return name

    def get_sensor_idx(self, name):
        try:
            idx = self.read_config(name, 'idx')
        except:
            idx = -1

        return idx

    def get_sensor_type(self, name):
        try:
            script = self.read_config(name, 'type')
        except:
            script = None

        return script

    def get_sensor_interval(self, name):
        try:
            interval = self.read_config(name, 'interval')
        except:
            interval = None

        return interval

    def get_debug(self):
        return self.read_config('general', 'debug')

    def get_local_port(self):
        return self.read_config('general', 'local_port')

    def get_gpio(self, name):
        try:
            gpio = self.read_config(name, 'gpio')
        except:
            gpio = None

        return gpio
