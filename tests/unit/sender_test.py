from libs.sender import Sender

ip = '172.16.2.40'
port = '8080'


def test_sender_creation():

    sender = Sender(ip, port, 0)
    assert sender is not None


def test_sender_send():

    sender = Sender(ip, port, 0)
    assert sender is not None

    ret = sender.send(None)
    assert ret == -1

    ret = sender.send('hello')
    assert (ret == -2) or (ret == 0)


def test_sender_set_idx():

    sender = Sender(ip, port, 1)
    assert sender is not None
    assert sender.idx == 1
