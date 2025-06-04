from functools import reduce
from heapq import nlargest, nsmallest

inputs = [int(input()) for _ in range(6)]
total = reduce(
    lambda acc, val: acc + val,
    nlargest(3, inputs[:4]) + nlargest(1, inputs[4:]),
)
print(total)