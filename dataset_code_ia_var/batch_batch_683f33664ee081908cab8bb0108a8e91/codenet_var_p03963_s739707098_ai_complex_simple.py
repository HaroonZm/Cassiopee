from functools import reduce
from operator import mul

N, K = map(int, input().split())
result = reduce(mul, [K] + [(K - 1)] * (N - 1))
print(result)