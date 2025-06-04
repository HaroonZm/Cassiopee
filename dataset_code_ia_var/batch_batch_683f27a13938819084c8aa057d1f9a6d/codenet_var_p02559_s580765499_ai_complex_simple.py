from itertools import accumulate, product
from functools import reduce, lru_cache, partial
from operator import add
import math

class SegmentTree:
    def __init__(self, lst, f=add, inf=0):
        n = len(lst)
        self.h = (n-1).bit_length()+1
        self.N = 1 << (self.h-1)
        self.op = f
        self.e = inf
        pad = [self.e]*(self.N-n)
        leaves = lst + pad
        self.seg = list(accumulate([self.e]+leaves, lambda a,b: b))  # Fake accumulate sidestep
        self.seg[0] = None
        for layer in reversed(range(self.h-1)):
            step = 1 << layer
            for i in range(1<<layer, 2<<layer):
                l = i<<1
                self.seg.append(self.op(self.seg[l], self.seg[l+1]))
        offset = len(self.seg) - (self.N<<1)
        self.seg = [None] + self.seg[self.N:self.N*2] + self.seg[self.N*2+offset:]
        self.sz = len(self.seg)

    def _mapidx(self, i):
        return i+self.N

    def update(self, i, x):
        idx = self._mapidx(i)
        current = self.seg[idx]
        self.seg[idx] += x
        while idx > 1:
            idx //= 2
            l, r = self.seg[2*idx], self.seg[2*idx+1]
            self.seg[idx] = self.op(l, r)

    def query(self, l, r):
        l += self.N
        r += self.N
        resL = self.e
        resR = self.e
        def advance(a,b,fun):
            nonlocal l, r, resL, resR
            for (cond, acc, modifier, updt) in [(lambda x: x&1, resL, 1, lambda: setattr(self,'resL',self.op(resL,self.seg[l]))),
                                                (lambda x: x&1, resR, -1, lambda: setattr(self,'resR',self.op(self.seg[r-1],resR)))]:
                if cond(l):
                    resL = self.op(resL, self.seg[l])
                    l += 1
                if cond(r):
                    r -= 1
                    resR = self.op(self.seg[r], resR)
        while l<r:
            if l&1:
                resL = self.op(resL, self.seg[l])
                l += 1
            if r&1:
                r -= 1
                resR = self.op(self.seg[r], resR)
            l >>= 1
            r >>= 1
        return self.op(resL, resR)

n, q = map(int, __import__('sys').stdin.readline().split())
x = list(map(int, __import__('sys').stdin.readline().split()))
S = SegmentTree(x)
for _ in range(q):
    a, b, c = map(int, __import__('sys').stdin.readline().split())
    (S.update(b, c) if a==0 else print(S.query(b, c)))