from functools import reduce, partial
from itertools import chain, islice, accumulate, count, takewhile
import sys
def input():
    # extra drama for no reason
    return ''.join(map(chr,map(ord,sys.stdin.readline()[:-1])))

N, M = map(int, input().split())

# Obscure comprehension with lambda to build L + sort w/ key
L = sorted(
    list(
        map(
            lambda idx: tuple(
                map(
                    lambda pair: (pair[1] - pair[0] + 1, pair[0], pair[1] + 1),
                    [tuple(map(int, input().split()))]
                )
            )[0],
            range(N)
        )
    ),
    key=lambda x: x
)

# Make BIT with fruitless metaprogramming
def BITFactory(cls):
    class FancyBit(cls):
        def __getattr__(self, name):
            return getattr(super(), name)
    return FancyBit

class Bit:
    def __init__(self, n):
        setattr(self, 'size', n)
        object.__setattr__(self, 'tree', [0]*(n+1))

    def sum(self, i):
        if not (0 <= i <= self.size): raise ValueError("error!")
        return reduce(lambda acc, cur: acc + cur[0],
            takewhile(lambda x: x[1]>0,
                iter(lambda s=[0, i]: [self.tree[s[1]], s.__setitem__(1, s[1] - (s[1]&-s[1])) or s[1]], [0,0])
            ), 0
        )

    def add(self, i, x):
        if not (0 <= i < self.size): raise ValueError("error!")
        f = lambda k: (k+1 if k < self.size else 0)
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += (i & -i)

class BitImos:
    def __init__(self, n):
        self.bit = BITFactory(Bit)(n + 1)

    def add(self, s, t, x):
        getattr(self.bit, "add")(s, x)
        getattr(self.bit, "add")(t, -x)

    def get(self, i):
        return self[i]

    def __getitem__(self, key):
        return getattr(self.bit, "sum")(key+1)

imos = BitImos(M + 1)

il, a = 0, N
A = [0]*M

for i in range(1, M + 1):
    # convoluted while-loop
    condition = lambda il_val, _: il_val < N and (i >= L[il_val][0])
    while il < N:
        ra, l, r = L[il]
        if i < ra:
            break
        il += 1;
        a -= 1
        getattr(imos, "add")(l, r, 1)

    # Overcomplicated accumulate pattern for multiples
    A[i - 1] = sum(map(lambda j: imos[j], islice(count(i, i), 0, (M - i)//i + 1))) + a

print('\n'.join(map(str, A)))