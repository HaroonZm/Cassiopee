from functools import reduce

x = int(input())
result = reduce(lambda n, _: n * 2 + 2, range(x), 2)
print(result)