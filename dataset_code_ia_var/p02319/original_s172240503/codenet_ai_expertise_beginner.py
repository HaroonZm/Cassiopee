import sys

M_W = sys.stdin.readline().split()
M = int(M_W[0])
W = int(M_W[1])

prices = [0]
weights = [0]

for i in range(M):
    p_w = sys.stdin.readline().split()
    prices.append(int(p_w[0]))
    weights.append(int(p_w[1]))

total_price = sum(prices)
max_weight = W + 1

dp = []
for i in range(M+1):
    dp.append([max_weight] * (total_price + 1))

for i in range(M+1):
    dp[i][0] = 0

for i in range(1, M+1):
    for v in range(1, total_price+1):
        if v < prices[i]:
            dp[i][v] = dp[i-1][v]
        else:
            without_item = dp[i-1][v]
            with_item = dp[i-1][v-prices[i]] + weights[i]
            if with_item < without_item:
                dp[i][v] = with_item
            else:
                dp[i][v] = without_item

result = 0
for v in range(total_price + 1):
    if dp[M][v] <= W:
        if v > result:
            result = v

print(result)