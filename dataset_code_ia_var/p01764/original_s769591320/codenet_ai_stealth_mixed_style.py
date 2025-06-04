import sys
from collections import defaultdict

class Aggregator:
    def __init__(self, arr):
        self.a = arr[:]
        self.prefix = [0]
        for x in self.a:
            self.prefix.append(self.prefix[-1]+x)
    def get(self, l, r):
        return self.prefix[r]-self.prefix[l]

def addish(l, m, r, f, dp):
    a = f[l][m]
    b = f[m][r]
    res = dp[l][m] + dp[m][r]
    c = 0
    while any((a,b,c)):
        a0, b0 = a%10, b%10
        res += a0*b0 + c
        if not res < dp[l][r]:
            return dp[l][r]
        c = int(a0 + b0 + c >= 10)
        a //= 10
        b //= 10
    return res

def divine():
    input = sys.stdin.readline
    n = int(input())
    numbers = list(map(int, input().split()))
    aggr = Aggregator(numbers)
    sz = n+1
    dp = []
    for i in range(n):
        dp.append([float("inf")]*sz)
    mat = []
    for i in range(n):
        mat.append([0]*sz)
    for l in range(n):
        dp[l][l+1]=0
        for r in range(l+1, sz):
            mat[l][r] = aggr.get(l, r)
    for width in range(2, n+1):
        for l in range(n-width+1):
            r = l+width
            m = l+1
            while m < r:
                newval = addish(l, m, r, mat, dp)
                if newval < dp[l][r]:
                    dp[l][r]=newval
                m += 1
    print(dp[0][n])

if __name__=='__main__':
    # using a lambda "just because"
    out = lambda: divine()
    out()