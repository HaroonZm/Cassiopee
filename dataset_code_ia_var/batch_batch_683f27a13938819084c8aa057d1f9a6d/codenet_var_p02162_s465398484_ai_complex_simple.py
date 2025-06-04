from operator import itemgetter
from functools import reduce

T = list(map(int, input().split()))
s = [("Alice", lambda x: x[0]<x[1]), ("Bob", lambda x: x[0]>x[1]), ("Draw", lambda x: x[0]==x[1])]
f = lambda t: t[2:]==[-1, -1] or -1 in t[2:]
g = lambda t: [t[0], t[1]] if f(t) else [t[2], t[3]]
print(next(filter(lambda name: next(filter(lambda cond: cond(g(T)), map(itemgetter(1), s))), map(itemgetter(0), s))))