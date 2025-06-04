from functools import reduce
import operator

n = int(input())
print(reduce(operator.mul, range(1, n+1), 1))