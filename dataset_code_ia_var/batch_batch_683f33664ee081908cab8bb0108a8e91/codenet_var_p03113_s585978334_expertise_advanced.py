from heapq import heappush, heappop
from itertools import count
from sys import stdin

n, k, *a = map(int, stdin.read().split())
pq = [(-val, idx) for idx, val in enumerate(a, 1)]
pq.sort()  # max-heap emulation
res = []
it = count(1)
used = set(idx for _, idx in pq)

while k:
    if not pq:
        print(-1)
        exit()
    val, idx = heappop(pq)
    res.append(idx)
    k -= 1
    for i, (v, j) in enumerate(pq):
        if j != idx:
            if v == -2:
                print(-1)
                exit()
            pq[i] = (v + 1, j)
    pq.sort()  # re-sort after modification

print(len(res), *res)