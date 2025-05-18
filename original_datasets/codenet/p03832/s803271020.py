def examC():
    ans = 0
    print(ans)
    return

def examD():
    ans = 0
    print(ans)
    return

def examE():
    class combination():
        # 素数のmod取るときのみ　速い
        def __init__(self, n, mod):
            self.n = n
            self.mod = mod
            self.fac = [1] * (n + 1)
            self.inv = [1] * (n + 1)
            for j in range(1, n + 1):
                self.fac[j] = self.fac[j - 1] * j % mod

            self.inv[n] = pow(self.fac[n], mod - 2, mod)
            for j in range(n - 1, -1, -1):
                self.inv[j] = self.inv[j + 1] * (j + 1) % mod

        def comb(self, n, r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.fac[n] * self.inv[n - r] * self.inv[r] % self.mod
        def combinv(self,n,r):
            if r > n or n < 0 or r < 0:
                return 0
            return self.inv[n] * self.fac[n - r] * self.fac[r] % self.mod
    N, A, B, C, D = LI()
    Comb = combination(N+1,mod)
    dp = [[0]*(N+1)for _ in range(B+1)]
    for i in range(A):
        dp[i][0] = 1
    for i in range(A,B+1):
        for j in range(N+1):
            loop = (N-j) // i + 1
            cnt_comb = 1
            dp[i][j] += dp[i-1][j]
            for k in range(C):
                cnt_comb *= Comb.comb(N-j-k*i,i)
                cnt_comb %= mod
            for k in range(C,min(loop,D+1)):
                dp[i][k*i+j] += dp[i-1][j]*cnt_comb * Comb.inv[k]
                dp[i][k*i+j] %= mod
                cnt_comb *= Comb.comb(N-j-k*i,i)
                cnt_comb %= mod
                #print(Comb.comb(N-j-k*i,i),Comb.inv[k+1])
    #print(dp)
    ans = dp[-1][-1]%mod
    print(ans)
    return

def examF():
    ans = 0
    print(ans)
    return

from decimal import Decimal as dec
import sys,bisect,itertools,heapq,math,random
from copy import deepcopy
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
def I(): return int(input())
def LI(): return list(map(int,sys.stdin.readline().split()))
def DI(): return dec(input())
def LDI(): return list(map(dec,sys.stdin.readline().split()))
def LSI(): return list(map(str,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def SI(): return sys.stdin.readline().strip()
global mod,mod2,inf,alphabet,_ep
mod = 10**9 + 7
mod2 = 998244353
inf = 10**18
_ep = dec("0.000000000001")
alphabet = [chr(ord('a') + i) for i in range(26)]
alphabet_convert = {chr(ord('a') + i): i for i in range(26)}

sys.setrecursionlimit(10**7)

if __name__ == '__main__':
    examE()

"""
10 1 1 1 10
"""