from itertools import count, islice, product
from functools import reduce
from operator import eq

def listing(char, s):
    return list(map(lambda x: x[0], filter(lambda p: p[1] == char, enumerate(s))))

def signboard(s, t):
    if s in t:
        return True
    idx_l = list(map(listing, s[:2], [t]*2))
    if any(map(lambda l: not l, idx_l)): return False
    combos = ((a, b) for a, b in product(*idx_l) if a < b)
    def match(a, b):
        step = b - a
        indices = (a + i*step for i in range(len(s)))
        try:
            return all(map(eq, s, (t[i] for i in indices)))
        except IndexError:
            return False
    return any(map(lambda ab: match(*ab), combos))

n = int(input())
a = input().strip()
S = list(islice((input().strip() for _ in count()), n))
print(sum(map(lambda b: signboard(a, b), S)))