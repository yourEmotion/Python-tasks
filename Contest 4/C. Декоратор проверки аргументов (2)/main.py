import sys
import functools


def takes(*types):
    def wraps(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for index in range(min(len(types), len(args))):
                if not isinstance(args[index], types[index]):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return wraps


@takes(str)
def f(*args):
    print(*args)


try:
    f('hi', 'hi')
except Exception as e:
    print(type(e).__name__)

