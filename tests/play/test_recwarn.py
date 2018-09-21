'''
Sample use recwarn
'''
import warnings


def invalid_function():
    '''
    sample for test
    '''
    warnings.warn(
        'this function is invalid. will End Of Life.',
        DeprecationWarning
    )


def test_invalid_function(recwarn):
    '''check warnings'''
    invalid_function()
    assert len(recwarn) == 1
    w = recwarn.pop()
    assert w.category == DeprecationWarning
    assert str(w.message) == 'this function is invalid. will End Of Life.'
