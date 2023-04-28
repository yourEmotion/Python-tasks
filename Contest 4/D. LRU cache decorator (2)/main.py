import functools
from collections import defaultdict


def cache(size: int):
    def wraps(func):
        function_executions = defaultdict()
        lru_values = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            value = str(args) + str(kwargs)
            if value not in function_executions:
                if size == len(lru_values):
                    function_executions.pop(lru_values.pop(0))
                function_executions[value] = func(value)
                lru_values.append(value)
            return function_executions[value]
        return wrapper
    return wraps
