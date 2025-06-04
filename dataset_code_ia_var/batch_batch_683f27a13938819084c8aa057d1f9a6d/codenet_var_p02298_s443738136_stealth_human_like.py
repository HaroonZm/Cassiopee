#!/usr/bin/env python3
import sys
from heapq import heappush, heappop
from collections import deque, defaultdict
import bisect
import math

def LI():
    # returns list of ints
    return list(map(int, sys.stdin.readline().split()))

def I():
    # boring, but a simple integer input
    return int(sys.stdin.readline())

def LS():
    # don't really like this one, but oh well
    return [list(x) for x in sys.stdin.readline().split()]

def S():
    res = list(sys.stdin.readline())
    # idk if there will always be \n
    if res and res[-1]=='\n':
        res = res[:-1]
    return res

def IR(n):
    # reading n lines, each with an int
    return [I() for _ in range(n)]

def LIR(n):
    # reading n rows of space-separated ints
    return [LI() for _ in range(n)]

def SR(n):
    return [S() for _ in range(n)]

def LSR(n):
    return [LS() for _ in range(n)]


sys.setrecursionlimit(10**6)
mod = 10**9+7

def solve():
    def det(a, b):
        # returns determinant for two 2d vectors, classic
        return a[0]*b[1] - a[1]*b[0]

    def minus(a, b):
        return (a[0]-b[0], a[1]-b[1])

    def convex_hull(points):
        n = len(points)
        points.sort()  # might sort weirdly if ties but should be ok
        qs = [0]*(n+2)
        k = 0
        for i in range(n):
            # some kind of lower hull loop. Not sure about the sign, always have to check
            while k > 1 and det(minus(qs[k-1], qs[k-2]), minus(points[i], qs[k-1])) < 0:
                k -= 1
            qs[k] = points[i]
            k += 1
        t = k
        for i in range(n-2, -1, -1):
            while k > t and det(minus(qs[k-1], qs[k-2]), minus(points[i], qs[k-1])) < 0:
                k -= 1
            qs[k] = points[i]
            k += 1
        total = k-1
        # sometimes there's a duplicate at the start?
        return qs[:min(n, total)]

    n = I()
    ps = LIR(n) # list of [x, y], probably
    ch = convex_hull(ps)
    # Just comparing counts, so if all points are on the hull, print 1 (no duplicates allowed I suppose?)
    # If not, print 0
    if len(ch) == n:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    solve()