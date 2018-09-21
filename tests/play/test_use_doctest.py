'''
Test for use_doctest
'''
import otajisan.samples.tdd.play.use_doctest as ud


def test_add():
    '''
    return added number
    '''
    assert ud.add(5, 3) == 8
