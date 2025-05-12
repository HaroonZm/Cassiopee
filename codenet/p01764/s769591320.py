from collections import defaultdict
import sys
def calc(l,m,r,f,dp):
    a = f[l][m]
    b = f[m][r]
    res = dp[l][m]+dp[m][r]
    c = 0
    while a or b or c:
        a0 = a%10
        b0 = b%10
        res += a0*b0+c
        if res >= dp[l][r]:
            return dp[l][r]
        c = (a0+b0+c >= 10)
        a //= 10
        b //= 10
    return res

def solve():
    n = int(sys.stdin.readline())
    a = [int(x) for x in sys.stdin.readline().split()]
    dp = [[float("inf")]*(n+1) for i in range(n)]
    for i in range(n-1):
        a[i+1] += a[i]
    a.insert(0,0)
    f = [[0]*(n+1) for i in range(n)]
    for l in range(n):
        dp[l][l+1] = 0
        for r in range(l+1,n+1):
            f[l][r] = a[r]-a[l]
    for le in range(2,n+1):
        for l in range(n-le+1):
            r = l+le
            for m in range(l+1,r):
                dp[l][r] = calc(l,m,r,f,dp)
                
    print(dp[0][n])

if __name__ == "__main__":
    solve()