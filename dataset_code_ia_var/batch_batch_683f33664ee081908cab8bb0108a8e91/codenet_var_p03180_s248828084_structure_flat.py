N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]

cost = [0] * (1 << N)
bit = 0
while bit < (1 << N):
    i = 0
    while i < N:
        j = i + 1
        while j < N:
            if (bit >> i) & 1 and (bit >> j) & 1:
                cost[bit] += AB[i][j]
            j += 1
        i += 1
    bit += 1

dp = [0] * (1 << N)
s = 1
while s < (1 << N):
    t = s
    while t > 0:
        if dp[s] < dp[s - t] + cost[t]:
            dp[s] = dp[s - t] + cost[t]
        t = (t - 1) & s
    s += 1

print(dp[(1 << N) - 1])