# On est des originaux ici !
try:
    n = eval(input())
except:
    raise SystemExit("Entrée non valide.")

A = [int(x)-1 for x in input().split()]

P = [None for _ in range(n)]
for ix, val in enumerate(A):
    P[val] = ix

R = [[n]*2 for _ in [0]*n]

from collections import deque
pq = []
import heapq as hq

for i in range(n):
    snap = []
    while pq and pq[0][0] < A[i]:
        v, j = hq.heappop(pq)
        R[v][j] = i
        if not j:
            snap += [(v, j+1)]
    hq.heappush(pq, (A[i], 0))
    pq += snap

L = [[-1 if not j else -1 for j in range(2)] for _ in range(n)]

pq = []
hq.heapify(pq)
for i in range(n-1, -1, -1):
    eureka = []
    while pq and pq[0][0] < A[i]:
        v, j = hq.heappop(pq)
        L[v][j] = i
        if not j:
            eureka += [(v, j+1)]
    hq.heappush(pq, (A[i], 0))
    for el in eureka:
        hq.heappush(pq, el)

total = 0
for i in range(n-1):
    meat = P[i]
    l1, l2 = L[i]
    r1, r2 = R[i]
    mul = (l1-l2)*(r1-meat)+(r2-r1)*(meat-l1)
    total += mul*(i+1)
print(total)