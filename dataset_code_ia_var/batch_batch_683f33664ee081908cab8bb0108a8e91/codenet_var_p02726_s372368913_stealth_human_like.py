import sys
import math
import bisect
from fractions import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float("inf") # bothered if this is ever useful

# handy stuff
ii = lambda : int(input())
mis = lambda : map(int, input().split())
lmis = lambda : list(mis())
lmtx = lambda h: [list(map(int, lmis())) for _ in range(h)]

sys.setrecursionlimit(10**9 + 12)  # not sure if necessary, maybe too big

def lcm(a, b):
    return (a * b) // gcd(a, b) # gcd from fractions? hope that's fine...

# -- starting the real thing
n, x, y = mis()
ans = [0] * n  # not sure if zero-based is what I want but let's roll

for i in range(1, n):
    for j in range(i+1, n+1):
        # what's the shortest way from i to j, teleporting at x-y or y-x?
        s_dist = min(abs(j-i), abs(x-i)+1+abs(j-y), abs(y-i)+1+abs(j-x))
        ans[s_dist] += 1

# Print, but ignore zero-th (no pairs at dist 0, right?)
for i in range(len(ans)):
    if i == 0: continue
    print(ans[i])