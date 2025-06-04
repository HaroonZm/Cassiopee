#!/usr/bin/env python3
from collections import defaultdict, deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def I():
    return int(sys.stdin.readline())

def LS():
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    return list(sys.stdin.readline())[:-1]

def IR(n):
    return [I() for _ in range(n)]

def LIR(n):
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

# A
def A():
    n = I()
    p = LI()
    t = LI()
    ans = float("inf")
    for i in range(n + 1):
        x0 = t[0] * i
        m0 = p[0] * i
        for j in range(n + 1):
            x1 = x0 + t[1] * j
            m1 = m0 + p[1] * j
            for k in range(n + 1):
                x2 = x1 + t[2] * k
                m2 = m1 + p[2] * k
                rest = max(0, math.ceil((n - x2) / t[3]))
                m3 = m2 + p[3] * rest
                if m3 < ans:
                    ans = m3
    print(ans)
    return

# B
def B():
    def f(n):
        if n < 4:
            return 1
        m = n
        res = 1
        i = 2
        while i ** 2 <= n:
            if m % i == 0:
                if m // i != i:
                    res *= m // i
                res *= i
            i += 1
        return res

    MA = 100000
    d = [0] * (MA + 1)
    for i in range(12, MA + 1):
        if not d[i]:
            if f(i) >= (i << 1):
                j = i
                while j <= MA:
                    d[j] = 1
                    j += i
    for i in range(MA):
        d[i + 1] += d[i]
    q = I()
    for _ in range(q):
        print(d[I()])
    return

# C
def C():
    def formula(s, i, k):
        return or_expr(s, i, k)

    def or_expr(s, i, k):
        a, i = and_expr(s, i, k)
        while i < len(s) and s[i] == "|":
            i += 1
            v, i = and_expr(s, i, k)
            if not k:
                a += v
        return a, i

    def and_expr(s, i, k):
        t, i = term(s, i, k)
        while i < len(s) and s[i] == "&":
            i += 1
            v, i = term(s, i, k)
            if k:
                t += v
        return t, i

    def term(s, i, k):
        if s[i] == "(":
            i += 1
            if not k:
                o0, j = or_expr(s, i, 0)
                o1, i = or_expr(s, i, 1)
                return min(o0, o1), i + 1
            else:
                o, i = or_expr(s, i, 1)
                return o, i + 1
        return 1, i + 1

    s = input()
    print(formula(s, 0, 0)[0], formula(s, 0, 1)[0])
    return

# D
def D():
    a, b = LI()
    for i in range(b + 1, b + a):
        x = i // b
        j = i % b
        x += j // a
        j = j % a
        x += j
        y = i // a + i % a
        if y < x:
            print(i)
            break
    else:
        print(-1)
    return

# E
def E():
    n, s, t = LI()
    d = [[None] * (n + 1) for _ in range(n + 1)]
    print("?", s, t)
    print(end='', flush=True)
    d[s][t] = I()
    d[t][s] = d[s][t]
    f = [None] * (n + 1)
    f[0] = (0, float("inf"))
    f[s] = (s, 0)
    f[t] = (t, d[s][t])
    for i in range(1, n + 1):
        if i in [t, s]:
            continue
        print("?", s, i)
        print(end='', flush=True)
        d[s][i] = I()
        d[i][s] = d[s][i]
        print("?", i, t)
        print(end='', flush=True)
        d[i][t] = I()
        d[t][i] = d[i][t]
        if d[s][i] + d[i][t] > d[s][t]:
            f[i] = (i, float("inf"))
        else:
            f[i] = (i, d[s][i])
    f.sort(key=lambda x: x[1])
    for i in range(n + 1):
        if f[i][1] == float("inf"):
            break
    f = f[1:i - 1]
    m = len(f)
    k = [0] * m
    if k:
        k[0] = 1
        x = f[0][0]
        for i in range(1, m):
            y = f[i][0]
            print("?", x, y)
            print(end='', flush=True)
            d[x][y] = I()
            if d[s][x] + d[x][y] == d[s][y]:
                k[i] = 1
            else:
                k[i] = 0
    ans = [s]
    for i in range(m):
        if k[i]:
            ans.append(f[i][0])
    ans.append(t)
    print("!", *ans)
    return

# F
def F():
    n = I()
    return

# G
def G():
    n, w = LI()
    p = LI()
    v = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b, c = LI()
        a -= 1
        b -= 1
        v[a].append((b, c))
        v[b].append((a, c))
    dp = []
    return

# Solve
if __name__ == "__main__":
    E()