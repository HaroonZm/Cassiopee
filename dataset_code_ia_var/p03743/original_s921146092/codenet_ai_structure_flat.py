N, D = map(int, input().split())
d = list(map(int, input().split()))
dp = [D] * N
if abs(D - d[0]) < D:
    dp[0] = abs(D - d[0])
i = 1
while i < N:
    dp[i] = min(dp[i-1], abs(dp[i-1] - d[i]))
    i += 1
ans = ["NO"] * N
data = [0] * (N + 1)
i = N - 1
while i > 0:
    if d[i] // 2 > data[i+1]:
        data[i] = data[i+1]
    else:
        data[i] = data[i+1] + d[i]
    if dp[i-1] > data[i+1]:
        ans[i] = "YES"
    i -= 1
i = 0
if d[i] // 2 > data[i+1]:
    data[i] = data[i+1]
else:
    data[i] = data[i+1] + d[i]
if D > data[i+1]:
    ans[i] = "YES"
Q = int(input())
q = list(map(int, input().split()))
i = 0
while i < Q:
    print(ans[q[i]-1])
    i += 1