#!/usr/bin/env python3

import sys
import math
from collections import defaultdict, deque
from heapq import heappush, heappop
import bisect
from itertools import permutations, accumulate

def LI():  # Liste d'entiers depuis entrée, rien de fancy
    return list(map(int, sys.stdin.readline().split()))

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().strip().split()]

def S():
    res = list(sys.stdin.readline())
    if res and res[-1] == "\n":
        return res[:-1]
    return res

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

# Bon, au cas où...
sys.setrecursionlimit(10**6)
mod = 10**9 + 7

def solve():
    n = I()
    f = [0] * n  # degrés
    v = [[] for _ in range(n)]  # la liste d'adjacence (toujours compliqué ce truc)
    for i in range(n-1):
        a, b = LI()
        a -= 1  # Python c'est 0-indexé, faut pas oublier
        b -= 1
        v[a].append(b)
        v[b].append(a)
        f[a] += 1
        f[b] += 1
    a = LI()
    b = LI()
    c = [b[i] - a[i] for i in range(n)]
    d = [0] * n
    d[0] = 1  # on commence à la racine en général
    q = deque()
    q.append(0)
    while q:
        x = q.popleft()
        nd = d[x] + 1
        for y in v[x]:
            if not d[y]:
                d[y] = nd
                q.append(y)
    V = list(range(n))
    V.sort(key=lambda x: -d[x])  # du plus profond au moins profond
    s = [1 for _ in range(n)]
    for x in V:
        for y in v[x]:
            if d[y] < d[x]:
                s[y] += s[x]
    V = list(range(n))
    V.sort(key=lambda x: s[x])
    ans = 0
    for x in V:
        m = 0
        for y in v[x]:
            if s[y] < s[x]:
                if m < c[y]:
                    m = c[y]
        ans += m
        c[x] += m * f[x]
        for y in v[x]:
            if s[y] < s[x]:
                if c[y] < m:
                    res = m - c[y]
                    ans += res * s[y]
                    c[x] -= res
            else:
                c[y] -= m
        # print(f"x:{x}, m:{m}, reste:{ans}")  # juste pour debug, on peut enlever
    print(ans)
    return

if __name__ == "__main__":
    # on lance le truc !
    solve()