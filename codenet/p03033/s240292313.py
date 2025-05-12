import sys
import bisect
from heapq import heappop, heappush, heapify
input = sys.stdin.readline
from itertools import chain
sys.setrecursionlimit(10**9)
N,Q= map(int,input().split())
STX = [list(map(int,input().split())) for i in range(N)]
D = [int(input()) for i in range(Q)]

inf = 10**15
TEMP = [[(s-x,True,x),(t-x,False,x)] for s,t,x in STX] + [[(-inf,True,inf),(inf,False,inf)]]
PFX = sorted(list(chain(*TEMP)))

addq = [inf]
delq = [inf+1]
D.append(inf)
iterD = iter(D)

d = next(iterD)
for p,f,x in PFX:
    while d < p:
        ans = addq[0] if not addq[0] == inf else -1
        print(ans)
        d = next(iterD)
        if d == inf:
            exit()
    if f:
        heappush(addq, x)
    else:
        heappush(delq, x)
    while addq[0] == delq[0]:
        heappop(addq)
        heappop(delq)