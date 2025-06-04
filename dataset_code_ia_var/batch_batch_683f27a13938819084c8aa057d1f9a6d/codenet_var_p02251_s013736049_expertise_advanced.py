from functools import reduce

n = int(input())
coins = (25, 10, 5, 1)
count = reduce(lambda acc, c: (acc[0] % c, acc[1] + acc[0] // c), coins, (n, 0))[1]
print(count)