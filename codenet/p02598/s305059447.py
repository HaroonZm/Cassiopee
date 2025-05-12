from decimal import Decimal
from heapq import heapify, heappop, heappush
N, K = map(int, input().split())
*A, = map(int, input().split())

tot = sum(A)

ng = 0
ok = 10**9

m = 4

while ng + 1 < ok:
    m = (ng+ok)//2
    c = sum((a-1)//m for a in A)
    if c > K:
        ng = m
    else:
        ok = m
print(ok)