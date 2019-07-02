import pytest
from libs.sender import *


def test_sender():
    
    ip = '172.16.2.40'
    port = '8080'

    sender = Sender(ip, port)
    assert sender != None


