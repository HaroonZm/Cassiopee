import functools
import operator

print(functools.reduce(lambda a, b: a + ' ' + b, input().split(',')))