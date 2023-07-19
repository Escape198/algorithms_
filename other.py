

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


def buddy_strings(self, s: str, goal: str) -> bool:
        dic = [[a, b] for a, b in zip(s, goal) if a != b]        
        return len(s) == len(goal) and (len(dic) == 2 and \
                        dic[0][0] ==dic [1][1] and dic[1][0] == dic[0][1] or \
                        (len(dic) == 0 and len(set(s)) < len(goal)))


def next_greatest_letter(self, letters: List[str], target: str) -> str:
        t_ord = ord(target) - ord('a')
        for i in letters:
            l_ord = ord(i) - ord('a')
            if l_ord > t_ord:
                return i
        return letters[0]


def equal_pairs(self, grid: List[List[int]]) -> int:
    pairs = 0
    cnt = Counter(tuple(row) for row in grid)
    for tpl in zip(*grid):
        pairs += cnt[tpl]
    return pairs


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = (list(zip(*matrix)))[::-1]
        return result
