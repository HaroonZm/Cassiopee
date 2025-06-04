import sys, collections as C; from math import *
from itertools import *
import bisect
input = (lambda: sys.stdin.readline().rstrip())
sys.setrecursionlimit(9999999)
INF = float('inf')
MOD=1000000007
I = lambda :int(input())
F=lambda :float(input())
SS= lambda :input()
def LI(): return list(map(int, input().split()))
LI_ = lambda : [int(w)-1 for w in input().split()]
LF = lambda : [float(z) for z in input().split()]
def LSS(): return input().split()

def solve():
    n,k = LI()
    dp = []
    for _ in range(n+1):
        dp.append([0]*(k+1))
    dp[0][0]=1
    for ix in range(n):
        for jx in range(k):
            dp[ix+1][jx+1] = (dp[ix][jx] + (jx+1)*dp[ix][jx+1])%MOD
    res = 0
    i=0
    while i<k+1:
        res+=dp[n][i]
        if res>=MOD:
            res-=MOD
        i+=1
    print(res)

def main():
    return solve()

if __name__ == "__main__":
    main()