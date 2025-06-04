# Version simple débutant

class SimpleSegmentTree:
    def __init__(self, arr):
        n = len(arr)
        N = 1
        while N < n:
            N *= 2
        self.N = N
        self.INF = float('inf')
        self.data = [0] * (2 * N)
        self.lazy = [0] * (2 * N)
        for i in range(n):
            self.data[N + i] = arr[i]
        for i in range(N - 1, 0, -1):
            self.data[i] = min(self.data[i * 2], self.data[i * 2 + 1])

    def _push(self, k):
        # Propagate lazy value to children
        if self.lazy[k]:
            self.data[k * 2] += self.lazy[k]
            self.lazy[k * 2] += self.lazy[k]
            self.data[k * 2 + 1] += self.lazy[k]
            self.lazy[k * 2 + 1] += self.lazy[k]
            self.lazy[k] = 0

    def _update(self, a, b, x, k, l, r):
        # update [a, b)
        if r <= a or b <= l:
            return
        if a <= l and r <= b:
            self.data[k] += x
            self.lazy[k] += x
        else:
            self._push(k)
            m = (l + r) // 2
            self._update(a, b, x, k * 2, l, m)
            self._update(a, b, x, k * 2 + 1, m, r)
            self.data[k] = min(self.data[k * 2], self.data[k * 2 + 1])

    def update(self, l, r, x):
        self._update(l, r, x, 1, 0, self.N)

    def _query(self, a, b, k, l, r):
        # query [a, b)
        if r <= a or b <= l:
            return self.INF
        if a <= l and r <= b:
            return self.data[k]
        else:
            self._push(k)
            m = (l + r) // 2
            vl = self._query(a, b, k * 2, l, m)
            vr = self._query(a, b, k * 2 + 1, m, r)
            return min(vl, vr)

    def query(self, l, r):
        return self._query(l, r, 1, 0, self.N)


n, q = map(int, input().split())
arr = [0] * n
seg = SimpleSegmentTree(arr)

for _ in range(q):
    tmp = list(map(int, input().split()))
    if tmp[0] == 0:
        _, s, t, x = tmp
        seg.update(s, t + 1, x)
    else:
        _, s, t = tmp
        print(seg.query(s, t + 1))