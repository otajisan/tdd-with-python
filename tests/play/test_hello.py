'''
Test for Hello
'''
from otajisan.samples.tdd.play.hello import Hello


def test_get_message():
    '''success get message'''
    obj = Hello()
    assert obj.get_message() == 'Hello World'


def test_say():
    '''success print message'''
    obj = Hello()
    assert obj.say() == 'Hello World'
