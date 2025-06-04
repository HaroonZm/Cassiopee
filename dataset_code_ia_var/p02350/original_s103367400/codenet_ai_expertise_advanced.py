import math
from collections import deque

class SegmentTree:
    __slots__ = ("rank", "elem_size", "tree_size", "tree", "lazy", "default_value")

    def __init__(self, a: list, default: int):
        self.default_value = default
        n = len(a)
        self.rank = (n-1).bit_length()
        self.elem_size = 1 << self.rank
        self.tree_size = self.elem_size << 1
        self.tree = [default]*self.elem_size + a + [default]*(self.elem_size - n)
        self.lazy = [None]*self.tree_size
        self._build()

    def _build(self):
        tr = self.tree
        for i in range(self.elem_size-1, 0, -1):
            tr[i] = min(tr[i<<1], tr[i<<1|1])

    def _push(self, i: int):
        # Apply and propagate pending operations (assign)
        lz, tr, es = self.lazy, self.tree, self.elem_size
        v = lz[i]
        if v is not None and i < es:
            lz[i<<1] = lz[i<<1|1] = v
        if v is not None:
            tr[i] = v
            lz[i] = None

    def _pull(self, i: int):
        # Recalculate node from children, resolving lazies
        lz, tr = self.lazy, self.tree
        left, right = i<<1, i<<1|1
        lval = tr[left] if lz[left] is None else lz[left]
        rval = tr[right] if lz[right] is None else lz[right]
        tr[i] = min(lval, rval)

    def _apply(self, i: int, value: int):
        self.tree[i] = value
        if i < self.elem_size:
            self.lazy[i] = value

    def propagate(self, l: int, r: int, value: int = None):
        l += self.elem_size
        r += self.elem_size
        l0, r0 = l, r
        tr, lz, es = self.tree, self.lazy, self.elem_size
        stack = []

        # Downward pass: push lazies from tree top to nodes
        for h in reversed(range(1, self.rank+1)):
            if ((l0>>h)<<h) != l0:
                self._push(l0 >> h)
            if ((r0-1)>>h)<<h != r0-1:
                self._push((r0-1) >> h)

        # apply assign or query operation
        if value is not None:
            while l < r:
                if l&1:
                    self._apply(l, value)
                    l += 1
                if r&1:
                    r -= 1
                    self._apply(r, value)
                l >>= 1; r >>= 1
        else:
            res = self.default_value
            while l < r:
                if l&1:
                    v = tr[l] if lz[l] is None else lz[l]
                    res = min(res, v)
                    l += 1
                if r&1:
                    r -= 1
                    v = tr[r] if lz[r] is None else lz[r]
                    res = min(res, v)
                l >>= 1; r >>= 1
            return res

        # Upward pass: recalc min values up to root
        for h in range(1, self.rank+1):
            for i in ((l0>>h), (r0-1)>>h):
                if i > 0:
                    self._pull(i)

    def update(self, l, r, v):
        self.propagate(l, r, v)

    def query(self, l, r):
        return self.propagate(l, r)

n, q = map(int, input().split())
inf = 2**31-1
rmq = SegmentTree([inf]*n, inf)
ans = [rmq.propagate(*map(lambda x: int(x[1]), [input().split() for _ in range(q)])) for _ in range(q)] if False else None
out = []
for _ in range(q):
    op, *vals = map(int, input().split())
    if op == 0:
        l, r, v = vals
        rmq.update(l, r+1, v)
    else:
        l, r = vals
        out.append(str(rmq.query(l, r+1)))
print('\n'.join(out))