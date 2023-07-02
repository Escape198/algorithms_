from memory_profiler import profile
import time


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.monotonic()
        retval = func(*args, **kwargs)
        after = time.monotonic() - before
        print("Function {}: {} seconds".format(func.__name__, after))
        return retval
    return wrapper


@profile
@timer
def gcd_rem_division(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


@profile
@timer
def gcd_extended(num1: int, num2: int) -> tuple:
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


print(gcd_rem_division(320, 3600))
print(gcd_extended(320, 3600))
