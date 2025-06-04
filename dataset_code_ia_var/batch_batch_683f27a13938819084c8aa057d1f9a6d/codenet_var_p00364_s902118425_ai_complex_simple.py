from functools import reduce
from operator import itemgetter

n, t = map(int, input().split())
heights = list(map(lambda _: tuple(map(int, input().split())), range(n)))
calc = lambda p: p[1] / p[0] * t
min_height = reduce(lambda a, b: max(a, b), map(calc, heights), 0)
print(min_height)