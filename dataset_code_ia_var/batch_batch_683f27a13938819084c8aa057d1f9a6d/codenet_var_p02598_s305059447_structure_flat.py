from decimal import Decimal
from heapq import heapify, heappop, heappush
N, K = map(int, input().split())
A = list(map(int, input().split()))
tot = sum(A)
ng = 0
ok = 10**9
while ng + 1 < ok:
    m = (ng + ok) // 2
    c = 0
    for a in A:
        c += (a - 1) // m
    if c > K:
        ng = m
    else:
        ok = m
print(ok)