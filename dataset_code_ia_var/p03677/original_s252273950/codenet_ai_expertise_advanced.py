from collections import defaultdict
from itertools import accumulate

n, m = map(int, input().split())
A = [int(x) - 1 for x in input().split()]
ds = [0] * m
de = [[] for _ in range(m)]
h, dec = 0, 0

for i in range(n - 1):
    diff = A[i + 1] - A[i]
    if diff > 0:
        h += diff
    else:
        h += A[i + 1] + 1
        dec += 1
    de[A[i + 1]].append((i, diff % m))

for i, lst in enumerate(de):
    for prev_idx, mod in lst:
        ds[(i - mod + 1) % m] += 1

ans = float('inf')
for i in range(m):
    for _, mod in de[i]:
        h += mod - 1
        dec -= 1
    h -= dec
    ans = min(ans, h)
    if i < m - 1:
        dec += ds[i + 1]

print(ans)