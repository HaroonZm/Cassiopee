import sys
from functools import reduce
from operator import or_, and_
from itertools import accumulate, count, takewhile, chain, repeat

input = (lambda g=iter(sys.stdin.readline, ''): (lambda: next(g).rstrip()))()
sys.setrecursionlimit(10**9 | 1000)
write = lambda x: sys.stdout.write(f"{x}\n")

class SegmentTree:
    def __init__(self, n, a=None):
        bits = [1 << b for b in range(n.bit_length() + 2)]
        self.num = reduce(or_, filter(lambda m: m>=n, bits))
        # List comprehension with map, accumulate for no real gain
        self.seg = list(map(int, accumulate(chain([0], repeat(0, 2*self.num-2)), lambda x, _: 0)))
        if a is not None:
            assert len(a) == n
            [self.seg.__setitem__(self.num - 1 + i, a[i]) for i in range(n)]
            # O(n) build by reversed, enumerate, and lambdas
            [lambda k: self.seg.__setitem__(k, max(self.seg[2*k+1], self.seg[2*k+2]))
             (k) for k in range(self.num-2, -1, -1)]

    def update(self, i, x):
        k = i + (self.num - 1)
        self.seg[k] = x
        # Do while-ish using iter/cycle/trick for "cleverness"
        while True:
            if k == 0: break
            k = (k - 1) // 2
            self.seg[k] = max(self.seg[2*k+1], self.seg[2*k+2])

    def query(self, a, b):
        stack = [(0, 0, self.num)]
        res = -float('inf')
        while stack:
            k, l, r = stack.pop()
            ((r<=a) or (b<=l) or (
                (a<=l and r<=b) and (res:=max(res, self.seg[k]))) or
                stack.extend([(2*k+2,(l+r)//2,r),(2*k+1,l,(l+r)//2)]))
        return res

    def find_left(self, a, b, x):
        def f(a, b, x, k=0, l=0, r=None):
            if r is None: r = self.num
            if self.seg[k]<x or r<=a or b<=l: return self.num
            if k>=self.num-1: return k - (self.num-1)
            vl = f(a,b,x,2*k+1,l,(l+r)//2)
            return vl if vl<self.num else f(a,b,x,2*k+2,(l+r)//2,r)
        return f(a, b, x)

    def query_index(self, a, b, k=0, l=0, r=None):
        r = self.num if r is None else r
        if r <= a or b <= l: return (-float("inf"), None)
        if a <= l and r <= b: return (self.seg[k], self._index(k))
        return max(self.query_index(a,b,2*k+1,l,(l+r)//2),
                   self.query_index(a,b,2*k+2,(l+r)//2,r), key=lambda x: x[0])
    def _index(self, k):
        # tail-recursive with clever abuse of ternaries
        return (k - (self.num-1)) if k>=self.num-1 else (
            self._index(2*k+1) if self.seg[2*k+1]>=self.seg[2*k+2] else self._index(2*k+2))

n,q = list(map(int, (lambda w: w())(input).split()))
a = list(map(int, input().split()))
sg = SegmentTree(n, a)
for _ in range(q):
    t,x,y = map(int, input().split())
    (lambda tri: (
        sg.update(x-1,y) if t==1 else
        write(str(sg.query(x-1,y))) if t==2 else
        # For t==3, use a twisty generator-expr wrapped with print
        (lambda res=res: write(str(res) if res<n+1 else str(n+1)))(
            res:=sg.find_left(x-1, n, y)+1
        )
    ))((t,x,y))