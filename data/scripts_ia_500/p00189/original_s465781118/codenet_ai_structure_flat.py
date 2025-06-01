import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    n_max = 10
    dp = [[float('inf')] * n_max for _ in range(n_max)]
    for i in range(n_max):
        dp[i][i] = 0
    max_town = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        dp[a][b] = c
        dp[b][a] = c
        if a > max_town:
            max_town = a
        if b > max_town:
            max_town = b
    V = max_town + 1
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dp[i][j] > dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
    min_dist = float('inf')
    town_live = -1
    for i in range(V):
        total = 0
        for j in range(V):
            total += dp[i][j]
        if total < min_dist:
            min_dist = total
            town_live = i
    print(town_live, min_dist)