import os


def get_platform():
    return os.uname()[4][:3]


