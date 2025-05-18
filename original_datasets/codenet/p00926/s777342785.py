#!usr/bin/env python3
from collections import defaultdict
from collections import deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
import itertools
sys.setrecursionlimit(10**5)
stdin = sys.stdin
bisect_left = bisect.bisect_left
bisect_right = bisect.bisect_right
def LI(): return list(map(int, stdin.readline().split()))
def LF(): return list(map(float, stdin.readline().split()))
def LI_(): return list(map(lambda x: int(x)-1, stdin.readline().split()))
def II(): return int(stdin.readline())
def IF(): return float(stdin.readline())
def LS(): return list(map(list, stdin.readline().split()))
def S(): return list(stdin.readline().rstrip())
def IR(n): return [II() for _ in range(n)]
def LIR(n): return [LI() for _ in range(n)]
def FR(n): return [IF() for _ in range(n)]
def LFR(n): return [LI() for _ in range(n)]
def LIR_(n): return [LI_() for _ in range(n)]
def SR(n): return [S() for _ in range(n)]
def LSR(n): return [LS() for _ in range(n)]
mod = 1000000007
inf = float('INF')

#A
def A():
    s = S()
    m = II()
    ans = ["I", "L", "M", "U"]
    nu = 0
    stack = []
    bf = int(s[0])
    for num,si in enumerate(s):
        if si == "+":
            bf += int(s[num+1])
        elif si == "*":
            bf *= int(s[num + 1])
    if bf == m:
        nu += 1
    stack = []
    bf = 0
    for num, si in enumerate(s):
        if si == "*":
            s[num + 1] = int(s[num + 1]) * int(s[num - 1])
            s[num - 1] = 0
    for si in s:
        if si != "*" and si != "+":
            bf += int(si)
    if bf == m:
        nu += 2
    print(ans[nu])    

    return

#B
def B():
    n, m = LI()
    cd = LIR(m)
    dp = [0 for i in range(n+1)]
    for c, d in cd:
        dp[c] += 1
        dp[d] -= 1
    for i in range(n):
        dp[i + 1] += dp[i]
    ans = 0
    flg = 0
    for i in range(n):
        
        if dp[i]:
            ans += 3

        elif flg:
            flg = 0
            ans += 3

        else:
            ans += 1
    
    print(ans+1)
        
    return

#C
def C():
    return

#D
def D():
    return

#E
def E():
    return

#F
def F():
    return

#G
def G():
    return

#H
def H():
    return

#Solve
if __name__ == '__main__':
    B()