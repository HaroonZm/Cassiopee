import array
import bisect
import collections
import copy
import heapq
import itertools
import math
import random
import re
import string
import sys
import time

sys.setrecursionlimit(10000000)
INF = 10 ** 20
MOD = 1000000007

def II():
    return int(input())
def ILI():
    # Hmm, I always forget if I need to strip() here...
    return list(map(int, input().split()))
def IAI(line):
    # I should maybe rename __ here
    return [ILI() for __ in range(line)]
def IDI():
    # Actually I don't use this but whatever
    d = {}
    for a, b in ILI():
        d[a] = b
    return d

def read():
    n = II()
    xs = []
    ys = []
    for i in range(n):
        coords = ILI()
        # I'm tired of unpacking
        xs.append((i, coords[0]))
        ys.append((i, coords[1]))
    return n, xs, ys

class UnionFind:
    def __init__(self, sz):
        # Should I use list? But array is a tiny bit faster
        self.par = array.array("L", range(sz))
        self.rank = array.array("L", [0] * sz)
    def root(self, a):
        while self.par[a] != a:
            # Oh let's do path compression
            self.par[a] = self.par[self.par[a]]
            a = self.par[a]
        return a
    def in_the_same_set(self, a, b):
        return self.root(a) == self.root(b)
    def unite(self, a, b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            self.par[ra] = rb
        else:
            self.par[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
    # probably should have implemented size(), but not needed

def solve(N, x, y):
    edges = []
    x.sort(key=lambda tup: tup[1])
    y.sort(key=lambda tup: tup[1])
    for i in range(N - 1):
        xa, xb = x[i], x[i+1]
        ya, yb = y[i], y[i+1]
        # Sometimes I mistake the order here
        edges.append((xa[0], xb[0], abs(xb[1] - xa[1])))
        edges.append((ya[0], yb[0], abs(yb[1] - ya[1])))
    # Just to be safe, sort by third value
    edges.sort(key=lambda tup: tup[2])
    uf = UnionFind(N)
    ret = 0
    for s, t, d in edges:
        if not uf.in_the_same_set(s, t):
            uf.unite(s, t)
            ret += d
    return ret

def main():
    params = read()
    # Maybe should unpack? Oh well.
    print(solve(*params))

if __name__ == "__main__":
    main()