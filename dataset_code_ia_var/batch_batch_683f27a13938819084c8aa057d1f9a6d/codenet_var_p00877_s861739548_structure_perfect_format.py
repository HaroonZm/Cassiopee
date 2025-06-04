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

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**13
mod = 10**9 + 7
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
    x1, y1 = a1
    x2, y2 = a2
    x3, y3 = b1
    x4, y4 = b2

    tc = (x1 - x2)*(y3 - y1) + (y1 - y2)*(x1 - x3)
    td = (x1 - x2)*(y4 - y1) + (y1 - y2)*(x1 - x4)
    return tc * td < 0

def kosa(a1, a2, b1, b2):
    return _kosa(a1, a2, b1, b2) and _kosa(b1, b2, a1, a2)

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def distance_p(a, b):
    return distance(a[0], a[1], b[0], b[1])

def distance3(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    ax = x2 - x1
    ay = y2 - y1
    bx = x3 - x1
    by = y3 - y1

    r = (ax * bx + ay * by) / (ax * ax + ay * ay)
    if r <= 0:
        return distance_p(p1, p3)
    if r >= 1:
        return distance_p(p2, p3)
    pt = (x1 + r * ax, y1 + r * ay, 0)
    return distance_p(pt, p3)

def ccw(a, b, c):
    ax = b[0] - a[0]
    ay = b[1] - a[1]
    bx = c[0] - a[0]
    by = c[1] - a[1]
    t = ax * by - ay * bx
    if t > 0:
        return 1
    if t < 0:
        return -1
    if ax * bx + ay * by < 0:
        return 2
    if ax * ax + ay * ay < bx * bx + by * by:
        return -2
    return 0

def convex_hull(ps):
    n = len(ps)
    if n < 3:
        return ps[:]
    k = 0
    ps.sort()
    ch = [None] * (n * 2)
    for i in range(n):
        while k >= 2 and ccw(ch[k - 2], ch[k - 1], ps[i]) <= 0:
            k -= 1
        ch[k] = ps[i]
        k += 1
    t = k + 1
    for i in range(n - 2, -1, -1):
        while k >= t and ccw(ch[k - 2], ch[k - 1], ps[i]) <= 0:
            k -= 1
        ch[k] = ps[i]
        k += 1
    return ch[:k - 1]

def main():
    rr = []

    def f(n, m):
        a = [LI() for _ in range(n)]
        b = [LI() for _ in range(m)]
        t = convex_hull(a + b)
        af = False
        bf = False
        for c in t:
            if c in a:
                af = True
            else:
                bf = True
        if not af or not bf:
            return 'NO'
        d = convex_hull(a)
        e = convex_hull(b)
        dl = len(d)
        el = len(e)
        if dl > 1:
            for i in range(dl):
                d1 = d[i]
                d2 = d[(i + 1) % dl]
                for j in range(el):
                    k = distance3(d1, d2, e[j])
                    if k < eps:
                        return 'NO'
                    if el > 1 and kosa(d1, d2, e[j], e[(j + 1) % el]):
                        return 'NO'
        if el > 1:
            for i in range(el):
                e1 = e[i]
                e2 = e[(i + 1) % el]
                for j in range(dl):
                    k = distance3(e1, e2, d[j])
                    if k < eps:
                        return 'NO'
        return 'YES'

    while True:
        n, m = LI()
        if n == 0:
            break
        rr.append(f(n, m))
    return '\n'.join(map(str, rr))

print(main())