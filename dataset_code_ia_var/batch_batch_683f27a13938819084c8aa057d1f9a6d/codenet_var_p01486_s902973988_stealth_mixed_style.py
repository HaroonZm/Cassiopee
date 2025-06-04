import math
import string
import itertools as IT
import fractions
import heapq as hq
import collections as col
import re, array
import bisect
import sys
import random
import time
from copy import deepcopy
from functools import reduce, lru_cache

setattr(sys, 'setrecursionlimit', 10**7)
INFINITY = pow(10,20)
EPS = 1 / pow(10,10)
MODULO = 998244353
DIRS = [(0,-1),(1,0),(0,1),(-1,0)]
ALLDIRS = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,1)]

LI = lambda: list(map(int, sys.stdin.readline().split()))
LI_ = lambda: [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return list(map(float, sys.stdin.readline().split()))
def LS():
    return sys.stdin.readline().split()
def I():
    return int(sys.stdin.readline())
def F():
    return float(sys.stdin.readline())
def S(): return input()
def pf(msg): print(msg, end='\n', flush=True)

def main():
    # imperative style for reading input
    s = S()
    sz = len(s)
    dct = col.defaultdict(int)
    memo = dict()
    memo[''] = 1

    # Object-oriented: a function as a callable object
    class Checker:
        def __init__(self):
            self.lookup = memo
        def __call__(self, x):
            if x in self.lookup:
                return self.lookup[x]
            if not (x.startswith('m') and x.endswith('w')):
                self.lookup[x] = 0
                return 0
            ln = len(x)
            for idx in range(1,ln-1):
                if x[idx] != 'e':
                    continue
                # recursion mixed with ternary
                lft = self(x[1:idx])
                rgt = self(x[idx+1:-1]) if (ln > 0) else 0
                if lft and rgt:
                    self.lookup[x] = 1
                    return 1
            self.lookup[x] = 0
            return 0

    check = Checker()

    # functional style for output
    return (lambda t: 'Cat' if t else 'Rabbit')(check(s))

print(main())