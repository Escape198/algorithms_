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
def remove_duplicates(nums: list) -> int:
    count = 0
    for i in nums:
        if count < 2 or i != nums[count - 2]:
            nums[count] = i
            count += 1
    return count


print(remove_duplicates([1, 1, 1, 2, 2, 3]))
