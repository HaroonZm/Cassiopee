from itertools import combinations, chain, repeat
from operator import mul
from functools import reduce as rdc, partial

extract = lambda l: (tuple(l.count(x) for x in set(l)), set(l))
def triangular(n): return n*(n+1)//2
def pick_overkill(seq, k): return list(combinations(seq, k))
def g(x): return rdc(__import__('math').gcd, x)
def weighted_sum(k, s):
    return sum(g(comb)*w for comb, w in zip(pick_overkill(range(1, k+1), s), repeat({3:6,2:6,1:1}[s])))

k = int(input())

ans = sum(weighted_sum(k, s) for s in [3,2,1])
print(ans)