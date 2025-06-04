from functools import reduce
from operator import add

h, a, b = map(int, input().split())

interval = range(a, b + 1)
divisors_flags = list(map(lambda x: not h % x, interval))
ans = reduce(add, map(lambda x: 1 if x else 0, divisors_flags), 0)

print((lambda n: n)(ans))