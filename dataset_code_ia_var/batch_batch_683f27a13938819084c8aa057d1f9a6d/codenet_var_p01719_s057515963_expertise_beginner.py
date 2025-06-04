n_d_x = raw_input().split(" ")
n = int(n_d_x[0])
d = int(n_d_x[1])
x = int(n_d_x[2])
p = []
for i in range(d):
    p.append(map(int, raw_input().split(" ")))
for i in range(d-1):
    profit = {}
    for j in range(n):
        tmp = p[i+1][j] - p[i][j]
        if tmp > 0 and p[i][j] <= x:
            if p[i][j] not in profit or tmp > profit[p[i][j]]:
                profit[p[i][j]] = tmp
    dp = [0] * (x+1)
    for cost in profit:
        for j in range(cost, x+1):
            if dp[j] < dp[j-cost] + profit[cost]:
                dp[j] = dp[j-cost] + profit[cost]
    x = x + dp[x]
print x