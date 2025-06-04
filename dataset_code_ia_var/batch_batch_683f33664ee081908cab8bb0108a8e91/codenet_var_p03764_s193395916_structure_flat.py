MOD = 10**9+7
n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
i = 0
xx = 0
while i < n - 1:
    w = x[i + 1] - x[i]
    c = (i + 1) * (n - i - 1)
    xx = (xx + w * c) % MOD
    i += 1
j = 0
yy = 0
while j < m - 1:
    h = y[j + 1] - y[j]
    c = (j + 1) * (m - j - 1)
    yy = (yy + h * c) % MOD
    j += 1
ans = (xx * yy) % MOD
print(ans)