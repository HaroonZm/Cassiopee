from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
import math
import bisect
import random
from itertools import permutations, accumulate, combinations
import sys
import string
from bisect import bisect_left, bisect_right
from math import factorial, ceil, floor

INF = float('inf')
def LI(): return list(map(int, sys.stdin.readline().split()))
def I(): return int(sys.stdin.readline())
def LIM(): return list(map(lambda x:int(x) - 1, sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def LIRM(n): return [LIM() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def LSR(n): return [LS() for i in range(n)]
def SRL(n): return [list(S()) for i in range(n)]
mod = 1000000007

n, k = LI()

left = 0
right = 2 * 10 ** 18
L = LIR(n)
while left <= right:
    mid = (left + right) // 2
    flag = False
    ret = 0
    for w, d in L:
        if w == mid:
            ret += 1
        elif w < mid:
            ret += 1
            ret += (mid - w) // d
    if ret >= k:
        flag = True
        right = mid - 1
    else:
        flag = False
        left = mid + 1

if flag:
    print(mid)
else:
    print(mid + 1)