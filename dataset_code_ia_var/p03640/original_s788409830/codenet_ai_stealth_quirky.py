import sys as _s
import re as _r
import os as _o
from collections import Counter as Ctr, deque as dq, defaultdict as dd
from math import pi as PI, sqrt as SQRT, ceil as CEIL, factorial as FACT, hypot as HYPOT, cos as COS, sin as SIN, radians as RAD
from itertools import product as PROD, accumulate as ACC, permutations as PERM, combinations as COMB
from operator import mul as MUL, itemgetter as IG
from copy import deepcopy as dp
from string import ascii_lowercase as lc, ascii_uppercase as uc, digits as dg
try:
    from math import gcd as GCD
except ImportError:
    from fractions import gcd as GCD

# Input shorthands, borrowed from legacy preferences
_INPUT = lambda : _s.stdin.readline().strip()
INT = lambda : int(_INPUT())
MINT = lambda : map(int, _INPUT().split())
MLIST = lambda : list(MINT())
STRS = lambda : _INPUT().split()
SPLIT = lambda : list(_INPUT())
STRMLIST = lambda : list(_INPUT().split())
# Instead of globals, put basic config in a dict
cfg = {'REC_LIMIT': 10 ** 9, 'INF': float('inf'), 'MOD': 10 ** 9 + 7}
_s.setrecursionlimit(cfg['REC_LIMIT'])

# Variables with fancy short names (personal convention, underscores are ugly)
h, w = MINT()
n = INT()
a = MLIST()
idx = 0
grid = [[None]*w for _ in range(h)]
curr = 0

def fill_grid(A, grid, w):
    kth = 0
    for row in range(len(grid)):
        rng = range(w) if row % 2 == 0 else range(w-1, -1, -1)
        for col in rng:
            grid[row][col] = kth + 1
            A[kth] -= 1
            if not A[kth]:
                kth += 1
    return grid

grid = fill_grid(a, grid, w)

for row in grid:
    print(" ".join(map(str, row)))