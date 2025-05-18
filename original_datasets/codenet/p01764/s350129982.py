import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
inf = float("INF")
dp = [[inf] * (n + 1) for _ in range(n)]
for i in range(n - 1): a[i + 1] += a[i]
a.insert(0, 0)
f = [[0] * (n + 1) for i in range(n)]
for i in range(n):
    fi = f[i]
    for k in range(i + 1, n + 1):
        fi[k] = a[k]-a[i]
def time(l, m, r, res, x, fl):
    sumlm = fl[m]
    summr = f[m][r]
    c = 0
    while sumlm or summr or c:
        lm = sumlm % 10
        mr = summr % 10
        res += lm * mr + c
        if res >= x:
            return x
        c =  (lm + mr + c > 9)
        sumlm //= 10
        summr //= 10
    return res
for i in range(n):
    dp[i][i + 1] = 0

for Ra in range(1,n+1):
    for l in range(n-Ra+1):
        r = l+Ra
        dpl = dp[l]
        x = dpl[r]
        fl = f[l]
        for m in range(l+1, r):
            x = time(l, m, r,dpl[m] + dp[m][r], x, fl)
        dpl[r] = x

print(dp[0][n])