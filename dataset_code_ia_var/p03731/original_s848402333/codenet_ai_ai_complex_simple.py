from functools import reduce
from itertools import tee, islice, starmap
from operator import add

n, t = map(int, input().split())
a = list(map(int, input().split()))

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a1, a2 = tee(iterable)
    next(a2, None)
    return zip(a1, a2)

increments = list(starmap(lambda prev, curr: min(prev + t, curr) - prev, pairwise(a)))
aggregate = reduce(add, increments, 0)
print(aggregate + t)