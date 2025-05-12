#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

def dijkstra(s,graph):
    d = [inf]*n
    d[s] = 0
    h = [(0,s)]
    while h:
        c,v = heappop(h)
        if d[v] < c:
            continue
        for t,cost in graph[v]:
            if d[v] + cost < d[t]:
                d[t] = d[v] + cost
                heappush(h,(d[t],t))
    return d

n, m = LI()
edges = [[] for _ in range(n)]
for i in range(1, n):
    edges[i].append((i-1, 0))

for _ in range(m):
    l, r, c = LI()
    edges[l-1].append((r-1, c))

d = dijkstra(0, edges)
if d[-1] == inf:
    print(-1)
else:
    print(d[-1])