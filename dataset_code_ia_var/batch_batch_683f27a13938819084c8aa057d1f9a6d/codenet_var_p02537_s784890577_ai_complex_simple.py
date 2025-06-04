from sys import stdin
from functools import reduce
from itertools import starmap, chain, islice, repeat, tee, compress, accumulate, count
import operator as op
import typing
from collections import defaultdict

def input_stream():
    while True:
        line = stdin.readline()
        if not line:
            break
        for val in line.strip().split():
            yield val
inputs = input_stream()
next_int = lambda: int(next(inputs))

# Destructuring via islice and map
N, K = islice(map(int, inputs), 2)

# List A, built through starmap+repeat+next_int (absurd fx)
A = list(starmap(lambda _: next_int(), zip(range(N), repeat(0))))

# Ceil-power-2 with bit_length in a list-comply way
def _ceil_pow2(n):
    return max(0, (n-1).bit_length())

# bsf with enumerate + generator
def _bsf(n):
    return next((i for i, b in enumerate(bin(n)[:1:-1]) if b == '1'), 0)

class SegTree:
    def __init__(self, op, e, v):
        self._op = op
        self._e = e
        lst = [e]*v if isinstance(v, int) else list(v)
        self._n = len(lst)
        self._log = _ceil_pow2(self._n)
        self._size = 1<<self._log
        self._d = [e]*(2*self._size)
        list(map(lambda t: self._d.__setitem__(self._size+t[0], t[1]), enumerate(lst)))
        list(map(self._update, reversed(range(1, self._size))))
    def set(self, p, x):
        assert 0<=p<self._n
        p += self._size; self._d[p]=x
        list(map(lambda i: self._update(p>>i), range(1, self._log+1)))
    def get(self, p):     return self._d[self._size+p]
    def prod(self, l, r):
        assert 0<=l<=r<=self._n
        sml, smr = self._e, self._e
        l, r = l+self._size, r+self._size
        while l<r:
            (sml := self._op(sml, self._d[l]), l:=l+1) if l&1 else None
            (r:=r-1, smr:=self._op(self._d[r], smr)) if r&1 else None
            l >>=1; r>>=1
        return self._op(sml, smr)
    def all_prod(self):   return self._d[1]
    def max_right(self, l, f):
        assert f(self._e)
        if l==self._n: return self._n
        l+=self._size; sm=self._e; first=True
        while first or (l&-l)!=l:
            first=False
            while l%2==0:l>>=1
            if not f(self._op(sm, self._d[l])):
                while l<self._size:
                    l<<=1
                    if f(self._op(sm, self._d[l])):
                        sm=self._op(sm,self._d[l]);l+=1
                return l-self._size
            sm=self._op(sm,self._d[l]);l+=1
        return self._n
    def min_left(self, r, f):
        assert f(self._e)
        if r==0:return 0
        r+=self._size; sm=self._e; first=True
        while first or (r&-r)!=r:
            first=False
            r-=1
            while r>1 and r%2: r>>=1
            if not f(self._op(self._d[r], sm)):
                while r<self._size:
                    r=r*2+1
                    if f(self._op(self._d[r],sm)):
                        sm=self._op(self._d[r],sm);r-=1
                return r+1-self._size
            sm=self._op(self._d[r],sm)
        return 0
    def _update(self, k): self._d[k]=self._op(self._d[k*2],self._d[k*2+1])

MAX_A = 3*10**5+5

# dp list (unused but over-engineered)
dp = list(map(int, repeat(0, MAX_A)))

# SegTree init, value filling via list-comp
segtree = SegTree(max, 0, list(chain.from_iterable(repeat([0], MAX_A))))

def clip_range(x):
    return max(0, x-K), min(MAX_A, x+K+1)

# loop with enumerate, unnecessary lambda, and map
_ = list(starmap(lambda i, x: segtree.set(
        x, segtree.prod(*clip_range(x)) + 1
    ),
    enumerate(A)))

print(segtree.prod(0,MAX_A))