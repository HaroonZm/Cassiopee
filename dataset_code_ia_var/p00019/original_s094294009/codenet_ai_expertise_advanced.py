from functools import reduce
from operator import mul

n = int(input())
print(reduce(mul, range(1, n + 1), 1))