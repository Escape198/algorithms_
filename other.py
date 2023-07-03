

def title_to_number(title: str) -> int:
    return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, title))


def reverse_bits(n: str) -> int:
    oribin = '{0:032b}'.format(n)
    reversebin = oribin[::-1]
    return int(reversebin, 2)
