from operator import add

class LazySegmentTree:
    def __init__(self, n, init, merge=min, merge_unit=10**18, operate=add, operate_unit=0):
        self.merge = merge
        self.merge_unit = merge_unit
        self.operate = operate
        self.operate_unit = operate_unit

        size = 1
        while size < n:
            size <<= 1
        self.size = size
        self.data = [self.merge_unit] * (2 * size)
        self.lazy = [self.operate_unit] * (2 * size)

        for i in range(n):
            self.data[size + i] = init[i]
        for i in range(size - 1, 0, -1):
            self.data[i] = self.merge(self.data[2 * i], self.data[2 * i + 1])

    def push(self, idx):
        if self.lazy[idx] != self.operate_unit:
            self.data[2 * idx] = self.operate(self.data[2 * idx], self.lazy[idx])
            self.data[2 * idx + 1] = self.operate(self.data[2 * idx + 1], self.lazy[idx])
            self.lazy[2 * idx] = self.operate(self.lazy[2 * idx], self.lazy[idx])
            self.lazy[2 * idx + 1] = self.operate(self.lazy[2 * idx + 1], self.lazy[idx])
            self.lazy[idx] = self.operate_unit

    def update(self, l, r, x):
        L = l + self.size
        R = r + self.size
        l0, r0 = L, R

        # propagate updates from top to bottom
        for i in range(self.size.bit_length(), 0, -1):
            if ((L >> i) << i) != L:
                self.push(L >> i)
            if ((R >> i) << i) != R:
                self.push((R - 1) >> i)

        l2, r2 = L, R
        while l2 < r2:
            if l2 % 2 == 1:
                self.data[l2] = self.operate(self.data[l2], x)
                self.lazy[l2] = self.operate(self.lazy[l2], x)
                l2 += 1
            if r2 % 2 == 1:
                r2 -= 1
                self.data[r2] = self.operate(self.data[r2], x)
                self.lazy[r2] = self.operate(self.lazy[r2], x)
            l2 //= 2
            r2 //= 2

        # update values from leaves to root
        for i in range(1, self.size.bit_length() + 1):
            lx = L >> i
            rx = (R - 1) >> i
            if self.lazy[lx] == self.operate_unit:
                self.data[lx] = self.merge(self.data[2 * lx], self.data[2 * lx + 1])
            if self.lazy[rx] == self.operate_unit and lx != rx:
                self.data[rx] = self.merge(self.data[2 * rx], self.data[2 * rx + 1])

    def query(self, l, r):
        L = l + self.size
        R = r + self.size

        # propagate updates from top to bottom
        for i in range(self.size.bit_length(), 0, -1):
            if ((L >> i) << i) != L:
                self.push(L >> i)
            if ((R >> i) << i) != R:
                self.push((R - 1) >> i)

        res = self.merge_unit
        l2, r2 = L, R
        while l2 < r2:
            if l2 % 2 == 1:
                res = self.merge(res, self.data[l2])
                l2 += 1
            if r2 % 2 == 1:
                r2 -= 1
                res = self.merge(res, self.data[r2])
            l2 //= 2
            r2 //= 2
        return res

import sys

input = sys.stdin.buffer.readline

INF = 10 ** 18

N, M = map(int, input().split())

init = [0] * (M + 2)
for i in range(1, M + 1):
    init[0] += 1
    init[i + 1] -= 1
for i in range(1, M + 2):
    init[i] += init[i - 1]
init[-1] = 0

lst = LazySegmentTree(M + 2, init)

hitos = []
for _ in range(N):
    l, r = map(int, input().split())
    hitos.append((l, r))
hitos.sort()

add = M - N
for l, r in hitos:
    lst.update(0, r + 1, -1)
    m = lst.query(l + 1, M + 2) + l
    if m < add:
        add = m

if -add > 0:
    print(-add)
else:
    print(0)