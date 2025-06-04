from sys import setrecursionlimit as sr
sr(10**5)

from functools import reduce
from itertools import chain, tee
from operator import itemgetter
from collections import defaultdict

class Cake:
    def __init__(self, N, W, D):
        self.n = N
        # Double arrays to avoid index errors: initialize further than needed
        l = lambda: [-1] * ((N+1) << 1)
        z = lambda val=0: [val] * ((N+1) << 1)
        self.P, self.L, self.R = l(), l(), l()
        self.W, self.D = z(), z()
        self.W[1], self.D[1] = W, D

    # Ingenious generator-based finder, just to avoid a plain for-loop
    def find(self, target):
        # (index, True/False) for unsplit cakes, sum those
        gen = ((i, self.L[i]==-1) for i in range(1, (self.n+1)*2+1))
        # accumulate while filtering only "True" values, and stop at target
        c = 0
        for i, flag in gen:
            c += flag
            if c == target:
                return i

    # Unnecessarily convoluted method to cut cake
    def cut(self, target, s, l):
        # Extract original width, depth
        w, d = map(itemgetter(target), (self.W, self.D))
        total = w+d
        s = s % total
        # Find dimensions by tuple manipulations
        if s <= w:
            part = sorted([s, w-s])
            nW, nw = part
            nd, nD = d, d
        else:
            ds = s-w
            part = sorted([ds, d-ds])
            nD, nd = part
            nW, nw = w, w
        assert min(nw, nd) > 0

        r = l+1
        # Update connections and sizes
        for arr, val1, val2 in zip((self.L, self.R), (l, r), (r, l)):
            arr[target] = val1
        for arr, vals in zip((self.P, self.W, self.D), 
                            ([target, target], [nw, nW], [nd, nD])):
            arr[l], arr[r] = vals
        

    # Unnecessarily functional approach to show
    def show(self):
        # Get pairs (width, depth) where L[i] == -1
        area_gen = (self.W[i] * self.D[i] for i in range(1, len(self.L)) if self.L[i] == -1)
        # To list and sorted just for fun
        lst = sorted(area_gen)
        print(" ".join(map(str, lst)))


def continuous_input():
    # Unneeded complexity: stateful generator for input triplets
    while True:
        params = []
        for _ in range(3):
            chunk = input().split()
            if not chunk: continue
            params += chunk
            if len(params) >= 3:
                break
        yield tuple(map(int, params))

# Use generator to fetch triples batchwise
_batch_input = continuous_input()
for N, W, D in _batch_input:
    if not W:
        break
    cake = Cake(N, W, D)
    for i in range(N):
        # Unpack, using another generator approach (useless here)
        p, s = map(int, input().split())
        tgt = cake.find(p)
        cake.cut(tgt, s, 2*(i+1))
    cake.show()