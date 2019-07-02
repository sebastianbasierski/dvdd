import pytest
from libs.sender import *


def test_sender_creation():
    
    ip = '172.16.2.40'
    port = '8080'

    sender = Sender(ip, port)
    assert sender != None

def test_sender_send():

    ip = '172.16.2.40'
    port = '8080'

    sender = Sender(ip, port)
    assert sender != None

    ret = sender.send()
    assert ret ==True
