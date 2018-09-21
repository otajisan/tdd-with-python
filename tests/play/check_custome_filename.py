'''
test module with prefix "check_"
'''


def some_func():
    '''return success message'''
    return 'Success'


def test_some_func():
    '''test for some func'''
    assert some_func() == 'Success'
