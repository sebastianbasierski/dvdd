import pytest
from libs.storage import *


def test_storage():
 
    storage = Storage("1", "2")
    assert storage != None

    first = storage.get_thread()
    assert first == '1'

    second = storage.get_sensor()
    assert second == '2'

