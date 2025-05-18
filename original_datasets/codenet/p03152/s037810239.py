import sys, re
from collections import deque, defaultdict, Counter
from math import sqrt, hypot, factorial, pi, sin, cos, radians
if sys.version_info.minor >= 5: from math import gcd
else: from fractions import gcd 
from heapq import heappop, heappush, heapify, heappushpop
from bisect import bisect_left, bisect_right
from itertools import permutations, combinations, product
from operator import itemgetter, mul
from copy import deepcopy
from functools import reduce, partial
from fractions import Fraction
from string import ascii_lowercase, ascii_uppercase, digits

def input(): return sys.stdin.readline().strip()
def list2d(a, b, c): return [[c] * b for i in range(a)]
def list3d(a, b, c, d): return [[[d] * c for j in range(b)] for i in range(a)]
def ceil(x, y=1): return int(-(-x // y))
def round(x): return int((x*2+1) // 2)
def fermat(x, y, MOD): return x * pow(y, MOD-2, MOD) % MOD
def lcm(x, y): return (x * y) // gcd(x, y)
def lcm_list(nums): return reduce(lcm, nums, 1)
def gcd_list(nums): return reduce(gcd, nums, nums[0])
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7

N, M = MAP()
# あとで大きい値から数えたいので降順ソートしておく
A = sorted(LIST(), reverse=True)
B = sorted(LIST(), reverse=True)
MAX = N * M

# 同じリストに同じ値がいたら論外
# (各値1回ずつしか使えないのに、違う行で最大値が同じとか不可能)
if len(A) != len(set(A)) or len(B) != len(set(B)):
    print(0)
    exit()

# 1: Aにある, 2: Bにある, 3: 両方にある, 0: どちらにもない
flags = [0] * (MAX+1)
for i in range(N):
    flags[A[i]] += 1
for i in range(M):
    flags[B[i]] += 2

ans = 1
j = k = biga = bigb = 0
for i in range(MAX, 0, -1):
    # リスト内の、自分iより大きい値の数を数えながら進める
    if j != N and A[j] >= i:
        biga += 1
        j += 1
    if k != M and B[k] >= i:
        bigb += 1
        k += 1
    tmp = 1
    # どちらにもない
    if flags[i] == 0:
        # Aで自分以上の数 * Bで自分以上の数 - 自分以上の数
        tmp = biga * bigb - (N*M-i)
        if tmp <= 0:
            print(0)
            exit()
    # Aにある
    elif flags[i] == 1:
        # 自分の行が決まっているので、列を調べに行く
        tmp = bigb
    # Bにある
    elif flags[i] == 2:
        tmp = biga
    ans = (ans * tmp) % MOD
print(ans)