from functools import reduce
from operator import mul

MOD = 10**9 + 7
n = int(input())
print(reduce(lambda x, y: x * y % MOD, range(1, n+1), 1))