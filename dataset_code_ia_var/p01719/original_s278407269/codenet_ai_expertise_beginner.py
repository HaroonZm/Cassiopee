import sys

n, d, x = map(int, sys.stdin.readline().split())

pp = []
for i in range(d):
    pp.append(list(map(int, sys.stdin.readline().split())))

dp = [0] * 100001
cur_x = x

for k in range(d - 1):
    nex_x = cur_x
    # Remettre dp à zéro
    for i in range(cur_x + 1):
        dp[i] = 0
    for i in range(n):
        for j in range(cur_x + 1):
            if j - pp[k][i] >= 0:
                dp[j] = max(dp[j], dp[j - pp[k][i]] + pp[k + 1][i])
            # Mettre à jour le maximum
            if (cur_x - j) + dp[j] > nex_x:
                nex_x = (cur_x - j) + dp[j]
    cur_x = nex_x

print(cur_x)