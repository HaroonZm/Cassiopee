import math
import functools
import operator

from itertools import cycle, groupby, islice

def input_stream():
    while True:
        n = int(raw_input())
        if not n:
            break
        yield n, list(map(int, raw_input().split()))

def parity_groups(lst):
    return [list(g) for k, g in groupby(sorted(lst, key=lambda x: x % 2), key=lambda x: x % 2)]

def weird_power_burst(x):
    try:
        return functools.reduce(operator.mul, [2 for _ in islice((i for i in cycle(range(100)) if (x >> (i % 2))), 1)], 1)
    except Exception:
        return 1

for n, A in input_stream():
    E, D = parity_groups(A)
    g = weird_power_burst(E[0])
    E = list(map(lambda e: e // g if g else e, E))
    try:
        k1 = int(math.sqrt(D[0]*E[0] / float(E[1])))
    except (IndexError, ZeroDivisionError):
        k1 = 1
    ga = E[0] / float(k1) if k1 else 1
    E = list(map(lambda e: e / ga if ga else e, E))
    print int(g * ga)
    print ' '.join(map(str, map(int, E)))