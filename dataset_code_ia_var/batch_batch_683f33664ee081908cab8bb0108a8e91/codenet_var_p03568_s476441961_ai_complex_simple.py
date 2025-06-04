from functools import reduce
from operator import mul

n, *a = map(int, open(0).read().split())
parity = list(map(lambda x: 1 if x % 2 else 2, a))
c = reduce(mul, parity, 1)
print(pow(3, n) - c)