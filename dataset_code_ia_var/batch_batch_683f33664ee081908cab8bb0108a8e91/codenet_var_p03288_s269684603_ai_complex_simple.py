from functools import reduce
from itertools import count, takewhile, chain

a = int(input())

labels = ("ABC", "ARC", "AGC")
bounds = (1200, 2800, float('inf'))

def branching(x, thresholds, actions):
    idx = next(reduce(lambda acc, val: acc if acc[0] else (x < val[1], val[0]), enumerate(thresholds), (True, 0)))[1]
    return actions[idx]

print(branching(a, bounds, labels))