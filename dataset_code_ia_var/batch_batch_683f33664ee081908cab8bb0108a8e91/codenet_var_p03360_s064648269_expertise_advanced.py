from operator import add
from functools import reduce

A, B, C = map(int, input().split())
K = int(input())

values = [A, B, C]
max_val = max(values)
result = reduce(add, values) + max_val * ((1 << K) - 1)
print(result)