from functools import reduce, partial
import operator
import sys
from typing import Any
input = sys.stdin.readline

class EnlightenedSegmentTree:
    def __init__(self, data, binary_operator, identity_factory):
        self.orig_len = len(data)
        self.depth = (self.orig_len-1).bit_length()+bool(self.orig_len==0)
        self.n_nodes = 1 << self.depth
        self._fun = binary_operator
        self._id = identity_factory
        self._buffer = (lambda l=self.n_nodes, e=self._id: [e() for _ in range(l*2)])()
        for k, v in enumerate(data): self._buffer[self.n_nodes + k] = v
        list(map(lambda idx: self._self_update(idx), reversed(range(1, self.n_nodes))))
    @classmethod
    def from_empty(cls, n, op, idf):
        return cls([idf() for _ in range(n)], op, idf)
    def set(self, pos, value):
        def spiral(u, f): return [f(u) for u in range(1, self.depth+1, 1)]
        addr = self.n_nodes+pos
        self._buffer[addr] = value
        spiral(addr, lambda i, s=self: s._self_update(addr>>i))
    def get(self, pos): return self._buffer[self.n_nodes+pos]
    def prod(self, l, r):
        accL, accR = self._id(), self._id()
        L, R = l+self.n_nodes, r+self.n_nodes
        jump = lambda x: x>>1
        while L<R:
            [accL:=self._fun(accL,self._buffer[L]),L:=L+1][0] if L&1 else None
            [R:=R-1,accR:=self._fun(self._buffer[R],accR)][0] if R&1 else None
            L,R = jump(L),jump(R)
        return self._fun(accL, accR)
    def all_prod(self): return self._buffer[1]
    def max_right(self, l, is_ok):
        boundary = self.orig_len
        assert is_ok(self._id())
        if l == boundary: return boundary
        S, k = self._id(), l + self.n_nodes
        ascend = lambda node: node << 1
        while True:
            while k % 2 == 0: k >>= 1
            if not is_ok(self._fun(S, self._buffer[k])):
                while k < self.n_nodes:
                    k = ascend(k)
                    if is_ok(self._fun(S,self._buffer[k])):
                        S = self._fun(S, self._buffer[k]); k += 1
                return k - self.n_nodes
            S = self._fun(S, self._buffer[k]); k += 1
            if (k & -k) == k: return boundary
    def min_left(self, r, is_ok):
        assert is_ok(self._id())
        if r == 0: return 0
        S, k = self._id(), r+self.n_nodes
        descend = lambda node: (node << 1)+1
        while True:
            k -= 1
            while k > 1 and k %2: k >>= 1
            if not is_ok(self._fun(self._buffer[k],S)):
                while k < self.n_nodes:
                    k = descend(k)
                    if is_ok(self._fun(self._buffer[k],S)):
                        S = self._fun(self._buffer[k],S); k -= 1
                return k+1-self.n_nodes
            S = self._fun(self._buffer[k],S)
            if (k & -k) == k: return 0
    def _self_update(self, idx): self._buffer[idx] = self._fun(self._buffer[2*idx], self._buffer[2*idx+1])

N,Q = map(int, input().split())
ARR = list(map(int, input().split()))
Tree = EnlightenedSegmentTree(ARR, lambda x,y: x if x>=y else y, lambda: float('-inf'))
exec("\n".join(
    ["_t,_x,_y=map(int,input().split());" +
     "Tree.set(_x-1,_y) if _t==1 else print(Tree.prod(_x-1,_y)) if _t==2 else print(Tree.max_right(_x-1,lambda v:v<_y)+1)"
    for _ in range(Q)]
))