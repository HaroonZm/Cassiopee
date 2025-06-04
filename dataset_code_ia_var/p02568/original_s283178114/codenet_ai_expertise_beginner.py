class SegmentTreeLazy:
    def __init__(self, arr, ti, ei, func, op, merge):
        n = len(arr)
        h = 1
        while (1 << h) < n:
            h += 1
        size = 1 << h
        self.n = size
        self.h = h
        self.func = func
        self.op = op
        self.merge = merge
        self.ti = ti
        self.ei = ei
        self.val = [ti] * (2 * size)
        self.laz = [ei] * (2 * size)
        for i in range(n):
            self.val[size + i] = arr[i]
        for i in range(size - 1, 0, -1):
            self.val[i] = func(self.val[2 * i], self.val[2 * i + 1])

    def reflect(self, k):
        if self.laz[k] == self.ei:
            return self.val[k]
        else:
            return self.op(self.val[k], self.laz[k])

    def propagate(self, k):
        if self.laz[k] == self.ei:
            return
        self.laz[2 * k] = self.merge(self.laz[2 * k], self.laz[k])
        self.laz[2 * k + 1] = self.merge(self.laz[2 * k + 1], self.laz[k])
        self.val[k] = self.reflect(k)
        self.laz[k] = self.ei

    def thrust(self, k):
        for d in range(self.h, 0, -1):
            self.propagate(k >> d)

    def recalc(self, k):
        while k > 1:
            k >>= 1
            self.val[k] = self.func(self.reflect(2 * k), self.reflect(2 * k + 1))

    def update(self, l, r, x):
        l += self.n
        r += self.n
        l0 = l
        r0 = r
        self.thrust(l)
        self.thrust(r - 1)
        while l < r:
            if l % 2 == 1:
                self.laz[l] = self.merge(self.laz[l], x)
                l += 1
            if r % 2 == 1:
                r -= 1
                self.laz[r] = self.merge(self.laz[r], x)
            l //= 2
            r //= 2
        self.recalc(l0)
        self.recalc(r0 - 1)

    def query(self, l, r):
        l += self.n
        r += self.n
        self.thrust(l)
        self.thrust(r - 1)
        res_left = self.ti
        res_right = self.ti
        while l < r:
            if l % 2 == 1:
                res_left = self.func(res_left, self.reflect(l))
                l += 1
            if r % 2 == 1:
                r -= 1
                res_right = self.func(self.reflect(r), res_right)
            l //= 2
            r //= 2
        return self.func(res_left, res_right)

import sys
input = sys.stdin.buffer.readline

MOD = 998244353

N, Q = map(int, input().split())
a_list = list(map(int, input().split()))
arr = []
for a in a_list:
    arr.append(a * MOD + 1)
ti = 0
ei = MOD

def func(a, b):
    a1 = a // MOD
    a2 = a % MOD
    b1 = b // MOD
    b2 = b % MOD
    c1 = (a1 + b1) % MOD
    c2 = (a2 + b2) % MOD
    return c1 * MOD + c2

def op(a, x):
    a1 = a // MOD
    a2 = a % MOD
    x1 = x // MOD
    x2 = x % MOD
    c1 = (a1 * x1 + a2 * x2) % MOD
    c2 = a2
    return c1 * MOD + c2

def merge(x, y):
    x1 = x // MOD
    x2 = x % MOD
    y1 = y // MOD
    y2 = y % MOD
    z1 = (x1 * y1) % MOD
    z2 = (x2 * y1 + y2) % MOD
    return z1 * MOD + z2

st = SegmentTreeLazy(arr, ti, ei, func, op, merge)

res = []
for _ in range(Q):
    temp = list(map(int, input().split()))
    q = temp[0]
    if q == 0:
        l, r, b, c = temp[1:]
        st.update(l, r, b * MOD + c)
    else:
        l, r = temp[1:]
        result = st.query(l, r)
        res.append(result // MOD)

for x in res:
    print(x)