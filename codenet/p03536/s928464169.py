N = int(input())
d = []
for i in range(N):
    h, p = map(int, input().split())
    d.append((h, p))

d = sorted(d, key=lambda x: x[0] + x[1])
INF = float('inf')
dp1 = [INF] * (N + 1)
dp2 = [INF] * (N + 1)
dp1[0] = 0
for i in range(1, N + 1):
    for j in range(N + 1):
        dp2[j] = dp1[j]
        if j == 0:
            continue
        if dp1[j - 1] > d[i - 1][0]:
            continue
        dp2[j] = min(dp2[j], dp1[j - 1] + d[i - 1][1])
    dp1, dp2 = dp2, dp1

for i in range(N, -1, -1):
    if dp1[i] < INF:
        print(i)
        exit()