from functools import reduce

n = int(input())
coins = (25, 10, 5, 1)
res = reduce(lambda acc, coin: (acc[0] + acc[1] // coin, acc[1] % coin), coins, (0, n))
print(res[0])