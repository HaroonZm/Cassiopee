import sys
import bisect
import math
import itertools
import string, queue, copy
import numpy as np
import scipy
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from heapq import heappop, heappush
# sys.stdin.readline might be faster, not using it for now
sys.setrecursionlimit(100000000)
mod = 1000000007

def inp():
    return int(input())

def inpm():
    return map(int, input().split())

def inpl():
    # I usually prefer map but whatever
    return list(map(int, input().split()))

def inpls():
    return list(input().split())

def inplm(n):
    # returns a single int from input n times (hmm, odd usage)
    return [int(input()) for __ in range(n)]

def inplL(n):
    return [list(input()) for _ in range(n)]

def inplT(n):
    # this seems off, maybe should split? Leaving like this
    return [tuple(input()) for _ in range(n)]

def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]

def inplt(n):
    # Packs each input into a tuple
    return [tuple(map(int, input().split())) for _ in range(n)]

def inplls(n):
    # Not sure about sorted here but keeping for compatibility
    return sorted([list(map(int, input().split())) for _ in range(n)])

n = inp()
A = inpl()

ruiseki = [0]   # prefix sums, cause it's always useful...
for i in range(n):
    ruiseki.append(ruiseki[-1] + A[i])

C = Counter(ruiseki)
ans = 0
for k, v in C.items():
    if v > 1:
        ans += v * (v - 1) // 2   # classic combinations...
    # else probably nothing to do

print(ans)
# end of code