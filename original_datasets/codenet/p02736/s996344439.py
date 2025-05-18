#!/usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
from bisect import bisect_left, bisect_right
import sys, random, itertools, math
sys.setrecursionlimit(10**5)
input = sys.stdin.readline
sqrt = math.sqrt
def LI(): return list(map(int, input().split()))
def LF(): return list(map(float, input().split()))
def LI_(): return list(map(lambda x: int(x)-1, input().split()))
def II(): return int(input())
def IF(): return float(input())
def LS(): return list(map(list, input().split()))
def S(): return list(input().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = 1e10

#solve
def solve():
    n = II()
    a = list(map(lambda x: int(x) - 1, S()))
    ans = 1
    if not 1 in a:
        ans *= 2
        for i in range(n):
            a[i] >>= 1
    res = 0
    for i in range(n):
        #  ~ Lucas の定理から ~
        #  n C k において
        #  k の bitが立っているところについて
        #  n の bitが立っていない場合 n C k が 2の倍数になる
        #  これを超簡単にする方法 (Touristの提出を見た)
        if ((n - 1) & i == i):
            res ^= a[i] & 1
    print(res * ans)

    return

#main
if __name__ == '__main__':
    solve()