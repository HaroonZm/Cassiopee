from functools import reduce
from operator import mul

n = int(input())
a = list(map(int, input().split()))

count = sum(map(lambda x: (lambda y: 1 if y == 0 else 0)(x % 2), a))

result = reduce(mul, [3] * n, 1) - pow(2, count)

print(result)