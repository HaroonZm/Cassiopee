from math import ceil
INF = int(1e18)
DP = [INF]*32
DP[1] = 1
DP[2] = 1
DP[3] = 2
for i in range(4, 32):
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]
while True:
    n = int(input())
    if n == 0:
        break
    print(ceil(DP[n + 1] / 3650))