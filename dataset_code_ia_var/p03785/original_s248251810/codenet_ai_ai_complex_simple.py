from functools import reduce
from itertools import islice, accumulate, chain, groupby
import sys

input = lambda: sys.stdin.readline().strip()
mp = lambda: map(int, input().split())
lmp = lambda: list(map(int, input().split()))

n, c, k = mp()
t = sorted([int(input()) for _ in range(n)])

def compute(ans=1, count=1, idxs=None):
    idxs = list(range(1,n))
    def upd(acc, i):
        count, f, a = acc
        count += 1
        diff = t[i] - f
        if diff > k or count > c:
            return (1, t[i], a+1)
        else:
            return (count, f, a)
    return reduce(lambda acc, i: upd(acc, i), idxs, (1, t[0], 1))[2]

print(compute())