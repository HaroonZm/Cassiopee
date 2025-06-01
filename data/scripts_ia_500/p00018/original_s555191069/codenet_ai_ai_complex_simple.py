from functools import reduce
import operator
from sys import stdin

a = list(map(int, reduce(operator.add, [stdin.readline().split()])))
b = [(lambda x: x)(x) for x in a]
b.sort(key=lambda x: -x)
for i, v in enumerate(reduce(lambda x, y: x + [y], b, [])):
    print(v,),