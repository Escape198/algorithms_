from memory_profiler import profile

import time


nums = list(range(1, 30**5))
nums += nums


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.monotonic()
        retval = func(*args, **kwargs)
        after = time.monotonic() - before
        print(f"Function {func.__name__}: {after} seconds")
        return retval
    return wrapper


@profile
@timer
def search_num(numbers: list) -> int:
    import operator
    import functools
    return functools.reduce(operator.xor, numbers)


print(search_num(nums))
