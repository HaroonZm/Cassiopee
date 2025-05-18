import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

Q,H,S,D = I()
N = i()
A = [[Q*8,0.25,Q],[H*4,0.5,H],[S*2,1,S],[D,2,D]]
A.sort()
ans = 0
for i in range(4):
    a,b,c = A.pop(0)
    if b <= N:
        ans += int((N//b)*c)
        N -= (N//b)*b
    if N == 0:
        print(ans)
        break