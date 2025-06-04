from functools import reduce

target = int(input())
coins = (25, 10, 5, 1)
ans, _ = reduce(lambda acc, coin: (acc[0] + acc[1] // coin, acc[1] % coin), coins, (0, target))
print(ans)