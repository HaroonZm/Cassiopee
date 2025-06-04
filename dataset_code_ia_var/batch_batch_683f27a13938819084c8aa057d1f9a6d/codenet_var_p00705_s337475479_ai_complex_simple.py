from functools import reduce
from operator import add, itemgetter

try:
    exec('input=raw_input')
except NameError:
    pass

while True:
    n, q = tuple(map(int, input().split()))
    if not any((n, q)):
        break
    counts = [0]*101
    maxd = [0]
    list(map(lambda _: list(map(lambda d: (counts.__setitem__(d, counts[d]+1), maxd.__setitem__(0, max(counts[d], maxd[0]))), map(int, input().split()[1:]))), range(n)))
    print(next((i for i,v in enumerate(counts) if v==maxd[0]), None) if q <= maxd[0] else 0)