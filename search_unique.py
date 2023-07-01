nums = list(range(1, 15**6))
nums += nums


def search_num(numbers: list) -> int:
    import operator
    import functools
    return functools.reduce(operator.xor, numbers)


print(search_num(nums))
