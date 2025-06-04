import sys
from functools import reduce
import operator

def read_input():
    return next(map(lambda s: list(map(int, s.split())), sys.stdin)).__iter__()

A, B = (lambda gen: (lambda x, y: (x, y))(*gen))(read_input())

f = lambda a, b: {True: "IMPOSSIBLE", False: reduce(lambda x, y: operator.floordiv(x, 2), [a + b])}[(a - b) & 1 == 1]
print(f(A, B))