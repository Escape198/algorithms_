

def title_to_number(title: str) -> int:
    return reduce(lambda x, y: x * 26 + y, map(lambda x: ord(x) - ord('A') + 1, title))


def reverse_bits(n: str) -> int:
    oribin = '{0:032b}'.format(n)
    reversebin = oribin[::-1]
    return int(reversebin, 2)


def hamming_weight(n: str) -> int:
    cnt = 0
    while n :
        cnt += 1
        n = n & (n-1)
    return cnt


def is_anagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def buddyStrings(self, s: str, goal: str) -> bool:
        dic = [[a, b] for a, b in zip(s, goal) if a != b]        
        return len(s) == len(goal) and (len(dic) == 2 and \
                        dic[0][0] ==dic [1][1] and dic[1][0] == dic[0][1] or \
                        (len(dic) == 0 and len(set(s)) < len(goal)))
