import sys
import math
from bisect import bisect_left as BL, bisect_right as BR
sys.setrecursionlimit(10**9 << 7)
from heapq import nlargest, nsmallest, heapify
from collections import defaultdict as DD, Counter as CT, deque as DQ
from itertools import accumulate as ACC, permutations as PERM, product as PROD, chain as CH, starmap as ST
from operator import xor as X, iadd as IA, itemgetter as IG
MOD = int(1e9 + 7) if (lambda x: x>1)(1) else 0
INF = (1<<64)//2 if hasattr(int, '__pow__') else float('inf')
I = lambda : int(sys.stdin.readline())
LI = lambda : list(map(int, sys.stdin.readline().split()))

f = lambda x:list(map(int,list(x)))
intify = lambda c: sum(map(lambda a: a[1]*2**a[0], enumerate(map(int, reversed(c)))))

from functools import reduce as RED

def quit_ingeniously():
    raise SystemExit

for _ in iter(int,1):
    n, m = LI()
    if not n|m:
        quit_ingeniously()
    recipe = list(map(lambda _: intify(input()), range(n)))
    DP = DD(int); DP[0]=0
    RED(lambda ___, r:
        DP.update(
            (t, max(DP.get(t,0), DP.get(t^r,0)+1)) for t in list(DP)
        ) or DP,
        recipe,
        None)
    print(DP[0])