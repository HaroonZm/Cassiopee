import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
S = input().strip()

if S[0] != 'B' or S[-1] != 'B':
    print(0)
    sys.exit(0)

LR = [''] * N * 2
l = 0
ans = 1
m = 10**9+7

def mod_add(a, b):
    return (a + b) % m
def mod_sub(a, b):
    return (a - b) % m
def mod_mul(a, b):
    return ((a % m) * (b % m)) % m
def mod_div(a, b):
    return mod_mul(a, pow(b, m-2, m))
def mod_pow(a, b):
    return pow(a, b, m)

for i in range(2*N):
    if S[i] == 'B':
        if l % 2 == 0:
            LR[i] = 'L'
            l += 1
        else:
            LR[i] = 'R'
            ans = mod_mul(ans, l)
            l -= 1
    else:
        if l % 2 == 0:
            LR[i] = 'R'
            ans = mod_mul(ans, l)
            l -= 1
        else:
            LR[i] = 'L'
            l += 1

C = Counter(LR)
if C['L'] != C['R']:
    print(0)
    sys.exit(0)

for i in range(1, N+1):
    ans = mod_mul(ans, i)

print(ans)