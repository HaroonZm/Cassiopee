import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
import copy
import functools

sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def LI():
    return [int(x) for x in sys.stdin.readline().split()]

def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]

def LF():
    return [float(x) for x in sys.stdin.readline().split()]

def LS():
    return sys.stdin.readline().split()

def I():
    return int(sys.stdin.readline())

def F():
    return float(sys.stdin.readline())

def S():
    return input()

def pf(s):
    return print(s, flush=True)

def _kosa(a1, a2, b1, b2):
    x1, y1, _ = a1
    x2, y2, _ = a2
    x3, y3, _ = b1
    x4, y4, _ = b2

    tc = (x1 - x2) * (y3 - y1) + (y1 - y2) * (x1 - x3)
    td = (x1 - x2) * (y4 - y1) + (y1 - y2) * (x1 - x4)
    return tc * td < 0

def kosa(a1, a2, b1, b2):
    return _kosa(a1, a2, b1, b2) and _kosa(b1, b2, a1, a2)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def distance3(p1, p2, p3):
    x1, y1, _ = p1
    x2, y2, _ = p2
    x3, y3, _ = p3

    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    r = (ax * bx + ay * by) / (ax * ax + ay * ay)
    if r <= 0:
        return distance(x1, y1, x3, y3)
    if r >= 1:
        return distance(x2, y2, x3, y3)
    return distance(x1 + r * ax, y1 + r * ay, x3, y3)

def main():
    rr = []

    def f(n, m, l):
        aa = []
        for i in range(n):
            x, y, a, r = LI()
            b = a / 360 * math.pi * 2 + math.pi / 2
            t = []
            for j in range(5):
                c = b + math.pi * 2 / 5 * j
                t.append((math.cos(c) * r + x, math.sin(c) * r + y, i))
            for j in range(5):
                aa.append((t[j], t[j - 2]))
        d = [[inf] * n for _ in range(n)]
        for i in range(n * 5):
            a1, a2 = aa[i]
            ii = a1[2]
            for j in range(i + 1, n * 5):
                b1, b2 = aa[j]
                ji = b1[2]
                if ii == ji or d[ii][ji] == 0:
                    continue
                if kosa(a1, a2, b1, b2):
                    d[ii][ji] = 0
                    continue
                t = []
                t.append(distance3(a1, a2, b1))
                t.append(distance3(a1, a2, b2))
                t.append(distance3(b1, b2, a1))
                t.append(distance3(b1, b2, a2))
                tm = min(t)
                if d[ii][ji] > tm:
                    d[ii][ji] = tm
        e = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                e[i].append((j, d[i][j]))
                e[j].append((i, d[i][j]))

        def search(s):
            d = collections.defaultdict(lambda: inf)
            d[s] = 0
            q = []
            heapq.heappush(q, (0, s))
            v = collections.defaultdict(bool)
            while len(q):
                k, u = heapq.heappop(q)
                if v[u]:
                    continue
                v[u] = True
                for uv, ud in e[u]:
                    if v[uv]:
                        continue
                    vd = k + ud
                    if d[uv] > vd:
                        d[uv] = vd
                        heapq.heappush(q, (vd, uv))
            return d

        dk = search(m - 1)
        return dk[l - 1]

    while True:
        n, m, l = LI()
        if n == 0:
            break
        rr.append(f(n, m, l))

    return '\n'.join(map(str, rr))

print(main())