import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())

def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())

def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]

def SMI(): return input().split()
def SLI(): return list(input())

def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')

# from math import ceil, floor, log2
# from collections import deque
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np
# from numpy import cumsum  # accumulate

def solve():
    S = SLI()
    l = len(S)
    MOD = 1000000007
    dp = [[0]*13 for _ in range(l+1)]
    dp[0][0] = 1
    mul = 1
    R = S[::-1]
    for i in range(l):
        s = S[-(i + 1)]
        if s == '?':
            for q in range(10):
                for j in range(13):
                    dp[i+1][(q*mul + j)%13] += dp[i][j]
                    dp[i+1][(q*mul + j)%13] %= MOD
        else:
            for j in range(13):
                k = int(s)
                dp[i+1][(k*mul + j)%13] += dp[i][j]
                dp[i+1][(k*mul + j)%13] %= MOD

        mul = mul * 10 % 13
    # print(dp[-1])
    print(dp[-1][5] % MOD)

if __name__ == '__main__':
    solve()