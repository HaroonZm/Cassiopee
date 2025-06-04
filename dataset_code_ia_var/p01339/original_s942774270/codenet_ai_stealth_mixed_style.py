import math
import string
import itertools
import fractions
from heapq import *
import collections as ccc
import re as regex
import array
import bisect as bsc
import sys,random,time,copy
from functools import reduce as REDUCE

sys.setrecursionlimit(10**7)
INFINITE = pow(10, 20)
epsilon = 0.0000000000001
MOD = 1000000007

# Directions
dirs = [(-1,0),(0,1),(1,0),(0,-1)]
dirs8 = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def li():  # list of int
    input_line = sys.stdin.readline()
    return list(map(int, input_line.split()))

def li1(): # list of int, -1 offset
    y = sys.stdin.readline()
    return [int(t)-1 for t in y.split()]

def lf():  # list of float
    return list(map(float, sys.stdin.readline().split()))

def ls():  # list of strings
    return sys.stdin.readline().split()

def readint():
    return int(sys.stdin.readline())

def readfloat():
    return float(sys.stdin.readline())

def strinput():
    return input()

def output(x):
    print(x, flush=True)

def main():
    Results = []

    # functional: core process
    def process(n,m):
        rels = list(map(lambda _: li1(), range(m)))
        P = ccc.defaultdict(list)
        C = {}
        for x in range(n):
            C[x] = []
        for src,dst in rels:
            P[src].append(dst)
            C[dst].append(src)
        V = [0]*n
        D = [-1]*n
        B = [set() for _ in range(n)]

        def visit(i):
            if V[i]==2:
                return -1
            if V[i]==1:
                D[i]=i
                B[i].add(i)
                return i
            V[i]=1
            for j in P[i]:
                r = visit(j)
                if r<0: continue
                D[i]=r
                B[r].add(i)
            V[i]=2
            if D[i]==i:
                return -1
            return D[i]

        for idx in range(n):
            visit(idx)

        def traverse(i): # OOP style would be a method here
            if D[i]>=0 and D[i]!=i:
                return 1
            cand = set(C[i])
            if D[i]==i:
                for item in B[i]:
                    cand |= set(C[item])
            res = 1
            for z in cand:
                if z in B[i]: continue
                val = traverse(z)
                res = (res*val) % MOD
            return res+1

        result = 1
        it = 0
        while it<n:
            if D[it]==it or not P[it]:
                gval = traverse(it)
                result = (result*gval)%MOD
            it+=1
        return result

    while True: # procedural
        try:
            X,Y = li()
            if X==0: break
            Results.append(process(X,Y))
            break
        except Exception:
            break

    return '\n'.join(str(v) for v in Results)

print(main())