from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

sys.setrecursionlimit(1000000)
mod = 1000000007

while True:
    line = sys.stdin.readline()
    if not line:
        break
    n_m = list(map(int, line.split()))
    if len(n_m) < 2:
        continue
    n, m = n_m
    if n == 0 and m == 0:
        break

    l = []
    cnt = 0
    while cnt < m:
        inp = sys.stdin.readline()
        if not inp:
            break
        arr = list(map(int, inp.split()))
        if len(arr) < 3:
            continue
        l.append(arr)
        cnt += 1

    l.sort(key=lambda x: x[2])
    for i in range(m):
        l[i][0] -= 1
        l[i][1] -= 1

    ans = []
    par = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    def root(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x

    for x, y, c in l:
        rx = root(x)
        ry = root(y)
        if rx != ry:
            if rank[rx] < rank[ry]:
                par[rx] = ry
            else:
                par[ry] = rx
                if rank[rx] == rank[ry]:
                    rank[rx] += 1
            ans.append(c)

    print(ans[(n - 1) // 2])