from functools import reduce
from itertools import groupby, count
import sys

def f(x):
    def gens(a):
        while True:
            yield a
            a = list(map(lambda e: reduce(lambda acc, v: acc + (v==e), a, 0), a))
    g = gens(list(x))
    idx = next(i for i, (p, n) in enumerate(zip(g, g)) if list(p) == list(n))
    return idx, " ".join(map(str, list(gens(list(x)))[idx]))

while True:
    if (lambda z: z==0)(int(input())): break
    c, s = f(map(int, __import__('builtins').input().split()))
    print(c);print(s)