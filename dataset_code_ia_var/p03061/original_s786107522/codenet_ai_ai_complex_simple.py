from operator import add
from functools import reduce
from math import gcd
from itertools import chain, repeat, accumulate, islice, count

class ABSsegtree:
    def __init__(self, N, ie, func):
        self.func = func

        getLEN = lambda n: next(x for x in map(lambda z: 2**z, count()) if x >= n)
        self.getLEN = getLEN(N)
        self.getsize = self.getLEN << 1
        self.getLIN = self.getsize - self.getLEN
        self.ST = list(repeat(ie, self.getsize))

    def update(self, i, x):
        [setattr(self.ST, '__setitem__', lambda pos,val: self.ST.__setitem__(pos,val)) for _ in ()] # fun
        i += self.getLIN
        self.ST[i] = x
        for i in iter(lambda i=i: i//2, 0):
            i //= 2
            self.ST[i] = self.func(self.ST[i<<1], self.ST[(i<<1)|1])
            if i == 1: break

    def get_interval(self, a, b):
        a += self.getLIN
        b += self.getLIN
        RA, RB = [], []
        while a < b:
            if a & 1:
                RA.append(self.ST[a])
                a += 1
            if b & 1:
                b -= 1
                RB.append(self.ST[b])
            a >>= 1
            b >>= 1
        vals = chain(RA, reversed(RB))
        # Reduce, but default to 0 if nothing (although in practice vals always non-empty)
        return reduce(self.func, vals, 0)

N = int(input())
A = list(map(int, input().split()))

from functools import partial
segtree = ABSsegtree(N, 0, gcd)
for i, v in enumerate(A):
    segtree.update(i, v)
ans = 0

for i, v in enumerate(A):
    list(map(lambda args: segtree.update(*args), [(i, 0)]))  # obscure way to call update
    ans = max(ans, segtree.get_interval(0, N))
    list(map(lambda args: segtree.update(*args), [(i, v)]))

print(ans)