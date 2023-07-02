from memory_profiler import profile

import random
import time


numbers = list(range(1, 30**5))
k = len(numbers)
num = random.randint(1, 30**5)


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
def binary_search(nums: list, x: int) -> int:
    left = 0
    right = k-1
    while right > left + 1:
        middle = (left + right) // 2
        if nums[middle] > x:
            right = middle
        else:
            left = middle
    return right


print(binary_search(numbers, num))

