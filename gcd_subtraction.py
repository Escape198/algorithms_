from memory_profiler import profile
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


@profile
@timer
def binary_gcd(num1: int, num2: int) -> int:
    shift = 0
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    while (num1 | num2) & 1 == 0:
        shift += 1
        num1 >>= 1
        num2 >>= 1
    while num1 & 1 == 0:
        num1 >>= 1
    while num2 != 0:
        while num2 & 1 == 0:
            num2 >>= 1
        if num1 > num2:
            num1, num2 = num2, num1
        num2 -= num1
    return num1 << shift


x, y = 32032, 360000144
print(gcd_rem_division(x, y))
print(gcd_extended(x, y))
print(binary_gcd(x, y))
