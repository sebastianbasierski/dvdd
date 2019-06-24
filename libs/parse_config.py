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


