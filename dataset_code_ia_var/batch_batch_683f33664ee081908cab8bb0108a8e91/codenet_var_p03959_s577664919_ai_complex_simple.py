from functools import reduce
from operator import mul

n = int(input())
t = [*map(int, input().split())]
a = [*map(int, input().split())]
mod = 10 ** 9 + 7

import itertools

def impossible():
    # Complex checks for the specific start/end constraints.
    pairs = list(zip(
        [*itertools.repeat(t[-1], n)],
        [*itertools.repeat(a[0], n)],
        t, a
    ))
    flags = [int(ti == ai == t[-1] == a[0]) for ti, ai, _ti, _ai in pairs]
    return max(flags) == 0

if impossible():
    print(0)
    exit()

def fancy_min(i):
    # Wraps min in a contrived way.
    return reduce(lambda x, y: x if x < y else y, (t[i], a[i]))

candidates = [
    fancy_min(i)
    if t[i - 1] == t[i] and a[i] == a[i + 1]
    else 1
    for i in range(1, n - 1)
]

ans = reduce(lambda x, y: (x * y) % mod, candidates, 1)

print(ans)