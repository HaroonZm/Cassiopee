# python3

import sys
import math
import bisect
from fractions import gcd
from itertools import count, permutations
from functools import lru_cache
from collections import deque, defaultdict
from pprint import pprint

INF = float('inf')

ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
lmtx = lambda h: [list(map(int, lmis())) for _ in range(h)]
sys.setrecursionlimit(1000000000)

def lcm(a, b):
    return (a * b) // gcd(a, b)

# main
n, x, y = mis()

ans = [0] * n

for i in range(1, n):
    for j in range(i+1, n+1):
        ans[min(abs(j-i),
                abs(x-i)+1+abs(j-y),
                abs(y-i)+1+abs(j-x))] += 1

for i, a in zip(range(len(ans)), ans):
    if i == 0:
        continue
    print(a)