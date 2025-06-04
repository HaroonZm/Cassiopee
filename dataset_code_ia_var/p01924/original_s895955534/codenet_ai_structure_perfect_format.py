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
eps = 1.0 / 10**10
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

    def f(t, d, l):
        a = [I() for _ in range(t)]
        r = [0] * t
        for i in range(t - 1, -1, -1):
            c = a[i]
            if c >= l:
                r[i] = 1
                for j in range(i + 1, min(i + d, t)):
                    if r[j] > 0:
                        break
                    r[j] = 1
        return sum(r[:-1])

    while 1:
        n, m, l = LI()
        if n == 0:
            break
        rr.append(f(n, m, l))

    return '\n'.join(map(str, rr))

print(main())