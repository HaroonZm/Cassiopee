import sys, os
from functools import reduce
from operator import add, mul
from itertools import accumulate, chain, islice, repeat
from collections import defaultdict

f = lambda: list(map(int, input().split()))

if any(map(lambda x: x == 'local', os.environ)):
    sys.stdin = open('./input.txt', 'r')

def deep_flatten(l):
    for el in l:
        if isinstance(el, (list, tuple)):
            yield from deep_flatten(el)
        else:
            yield el

def primedict(default):
    class PD(defaultdict):
        def __missing__(self, key):
            self[key] = default
            return default
    return PD

def idx_finder(t, i):
    return next(filter(lambda x: x[1] >= i, enumerate(accumulate(map(lambda x: x*2, t)))), (0,0))[0]

def convolve(v, i, idx):
    return min([v[i-1]+0.5, idx])

def solve():
    n, = f()
    t, v = f(), f()
    sumt = reduce(add, map(mul, t, repeat(2)), 0)
    vs = [10**8] * (sumt+1)
    vs[0] = 0
    pd = primedict(0)
    for i in range(1, sumt):
        idx = idx_finder(t, i)
        vs[i] = min(vs[i-1]+0.5, v[idx] if idx < len(v) else 10**8)
    vs[sumt] = 0
    for i in range(sumt-1, 0, -1):
        idx = idx_finder(t, i+1)
        vs[i] = reduce(min, filter(lambda x: x is not None, [vs[i+1]+0.5, vs[i], v[idx] if idx < len(v) else None]))
    ans = reduce(add, map(lambda i: (vs[i]+vs[i+1])/4, range(sumt)), 0)
    print(ans)

solve()