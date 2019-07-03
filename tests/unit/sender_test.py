import pytest
from libs.sender import *

ip = '172.16.2.40'
port = '8080'

def test_sender_creation():
    
    sender = Sender(ip, port, 0)
    assert sender != None

def test_sender_send():

    sender = Sender(ip, port, 0)
    assert sender != None

    ret = sender.send(None)
    assert ret == False

    ret = sender.send("X")
    assert ret == True

def test_sender_set_idx():

    sender = Sender(ip, port, 1)
    assert sender != None

    assert sender.idx == 1
