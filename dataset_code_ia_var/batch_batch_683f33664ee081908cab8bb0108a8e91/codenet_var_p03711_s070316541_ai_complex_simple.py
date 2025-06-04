from itertools import chain, groupby
from operator import itemgetter
import sys

groups = dict(chain.from_iterable(
    ((v, k) for v in vs)
    for k, vs in zip("ABC", ([1, 3, 5, 7, 8, 10, 12], [4, 6, 9, 11], [2]))
))

x, y = map(int, sys.stdin.readline().split())

gx, gy = map(groups.get, (x, y))

print(("No", "Yes")[(lambda a, b: a == b)(gx, gy)])