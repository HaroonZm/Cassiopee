# region header
import sys
import math
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from copy import deepcopy
from fractions import gcd
from functools import lru_cache, reduce
from heapq import heappop, heappush
from itertools import accumulate, groupby, product, permutations, combinations, combinations_with_replacement
from math import ceil, floor, factorial, log, sqrt, sin, cos
from operator import itemgetter
from string import ascii_lowercase, ascii_uppercase, digits
sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 10 ** 9 + 7
def rs(): return sys.stdin.readline().rstrip()
def ri(): return int(rs())
def rf(): return float(rs())
def rs_(): return [_ for _ in rs().split()]
def ri_(): return [int(_) for _ in rs().split()]
def rf_(): return [float(_) for _ in rs().split()]
def divisors(n, sortedresult=True):
    div = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n//i)
    if sortedresult:
        div.sort()
    return div
# endregion
H, W = ri_()
S = [rs_() for _ in range(H)]
for i in range(H):
    for j in range(W):
        if S[i][j] == 'snuke':
            print('ABCDEFGHIJKLMNOPQRSTUVWXYZ'[j] + str(i + 1))