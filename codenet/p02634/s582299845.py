a, b, c, d = map(int, input().split())
mod = 998244353
DP = [[0] * (d+1) for _ in range(c+1)]

DP[a][b] = 1
for y in range(a+1, c+1):
    DP[y][b] = DP[y-1][b] * b % mod

for x in range(b+1, d+1):
    DP[a][x] = DP[a][x-1] * a % mod

for y in range(a+1, c+1):
    for x in range(b+1, d+1):
        DP[y][x] = (DP[y-1][x] * x + (DP[y][x-1] - DP[y-1][x-1] * (x-1)) * y + DP[y-1][x-1] * (x-1)) % mod

print(DP[c][d])