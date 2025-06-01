pasta_prices = [int(input()) for _ in range(3)]
juice_prices = [int(input()) for _ in range(2)]

min_price = min(p + j for p in pasta_prices for j in juice_prices) - 50
print(min_price)