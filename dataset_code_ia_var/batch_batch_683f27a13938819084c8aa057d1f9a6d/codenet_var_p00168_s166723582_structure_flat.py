from math import ceil

INF = int(1e18)
DP = [INF for _ in range(32)]
DP[1] = 1
DP[2] = 1
DP[3] = 2
i = 4
while i < 32:
    DP[i] = DP[i - 1] + DP[i - 2] + DP[i - 3]
    i += 1

while True:
    n = int(input())
    if n == 0:
        break
    res = DP[n + 1] / 3650
    if res != int(res):
        out = int(res) + 1
    else:
        out = int(res)
    print(out)