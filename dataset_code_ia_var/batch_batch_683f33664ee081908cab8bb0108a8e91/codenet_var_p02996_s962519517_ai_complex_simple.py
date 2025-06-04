from functools import reduce
from itertools import accumulate, chain
import operator
import sys

input = lambda: sys.stdin.readline()

n = int(input())
l = list(map(lambda _: list(map(int, input().split())), range(n)))
l = sorted(l, key=operator.itemgetter(1))

def verdict(tasks):
    s = list(accumulate(map(operator.itemgetter(0), tasks)))
    checks = map(lambda pair: pair[0] <= pair[1], zip(s, map(operator.itemgetter(1), tasks)))
    try:
        reduce(lambda _, x: x if x else (_ for _ in ()).throw(SystemExit(print('No'))), checks)
        print('Yes')
    except SystemExit:
        pass

verdict(l)