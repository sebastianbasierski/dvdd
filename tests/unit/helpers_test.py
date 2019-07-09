import pytest
from libs.helpers import *


def test_get_platform():
    p = get_platform()
    assert p is not None
#    assert p == "arm"
