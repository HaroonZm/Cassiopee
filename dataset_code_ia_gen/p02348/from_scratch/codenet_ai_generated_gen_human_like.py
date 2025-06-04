import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class SegmentTreeRUQ:
    def __init__(self, n, default):
        self.n = 1
        while self.n < n:
            self.n <<= 1
        self.default = default
        self.data = [default] * (2 * self.n)
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
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.lazy[k] = x
            self._eval(k, l, r)
        else:
            mid = (l + r) // 2
            self._update(a, b, x, 2*k, l, mid)
            self._update(a, b, x, 2*k+1, mid, r)

    def update(self, a, b, x):
        self._update(a, b+1, x, 1, 0, self.n)

    def _query(self, i, k, l, r):
        self._eval(k, l, r)
        if r - l == 1:
            return self.data[k]
        mid = (l + r) // 2
        if i < mid:
            return self._query(i, 2*k, l, mid)
        else:
            return self._query(i, 2*k+1, mid, r)

    def query(self, i):
        return self._query(i, 1, 0, self.n)

def main():
    n, q = map(int, input().split())
    MAX_VAL = 2**31 - 1
    seg = SegmentTreeRUQ(n, MAX_VAL)

    for _ in range(q):
        query = input().split()
        t = int(query[0])
        if t == 0:
            s, t_, x = map(int, query[1:])
            seg.update(s, t_, x)
        else:
            i = int(query[1])
            print(seg.query(i))

if __name__ == "__main__":
    main()