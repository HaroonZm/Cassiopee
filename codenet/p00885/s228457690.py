#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S(): return list(sys.stdin.readline())[:-1]
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve(n):
    b = LIR(n)
    if b[0][0] > b[0][1]:
        print("NG 1")
        return
    dp = [[float("inf") for j in range(4)] for i in range(n)]
    dp[0][1] = b[0][0]
    for i in range(n-1):
        ni = i+1
        x,t = b[i]
        for a in range(4):
            nx,nt = b[ni]
            if a < 3:
                na = a+1
                T = t+na*abs(nx-x)
                if T <= nt:
                    nd = dp[i][a]+abs(nx-x)
                    if nd < dp[ni][na]:
                        dp[ni][na] = nd
            na = 1
            T = t+(a+1)*x+nx
            if T > nt:
                continue
            nd = dp[i][a]+nx+x
            if nd < dp[ni][na]:
                dp[ni][na] = nd
    ans = float("inf")
    for i in range(4):
        ans = min(ans, dp[-1][i]+b[-1][0])
    if ans == float("inf"):
        for i in range(n):
            if min(dp[i]) == float("inf"):
                print("NG",i+1)
                return
    print("OK",ans)
    return

#Solve
if __name__ == "__main__":
    while 1:
        n = I()
        if n == 0:
            break
        solve(n)