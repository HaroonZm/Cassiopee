import math as m
import string
import itertools as it
from fractions import Fraction
from heapq import *
import collections
import re, array, bisect, sys, random
import time
from copy import deepcopy
import functools as ft

sys.setrecursionlimit(10**7)
INF = float('inf')
EPS = 1e-10
MOD = 10**9 + 7

LI = lambda : list(map(int, sys.stdin.readline().split()))
LI_ = lambda: list(map(lambda x: int(x)-1, sys.stdin.readline().split()))
def LF(): return [float(i) for i in sys.stdin.readline().split()]
LS = lambda : sys.stdin.readline().split()
I = lambda : int(sys.stdin.readline())
F = lambda : float(sys.stdin.readline())
def S():
    return input()
pf = lambda s: print(s, flush=True)

def main():

    out = list()
    D = [(0,-1), (1,0), (0,1), (-1,0)]

    def points(n):
        coords = [(0,0)]
        for _ in range(n-1):
            i,d = LI()
            xi,yi = coords[i]
            dx,dy = D[d]
            coords.append((xi+dx, yi+dy))
        return coords

    getx = lambda arr: [x for (x,_) in arr]
    gety = lambda arr: [y for (_,y) in arr]

    n = -1
    while 1:
        n = I()
        if n==0:
            break
        pos = points(n)
        xs = sorted(getx(pos))
        ys = sorted(gety(pos))
        w = xs[-1]-xs[0]+1
        h = ys[-1]-ys[0]+1
        out.append("{0} {1}".format(h, w))

    return '\n'.join(map(str, out))

if __name__=='__main__': print(main())