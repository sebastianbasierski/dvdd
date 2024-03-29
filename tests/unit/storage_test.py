from libs.storage import *


def test_storage():

    storage = Storage("1", "2")
    assert storage is not None

    first = storage.get_thread()
    assert first == '1'

    second = storage.get_sensor()
    assert second == '2'
