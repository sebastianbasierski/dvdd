from libs.helpers import get_platform


def test_get_platform():
    p = get_platform()
    assert p is not None
#    assert p == "arm"
