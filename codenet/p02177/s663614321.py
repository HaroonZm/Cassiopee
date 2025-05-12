#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(1000000000)
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

n,m = LI()
graph = [[] for _ in range(n)]
for _ in range(m):
    a,b = LI()
    graph[a-1].append(b-1)

def dfs(s,lst,graph,check):
    lst.append(s)
    check[s] = False
    for v in graph[s]:
        if check[v]:
            dfs(v,lst,graph,check)
    return lst
L = []
for i in range(n):
    c = [True]*n
    l = dfs(i,[],graph,c)
    l.sort()
    L.append(l)

ans = [[] for _ in range(n)]
for i in range(n):
    for j in L[i]:
        if i in L[j]:
            ans[i].append(j+1)
for i in range(n):
    print(*ans[i])