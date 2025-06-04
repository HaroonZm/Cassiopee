n, d, x = map(int, input().split())
prices = []
for i in range(d):
    prices.append(list(map(int, input().split())))

def get_profit(weights, values, money):
    dp = [0] * (money + 1)
    for i in range(len(weights)):
        w = weights[i]
        v = values[i]
        for m in range(w, money + 1):
            if dp[m] < dp[m - w] + v:
                dp[m] = dp[m - w] + v
    return dp[money]

for day in range(d - 1):
    adds = []
    items = []
    for product in range(n):
        adds.append(prices[day + 1][product] - prices[day][product])
        items.append(prices[day][product])
    x = x + get_profit(items, adds, x)
print(x)