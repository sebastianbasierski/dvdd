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
