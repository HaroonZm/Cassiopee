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
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
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

def solve():
    s = list(map(int, input()))
    t = list(input())
    n = len(t)
    for i in range(n):
        if t[i].isdecimal():
            t[i] = int(t[i])
    dp = [[[0]*2 for j in range(2)] for i in range(n+1)]
    dp[0][0] = [1,0]
    p = [pow(10,i,mod) for i in range(n)]
    for i in range(n):
        ni = i+1
        for j in range(2):
            if t[i] == "?":
                x = 9 if j else s[i]
                for d in range(x+1):
                    nj = j|(d < s[i])
                    dp[ni][nj][0] += dp[i][j][0]
                    dp[ni][nj][1] += dp[i][j][0]*d+10*dp[i][j][1]
                    dp[ni][nj][0] %= mod
                    dp[ni][nj][1] %= mod
            else:
                d = t[i]
                nj = j|(d < s[i])
                if d <= s[i]:
                    dp[ni][nj][0] += dp[i][j][0]
                    dp[ni][nj][1] += dp[i][j][0]*d+10*dp[i][j][1]
                    dp[ni][nj][0] %= mod
                    dp[ni][nj][1] %= mod
                else:
                    if nj:
                        dp[ni][nj][0] += dp[i][j][0]
                        dp[ni][nj][1] += dp[i][j][0]*d+10*dp[i][j][1]
                        dp[ni][nj][0] %= mod
                        dp[ni][nj][1] %= mod

    print((dp[-1][0][1]+dp[-1][1][1])%mod)
    return

if __name__ == "__main__":
    solve()