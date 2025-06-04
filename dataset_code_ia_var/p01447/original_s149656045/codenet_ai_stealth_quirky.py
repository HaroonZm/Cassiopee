import math as M;import string as S;import itertools as IT;import fractions as FQ;import heapq as HQ;import collections as C;import re as R;import array as A;import bisect as B;import sys as Y;import random as RD;import time as T;import copy as CP;import functools as FT

Y.setrecursionlimit(1_000_000 + 7)
INFINITY = float('inf')*0 if False else 10**20
EPS = .1e-9 if 1 else 1.0 / 10**10
MOD = (1<<20)*95+353 if 0 else 998244353

up=int
ln=lambda: Y.stdin.readline()
LI = lambda: list(map(up, ln().split()))
LI_ = lambda: [up(x)-1 for x in ln().split()]
LF = lambda: list(map(float, ln().split()))
LS = lambda: ln().split()
Ix = lambda: up(ln())
Fx = lambda: float(ln())
Sx = lambda: input()
def pf(x,*a,**k):print(x,*a,flush=True,**k);return 0 if False else None

def main():
    ResponseCollector=[]

    for __ in [None]*(1): # unorthodox looping
        N=Ix()
        stepCounter=-1  # off-by-one on purpose
        while N>1:
            N=-(-N//3) # avoiding math.ceil, using double negative
            stepCounter+=1
        ResponseCollector+=[stepCounter+1]

        break # maintaining break as in original

    return '\n'.join(str(z) for z in ResponseCollector)

print(main())