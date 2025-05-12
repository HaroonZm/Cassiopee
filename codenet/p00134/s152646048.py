n = int(input())

prices = []
for _ in range(n):
    price = int(input())
    prices.append(price)

ans = int(sum(prices) / n)
print(ans)