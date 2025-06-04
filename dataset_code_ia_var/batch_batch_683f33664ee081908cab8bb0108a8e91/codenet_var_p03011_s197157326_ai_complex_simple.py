import functools
import operator

a = list(map(int, input().split()))
print(functools.reduce(operator.add, sorted(a)[:2]))