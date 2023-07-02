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
def triangle(numRows: int) -> list:
    s = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != i and j != 0:
                row[j] = s[i - 1][j - 1] + s[i - 1][j]
        s.append(row)
    return s


x = 5
print(generate(x))
