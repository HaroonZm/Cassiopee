import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.INF = 2**31 - 1
        self.data = [self.INF] * (2 * self.n)
        self.lazy = [None] * (2 * self.n)

    def _eval(self, k, l, r):
        if self.lazy[k] is not None:
            self.data[k] = self.lazy[k]
            if r - l > 1:
                self.lazy[2*k] = self.lazy[k]
                self.lazy[2*k+1] = self.lazy[k]
            self.lazy[k] = None

    def _update(self, a, b, x, k, l, r):
        self._eval(k, l, r)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.lazy[k] = x
            self._eval(k, l, r)
            return
        m = (l + r) >> 1
        self._update(a, b, x, 2*k, l, m)
        self._update(a, b, x, 2*k+1, m, r)
        # No need to update data[k] here because only find requires propagation to leaves.

    def update(self, a, b, x):
        self._update(a, b+1, x, 1, 0, self.n)

    def _query(self, i, k, l, r):
        self._eval(k, l, r)
        if r - l == 1:
            return self.data[k]
        m = (l + r) >> 1
        if i < m:
            return self._query(i, 2*k, l, m)
        else:
            return self._query(i, 2*k+1, m, r)

    def query(self, i):
        return self._query(i, 1, 0, self.n)


n, q = map(int, input().split())
seg = SegmentTree(n)

for _ in range(q):
    tmp = input().split()
    if tmp[0] == '0':
        _, s, t, x = tmp
        seg.update(int(s), int(t), int(x))
    else:
        _, i = tmp
        print(seg.query(int(i)))