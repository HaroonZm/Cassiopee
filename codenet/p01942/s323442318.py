class BIT2:
    # H*W
    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.data = [{} for i in range(h+1)]

    # O(logH*logW)
    def sum(self, i, j):
        s = 0
        data = self.data
        while i > 0:
            el = data[i]
            k = j
            while k > 0:
                s += el.get(k, 0)
                k -= k & -k
            i -= i & -i
        return s

    # O(logH*logW)
    def add(self, i, j, x):
        w = self.w; h = self.h
        data = self.data
        while i <= h:
            el = data[i]
            k = j
            while k <= w:
                el[k] = el.get(k, 0) + x
                k += k & -k
            i += i & -i

    # [x0, x1) x [y0, y1)
    def range_sum(self, x0, x1, y0, y1):
        return self.sum(x1, y1) - self.sum(x1, y0) - self.sum(x0, y1) + self.sum(x0, y0)

h,w,T,Q = map(int,input().split())
ready = BIT2(h+1,w+1)
edible = BIT2(h+1,w+1)

from collections import deque

baking = deque([])

for i in range(Q):
    q = list(map(int,input().split()))
    while baking and baking[0][0] + T <= q[0]:
        t,x,y = baking.popleft()
        edible.add(x, y, 1)
    if q[1] == 0:
        x,y = q[2:]
        if ready.range_sum(x-1,x,y-1,y) == 0:
            ready.add(x ,y , 1)
            baking.append((q[0], x, y))
    if q[1] == 1:
        x,y = q[2:]
        if edible.range_sum(x-1,x,y-1,y) == 1:
            ready.add(x, y, -1)
            edible.add(x, y, -1)
    if q[1] == 2:
        x0,y0,x1,y1 = q[2:]
        ed = edible.range_sum(x0-1,x1,y0-1,y1)
        re = ready.range_sum(x0-1,x1,y0-1,y1)
        print(ed, re-ed)