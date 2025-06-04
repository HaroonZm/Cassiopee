from functools import reduce
from itertools import accumulate, takewhile, repeat, islice
from operator import ior, iand
from bisect import bisect_left

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        # accumulation with generator, reducing i until 0
        def index_gen(ii):
            while ii > 0:
                yield ii
                ii -= ii & -ii
        return sum(map(self.tree.__getitem__, index_gen(i)))

    def add(self, i, x):
        # clever usage of generator, closure, and operator
        def add_loop(idx=self, pos=i+1, val=x):
            while pos <= idx.size:
                idx.tree[pos] += val
                pos += pos & -pos
        list(map(lambda _: None, repeat(0,1))) or add_loop()

    def bsearch(self, x):
        # Bitwise trick with functional reduction
        h = self.size.bit_length()
        pos = 0
        for pw in map(lambda e: 1 << e, reversed(range(h))):
            if pos + pw <= self.size and self.tree[pos + pw] < x:
                x -= self.tree[pos + pw]
                pos += pw
        return pos + 1

n, q = map(int, input().split())
a = list(map(int, input().split()))
bit = BIT(n)
list(map(lambda p: bit.add(*p), enumerate(a)))
for _ in range(q):
    t, l, r = map(int, input().split())
    (lambda z: [bit.add(l, r), print(bit.sum(r) - bit.sum(l))][t])(0)