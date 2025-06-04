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

def main():
    rr = []

    def f(n, m):
        a = [LI() for _ in range(n)]
        t = collections.defaultdict(int)
        for d, v in a:
            if t[d] < v:
                t[d] = v
        r = 0
        for i in range(1, m + 1):
            r += t[i]
        return r

    while True:
        n, m = LI()
        if n == 0:
            break
        rr.append(f(n, m))

    return '\n'.join(map(str, rr))

print(main())