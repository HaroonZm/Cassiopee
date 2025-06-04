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
eps = 1.0 / 10 ** 13
mod = 10 ** 9 + 9
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

class Flow():
    def __init__(self, e, N):
        self.EE = collections.defaultdict(set)
        for i in range(N):
            self.EE[i] |= e[i]
        self.E = e
        self.N = N
        self.nl = list(range(N))
        self.R = 0

    def max_flow(self, s, t):
        e = self.E
        v = None

        def f(c):
            v[c] = 1
            if c == t:
                return 1
            for i in e[c]:
                if v[i] is None and f(i):
                    if c in e[i]:
                        e[c].remove(i)
                    else:
                        e[i].add(c)
                    return 1
            return

        while True:
            v = [None] * self.N
            if f(s) is None:
                break
            self.R += 1

        return self.R

    def max_flow_add(self, s, t, u, v):
        self.E[u].add(v)
        self.E[v].add(u)
        self.EE[u].add(v)
        self.EE[v].add(u)
        return self.max_flow(s, t)

    def del_path_st(self, u, v, s, t):
        e = self.E
        vv = [None] * self.N

        def f(c):
            vv[c] = 1
            if c == v:
                return 1
            for i in e[c]:
                if vv[i] is None and f(i):
                    if c in e[i]:
                        e[c].remove(i)
                    else:
                        e[i].add(c)
                    return 1
            return

        if f(u):
            return

        uu = self.del_path_s(u, s)
        tt = self.del_path_s(t, v)
        self.R -= 1

    def del_path_s(self, u, s):
        e = self.E
        ee = self.EE
        v = [None] * self.N

        def f(c):
            if v[c]:
                return
            v[c] = 1
            if c == s:
                return 1
            for i in e[c]:
                if c in e[i]:
                    continue
                if f(i):
                    e[i].add(c)
                    return 1
            return

        return f(u)

    def max_flow_del(self, s, t, u, v):
        e = self.E
        ee = self.EE
        ee[u].remove(v)
        ee[v].remove(u)
        if v in e[u] and u in e[v]:
            e[u].remove(v)
            e[v].remove(u)
        elif v in e[u]:
            e[u].remove(v)
            self.del_path_st(v, u, s, t)
        else:
            e[v].remove(u)
            self.del_path_st(u, v, s, t)
        return self.max_flow(s, t)

def main():
    rr = []

    def f(n, e, q):
        ft = [LI() for _ in range(e)]
        mab = [LI() for _ in range(q)]
        e = collections.defaultdict(set)
        for fi, ti in ft:
            e[fi].add(ti)
            e[ti].add(fi)
        fl = Flow(e, n + 1)
        r = []
        for m, a, b in mab:
            if m == 1:
                r.append(fl.max_flow_add(1, n, a, b))
            else:
                r.append(fl.max_flow_del(1, n, a, b))
        return r

    while 1:
        n, m, l = LI()
        if n == 0:
            break
        rr.extend(f(n, m, l))
        break

    return '\n'.join(map(str, rr))

print(main())