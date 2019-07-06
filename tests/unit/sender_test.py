import pytest
from libs.sender import *

ip = '172.16.2.40'
port = '8080'


def test_sender_creation():

    sender = Sender(ip, port, 0)
    assert sender is not None


def test_sender_send():

    sender = Sender(ip, port, 0)
    assert sender is not None

    ret = sender.send(None)
    assert ret is False

    ret = sender.send("X")
    assert ret is True


def test_sender_set_idx():

    sender = Sender(ip, port, 1)
    assert sender is not None

    assert sender.idx == 1
