h, w, T, Q = map(int, input().split())

w2 = w + 2
h2 = h + 2

# BIT2-like for ready
ready_data = [{} for _ in range(h2)]
# BIT2-like for edible
edible_data = [{} for _ in range(h2)]

from collections import deque
baking = deque([])

def bit2_sum(data, i, j):
    s = 0
    while i > 0:
        el = data[i]
        k = j
        while k > 0:
            s += el.get(k, 0)
            k -= k & -k
        i -= i & -i
    return s

def bit2_add(data, h, w, i, j, x):
    while i <= h:
        el = data[i]
        k = j
        while k <= w:
            el[k] = el.get(k, 0) + x
            k += k & -k
        i += i & -i

for _ in range(Q):
    q = list(map(int, input().split()))
    while baking and baking[0][0] + T <= q[0]:
        t, x, y = baking.popleft()
        bit2_add(edible_data, h+1, w+1, x, y, 1)
    if q[1] == 0:
        x, y = q[2:]
        r = bit2_sum(ready_data, x, y) - bit2_sum(ready_data, x, y-1) - bit2_sum(ready_data, x-1, y) + bit2_sum(ready_data, x-1, y-1)
        if r == 0:
            bit2_add(ready_data, h+1, w+1, x, y, 1)
            baking.append((q[0], x, y))
    if q[1] == 1:
        x, y = q[2:]
        ed = bit2_sum(edible_data, x, y) - bit2_sum(edible_data, x, y-1) - bit2_sum(edible_data, x-1, y) + bit2_sum(edible_data, x-1, y-1)
        if ed == 1:
            bit2_add(ready_data, h+1, w+1, x, y, -1)
            bit2_add(edible_data, h+1, w+1, x, y, -1)
    if q[1] == 2:
        x0, y0, x1, y1 = q[2:]
        e1 = bit2_sum(edible_data, x1, y1)
        e2 = bit2_sum(edible_data, x1, y0-1)
        e3 = bit2_sum(edible_data, x0-1, y1)
        e4 = bit2_sum(edible_data, x0-1, y0-1)
        ed = e1 - e2 - e3 + e4
        r1 = bit2_sum(ready_data, x1, y1)
        r2 = bit2_sum(ready_data, x1, y0-1)
        r3 = bit2_sum(ready_data, x0-1, y1)
        r4 = bit2_sum(ready_data, x0-1, y0-1)
        re = r1 - r2 - r3 + r4
        print(ed, re-ed)