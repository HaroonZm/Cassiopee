class SimpleLazySegtree:
    def __init__(self, n, init_val, merge_func, ide_ele):
        self.n = n
        self.ide_ele = ide_ele
        self.merge_func = merge_func
        size = 1 << n
        self.val = [0] * size
        self.merge = [0] * size
        self.parent = [-1] * size
        self.lazy = [0] * size

        from collections import deque
        deq = deque()
        deq.append(1 << (n - 1))
        node_order = []
        while deq:
            v = deq.popleft()
            node_order.append(v)
            if v % 2 == 0:
                gap = (v & -v) // 2
                self.parent[v-gap] = v
                deq.append(v-gap)
                self.parent[v+gap] = v
                deq.append(v+gap)

        for v in reversed(node_order):
            if v - 1 < len(init_val):
                self.val[v-1] = init_val[v-1]
            else:
                self.val[v-1] = 10**18
            self.merge[v-1] = self.val[v-1]
            if v % 2 == 0:
                gap = (v & -v) // 2
                self.merge[v-1] = self.merge_func(self.merge[v-1], self.merge[v-gap-1], self.merge[v+gap-1])

    def propagate(self, pos):
        if self.lazy[pos-1]:
            x = self.lazy[pos-1]
            self.val[pos-1] += x
            self.merge[pos-1] += x
            if pos % 2 == 0:
                gap = (pos & -pos) // 2
                self.lazy[pos-gap-1] += x
                self.lazy[pos+gap-1] += x
            self.lazy[pos-1] = 0

    def idgetter(self, start, goal):
        res = []
        pos = goal
        while pos != start:
            res.append(pos)
            pos = self.parent[pos]
        res.append(start)
        return res[::-1]

    def lower_kth_update(self, nd, k, x):
        if k == -1:
            return
        maxi = nd - (nd & -nd) + 1 + k
        ids = self.idgetter(nd, maxi)
        for pos in ids:
            gap = (pos & -pos) // 2
            self.propagate(pos)
            if pos <= maxi:
                self.val[pos-1] += x
                if gap != 0:
                    self.lazy[pos-gap-1] += x
        for pos in reversed(ids):
            if pos % 2 == 1:
                self.merge[pos-1] = self.val[pos-1]
            else:
                gap = (pos & -pos) // 2
                self.merge[pos-1] = self.merge_func(self.val[pos-1], self.merge[pos-gap-1]+self.lazy[pos-gap-1], self.merge[pos+gap-1]+self.lazy[pos+gap-1])

    def upper_kth_update(self, nd, k, x):
        if k == -1:
            return
        mini = nd + (nd & -nd) - 1 - k
        ids = self.idgetter(nd, mini)
        for pos in ids:
            gap = (pos & -pos) // 2
            self.propagate(pos)
            if pos >= mini:
                self.val[pos-1] += x
                if gap != 0:
                    self.lazy[pos+gap-1] += x
        for pos in reversed(ids):
            if pos % 2 == 1:
                self.merge[pos-1] = self.val[pos-1]
            else:
                gap = (pos & -pos) // 2
                self.merge[pos-1] = self.merge_func(self.val[pos-1], self.merge[pos-gap-1]+self.lazy[pos-gap-1], self.merge[pos+gap-1]+self.lazy[pos+gap-1])

    def update(self, l, r, x):
        pos = 1 << (self.n - 1)
        while True:
            gap = (pos & -pos) // 2
            self.propagate(pos)
            if pos-1 < l:
                pos += gap
            elif pos-1 > r:
                pos -= gap
            else:
                self.val[pos-1] += x
                self.upper_kth_update(pos-gap, pos-1-l-1, x)
                self.lower_kth_update(pos+gap, r-pos, x)
                break
        while self.parent[pos] != -1:
            if pos % 2 == 1:
                self.merge[pos-1] = self.val[pos-1]
            else:
                gap = (pos & -pos) // 2
                self.merge[pos-1] = self.merge_func(self.val[pos-1], self.merge[pos-gap-1]+self.lazy[pos-gap-1], self.merge[pos+gap-1]+self.lazy[pos+gap-1])
            pos = self.parent[pos]

    def lower_kth_merge(self, nd, k):
        if k == -1:
            return self.ide_ele
        maxi = nd - (nd & -nd) + 1 + k
        ids = self.idgetter(nd, maxi)
        for pos in ids:
            self.propagate(pos)
        stack = [self.ide_ele]
        for pos in reversed(ids):
            gap = (pos & -pos) // 2
            if pos % 2 == 1:
                self.merge[pos-1] = self.val[pos-1]
            else:
                self.merge[pos-1] = self.merge_func(self.val[pos-1], self.merge[pos-gap-1]+self.lazy[pos-gap-1], self.merge[pos+gap-1]+self.lazy[pos+gap-1])
            if pos <= maxi:
                stack.append(self.val[pos-1])
                if pos % 2 == 0:
                    stack.append(self.merge[pos-gap-1]+self.lazy[pos-gap-1])
        return self.merge_func(stack)

    def upper_kth_merge(self, nd, k):
        if k == -1:
            return self.ide_ele
        mini = nd + (nd & -nd) - 1 - k
        ids = self.idgetter(nd, mini)
        for pos in ids:
            self.propagate(pos)
        stack = [self.ide_ele]
        for pos in reversed(ids):
            gap = (pos & -pos) // 2
            if pos % 2 == 1:
                self.merge[pos-1] = self.val[pos-1]
            else:
                self.merge[pos-1] = self.merge_func(self.val[pos-1], self.merge[pos-gap-1]+self.lazy[pos-gap-1], self.merge[pos+gap-1]+self.lazy[pos+gap-1])
            if pos >= mini:
                stack.append(self.val[pos-1])
                if pos % 2 == 0:
                    stack.append(self.merge[pos+gap-1]+self.lazy[pos+gap-1])
        return self.merge_func(stack)

    def query(self, l, r):
        pos = 1 << (self.n - 1)
        res = self.ide_ele
        while True:
            gap = (pos & -pos) // 2
            self.propagate(pos)
            if pos-1 < l:
                pos += gap
            elif pos-1 > r:
                pos -= gap
            else:
                left = self.upper_kth_merge(pos-gap, pos-1-l-1)
                right = self.lower_kth_merge(pos+gap, r-pos)
                res = self.merge_func(left, right, self.val[pos-1])
                return res

import sys

def mymin(*args):
    return min(args)

ide_ele = 10**18

N, M = map(int, sys.stdin.buffer.readline().split())
init = [0] * (M+2)
for i in range(1, M+1):
    init[0] += 1
    init[i+1] -= 1
for i in range(1, M+2):
    init[i] += init[i-1]
init[-1] = 0

bit_len = (M+2).bit_length()
LST = SimpleLazySegtree(bit_len, init, merge_func=mymin, ide_ele=ide_ele)

hito = []
for i in range(N):
    a, b = map(int, sys.stdin.buffer.readline().split())
    hito.append((a, b))

hito.sort()
add = M - N
for l, r in hito:
    LST.update(0, r, -1)
    m = LST.query(l+1, M+1) + l
    if m < add:
        add = m

result = max(-add, 0)
print(result)