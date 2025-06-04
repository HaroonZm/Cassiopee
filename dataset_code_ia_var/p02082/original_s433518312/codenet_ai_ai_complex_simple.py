from functools import reduce
import operator
import sys

extract = lambda inp: list(map(int, inp().split()))
flatten = lambda l: reduce(operator.add, [int(x) for x in l], 0)
ignore = sys.stdin.readline

def deep_xor(*args):
    return reduce(operator.xor, args)

s, t = extract(input())
ignore()
y = flatten([input()])
print(deep_xor(s, t, y))