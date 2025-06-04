coins = [i*i for i in range(1,18)]
dp = [1] + [0]*300
for c in coins:
    for i in range(c,301):
        dp[i] += dp[i-c]
while True:
    n = int(input())
    if n == 0:
        break
    print(dp[n])