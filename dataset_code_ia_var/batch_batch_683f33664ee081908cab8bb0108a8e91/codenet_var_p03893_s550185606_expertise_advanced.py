from functools import reduce

x = int(input())
print(reduce(lambda acc, _: acc * 2 + 1, range(x), 3) - 1)