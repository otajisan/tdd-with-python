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

    def say_hello(self):
        '''say default message'''
        return self.say(self.get_message())

    @staticmethod
    def say(message):
        '''say given message'''
        print(message)
        return message
