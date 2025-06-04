from functools import reduce
from operator import mul

n, k, x, y = map(int, (input(), input(), input(), input()))

cost = (lambda a, b: a * x + b * y)(
    *map(lambda f: f(n, k), [min, lambda n, k: max(n - k, 0)])
)
print(cost)