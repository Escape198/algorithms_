from memory_profiler import profile

import random
import time


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
def int_to_roman(num: int) -> str:
    num_map = {
        1: "I",
        5: "V", 4: "IV",
        10: "X", 9: "IX",
        50: "L", 40: "XL",
        100: "C", 90: "XC",
        500: "D", 400: "CD",
        1000: "M", 900: "CM",
    }

    # Result Variable
    r = ''

    for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        # If n in list then add the roman value to result variable
        while n <= num:
            r += num_map[n]
            num -= n
    return r


num = random.randint(1, 4**5)
print(num, int_to_roman(num), sep=':')
