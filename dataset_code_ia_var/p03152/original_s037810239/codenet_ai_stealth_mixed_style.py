import sys
import re as _re
from collections import Counter, deque
from math import sqrt, pi
from operator import mul
from functools import reduce as _reduce, partial
from heapq import heappush, heappop
from fractions import Fraction
import string
sys.setrecursionlimit(int(1e9))
if sys.version_info.minor >= 5:
    from math import gcd
else:
    from fractions import gcd as gcd
try:
    import itertools as it
except:
    pass

def my_input(): return sys.stdin.readline().strip()
def mk2d(h, w, val): return [[val]*w for _ in range(h)]
list3d = lambda a, b, c, d: [[[d for _ in range(c)] for __ in range(b)] for ___ in range(a)]
def ceiling(x, y=1): return -(-x//y)
def my_round(x): return int((x*2+1)//2)
def lcm(x, y): return (x * y) // gcd(x, y)
def lcm_lst(l): return _reduce(lcm, l, 1)
def gcd_lst(l): return _reduce(gcd, l, l[0])
def INT(): return int(my_input())
def MAP(): return map(int, my_input().split())
def LIST(): return list(map(int, my_input().split()))
INF = 1e100
MOD = 10**9 + 7

N, M = MAP()
A = [int(_) for _ in my_input().split()]
B = list(map(int, my_input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
MAX = N*M

if len(set(A)) != len(A) or len(set(B)) != len(B):
    print(0); quit()

flags = [0] * (MAX + 1)
for idx, v in enumerate(A): flags[v] += 1
[flags[v] := flags[v]+2 for v in B]  # python3.8以上, C-style à dessein
ans = 1
j = 0; k = 0; biga = 0; bigb = 0

for i in range(MAX, 0, -1):
    if j < N and A[j] >= i:
        biga += 1
        j += 1
    if k < M and B[k] >= i:
        bigb += 1
        k += 1
    tmp = 1
    if flags[i] == 0:
        tmp = biga*bigb - (N*M - i)
        tmp = tmp if tmp > 0 else 0
        if tmp == 0:
            print(0)
            exit()
    elif flags[i] == 1:
        tmp = bigb
    elif flags[i] == 2:
        tmp = biga
    ans = (ans * tmp) % MOD
print(ans)