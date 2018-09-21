'''
Hello World
'''


class Hello:
    '''
    Say Hello World
    '''
    HELLO = 'Hello World'

    def __init__(self):
        '''initialize variables'''
        self.message = self.HELLO

    def get_message(self):
        '''execute'''
        return self.message

    def say(self):
        '''say message'''
        print(self.get_message())
        return self.get_message()
