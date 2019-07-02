def get_sensors_count():
    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0

    # instantiate
    config = ConfigParser()

    # parse existing file
    config.read('/etc/domoticz/domoticz.conf')

    # read values from a section
    count = config.get('sensors', 'count')
    return count

def get_sensor_name(idx):
    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0

    config = ConfigParser()

    config.read('/etc/domoticz/domoticz.conf')

    # read sensor name
    try:
        name = config.get('sensors', 'sensor' + str(idx))
    except:
        name = None

    return name

def get_sensor_idx(name):
    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0

    config = ConfigParser()

    config.read('/etc/domoticz/domoticz.conf')

    # read sensor name
    try:
        idx = config.get(name, 'idx')
    except:
        idx = -1

    return idx

def get_sensor_type(name):
    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0

    config = ConfigParser()

    config.read('/etc/domoticz/domoticz.conf')

    # read sensor name
    try:
        script = config.get(name, 'type')
    except:
        script = None

    return script

def get_sensor_interval(name):
    try:
        from configparser import ConfigParser
    except ImportError:
        from ConfigParser import ConfigParser  # ver. < 3.0

    config = ConfigParser()

    config.read('/etc/domoticz/domoticz.conf')

    # read sensor name
    try:
        interval= config.get(name, 'interval')
    except:
        interval = None

    return interval

