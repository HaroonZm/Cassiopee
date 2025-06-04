import sys
import math
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from copy import deepcopy
from math import comb, isqrt
from functools import lru_cache, reduce, partial
from heapq import heappop, heappush
from itertools import accumulate, groupby, product, permutations, combinations, combinations_with_replacement, chain
from math import ceil, floor, factorial, log, sqrt, sin, cos
from operator import itemgetter
from string import ascii_uppercase
from typing import Any, Callable

sys.setrecursionlimit(10**6)
INF = float('inf')
MOD = 10**9 + 7

def rs() -> str:
    return sys.stdin.readline().rstrip()

def ri() -> int:
    return int(rs())

def rf() -> float:
    return float(rs())

def rs_() -> list[str]:
    return rs().split()

def ri_() -> list[int]:
    return list(map(int, rs().split()))

def rf_() -> list[float]:
    return list(map(float, rs().split()))

def divisors(n: int, sortedresult: bool = True) -> list[int]:
    small, large = [], []
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            small.append(i)
            if i != n // i:
                large.append(n // i)
    res = small + large[::-1]
    return sorted(res) if sortedresult else res

H, W = ri_()
S = [rs_() for _ in range(H)]

target = 'snuke'
for i, row in enumerate(S):
    for j, val in enumerate(row):
        if val == target:
            print(f"{ascii_uppercase[j]}{i+1}")