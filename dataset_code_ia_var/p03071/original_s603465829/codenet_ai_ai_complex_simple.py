from functools import reduce
from operator import add, mul

A, B = map(int, input().split())
choices = sorted([A, B], reverse=True)
result = reduce(add, (choices[0], max(choices[0] - 1, choices[1])))
print(result)