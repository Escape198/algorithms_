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
def simplify_path(path):
    stack = []
    path = path.split('/')
    for p in path:
        if not p or p == '.':
            continue
        elif p == '..':
            if stack:
                stack.pop()
        else:
            stack.append(p)
    root = "/"
    return root + "/".join(stack)


print(simplify_path("/ home // foo/"))
