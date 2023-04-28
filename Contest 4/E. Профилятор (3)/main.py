from time import time
import functools


def profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not wrapper.was_called:
            wrapper.calls = 0
            wrapper.rec_depth = 0
            wrapper.was_called = True
            wrapper.last_time_taken = 0

        wrapper.rec_depth += 1
        wrapper.calls += 1
        begin_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        wrapper.rec_depth -= 1
        wrapper.last_time_taken = end_time - begin_time

        if wrapper.rec_depth == 0:
            wrapper.was_called = False
            wrapper.last_time_taken = 0

        return result

    wrapper.was_called = False
    return wrapper
