import random
import time


numbers = list(range(1, 10**4))
k = len(numbers)
random.shuffle(numbers)


def timer(func):
    def wrapper(*args, **kwargs):
        before = time.monotonic()
        retval = func(*args, **kwargs)
        after = time.monotonic() - before
        print("Function {}: {} seconds".format(func.__name__, after))
        return retval
    return wrapper


@timer
def insert_sort(nums: list) -> list:
    nums = nums.copy()
    for i in range(k-1):
        m = i
        for j in range(i+1, k):
            if numbers[j] < numbers[m]:
                m = j
        numbers[i], numbers[m] = numbers[m], numbers[i]
    return nums


@timer
def choice_sort(nums: list) -> list:
    nums = nums.copy()
    for i in range(k-1):
        for j in range(i+1, k):
            if nums[j] < nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
    return nums


@timer
def bubble_sort(nums: list) -> list:
    nums = nums.copy()
    for i in range(1, k):
        for j in range(0, k-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def quick_sort(nums: list) -> list:
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        list1 = [elem for elem in nums if elem < q]
        list2 = [q] * nums.count(q)
        list3 = [elem for elem in nums if elem > q]
        return quick_sort(list1) + list2 + quick_sort(list3)


choice_sort(numbers)
insert_sort(numbers)
bubble_sort(numbers)
quick_sort(numbers)
