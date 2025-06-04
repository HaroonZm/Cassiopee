from functools import reduce
import operator

print(reduce(operator.mul, map(int, input().split())))