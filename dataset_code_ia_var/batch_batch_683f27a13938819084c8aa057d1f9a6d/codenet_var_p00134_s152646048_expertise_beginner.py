n = int(input())
prices = []
i = 0
while i < n:
    price = int(input())
    prices.append(price)
    i = i + 1
total = 0
j = 0
while j < len(prices):
    total = total + prices[j]
    j = j + 1
ans = int(total / n)
print(ans)