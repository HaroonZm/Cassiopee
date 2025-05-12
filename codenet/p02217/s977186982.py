#!usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
from itertools import permutations, accumulate
import sys
import math
import bisect
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    n = I()
    f = [0]*n
    v = [[] for i in range(n)]
    for i in range(n-1):
        a,b = LI()
        a -= 1
        b -= 1
        v[a].append(b)
        v[b].append(a)
        f[a] += 1
        f[b] += 1
    a = LI()
    b = LI()
    c = [b[i]-a[i] for i in range(n)]
    d = [0]*n
    d[0] = 1
    q = deque([0])
    while q:
        x = q.popleft()
        nd = d[x] + 1
        for y in v[x]:
            if not d[y]:
                d[y] = nd
                q.append(y)
    V = list(range(n))
    V.sort(key = lambda x:-d[x])
    s = [1]*n
    for x in V:
        for y in v[x]:
            if d[y] < d[x]:
                s[y] += s[x]
    V = list(range(n))
    V.sort(key = lambda x:s[x])
    ans = 0
    for x in V:
        m = 0
        for y in v[x]:
            if s[y] < s[x]:
                if m < c[y]:
                    m = c[y]
        ans += m
        c[x] += m*f[x]
        for y in v[x]:
            if s[y] < s[x]:
                if c[y] < m:
                    res = m-c[y]
                    ans += res*s[y]
                    c[x] -= res
            else:
                c[y] -= m
    print(ans)
    return

#Solve
if __name__ == "__main__":
    solve()