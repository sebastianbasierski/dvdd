import os


def get_platform():
    return os.uname()[4][:3]


def get_config_file_path():
    return os.getcwd() + '/domoticz.conf'
