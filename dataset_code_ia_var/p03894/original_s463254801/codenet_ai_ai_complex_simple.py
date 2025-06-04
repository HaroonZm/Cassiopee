from functools import reduce
from operator import itemgetter

import sys
sys.setrecursionlimit(10 ** 7)
input = lambda: sys.stdin.readline()

N, Q = map(int, input().split())
AB = list(map(lambda _: tuple(map(int, input().split())), [None]*Q))

cup = (lambda n: list(range(n+2)))(N)
se = set(reduce(lambda acc, x: acc | {x}, (i for i in range(3)), set()))
ball = 1

swapper = lambda lst, a, b: lst.__setitem__(slice(a, b+1), [lst[b], lst[a]] if b == a+1 else [lst[a], lst[b]])
for a, b in AB:
    cup[a], cup[b] = cup[b], cup[a]
    ball = reduce(lambda p, q: p if cup[p] == 1 else (q if cup[q] == 1 else ball), [a, b], ball)
    se |= {cup[ball-1], cup[ball+1]}

try:
    se.remove(0)
except KeyError:
    pass

print((lambda x: reduce(lambda a, _: a+1, x, 0))(set(se)))