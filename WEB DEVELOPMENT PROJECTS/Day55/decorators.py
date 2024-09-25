import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(1)
        function()
    return wrapper_function

  
@delay_decorator
def say_hello():
    print('hello')

say_hello()