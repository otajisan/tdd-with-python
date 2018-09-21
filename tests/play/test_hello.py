'''
Test for Hello
'''
from otajisan.samples.tdd.play.hello import Hello

import pytest


def test_get_message():
    '''success get message'''
    obj = Hello()
    assert obj.get_message() == 'Hello World'


def test_say_hello(capsys):
    '''success return hello message'''
    obj = Hello()
    assert obj.say_hello() == 'Hello World'
    out, err = capsys.readouterr()
    assert out == 'Hello World\n'
    assert err == ''


@pytest.mark.parametrize('message',
                         ['Good Afternoon',
                          'Good Night',
                          'Good Morning'])
def test_say(capsys, message):
    '''success return given message'''
    obj = Hello()
    assert obj.say(message) == message
    out, err = capsys.readouterr()
    assert out == '{}\n'.format(message)
    assert err == ''


@pytest.mark.skip(reason='because of skip sample')
def test_skip_sample():
    '''this function should be skipped'''
    assert False


def test_use_sample_fixture(sample_fixture):
    '''use fixture sample'''
    assert True


def test_sample_monkeypatch(monkeypatch):
    '''use monckeypatch sample'''
    obj = Hello()
    monkeypatch.setattr(obj, 'say',
                        (lambda x: 'MonkeyPatch {}'.format(x)))
    assert obj.say('Test') == 'MonkeyPatch Test'
