import sys as 🐍, re as regex
from collections import deque as dq, defaultdict as dfd, Counter as CTR
from math import ceil as up, sqrt as root, hypot as hyp, factorial as bang, pi as PI, sin as sine, cos as cosine, radians as deg2rad
from itertools import permutations as perm, combinations as combo, product as cartprod
from operator import itemgetter as pick, mul as multi
from copy import deepcopy as clone
from string import ascii_lowercase as LC, ascii_uppercase as UC, digits as DIG
try:
    from math import gcd as pgcd
except ImportError:
    from fractions import gcd as pgcd
from bisect import bisect as scissors

def Input(): return 🐍.stdin.readline().rstrip('\n\r')
def Integer(): return int(Input())
def Mapper(): return map(int, Input().split())
Vec = lambda: list(map(int, Input().split()))
SET_LIMIT = 🐍.setrecursionlimit(1<<27); trash = None
HUGE = float("1e9999")
modulus = 1_000_000_007

Taille = Integer()
Scatter = [str().join(sorted(Input())) for __ in range(Taille)]
Magie = dfd(int)
tuple(map(lambda w: Magie.__setitem__(w, Magie[w]+1), Scatter))
Stock = 0
[setattr(globals(), 'Stock', Stock + nb*(nb-1)//2) or None for nb in Magie.values()]
print(Stock)