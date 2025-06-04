from itertools import islice, repeat, starmap
from functools import reduce

def get_input():
    while True:
        yield int(input())

def flatten(l):
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in l), [])

def aggregate_time(parts): # aggregate time tuple to total seconds
    group = lambda l: zip(*[iter(l)]*2)
    to_secs = lambda m, s: m*60+s
    return sum(starmap(to_secs, group(parts[1:]))), parts[0]

consume = lambda it, n: list(islice(it, n))

for _ in repeat(None):
    n = next(get_input())
    if not n:
        break
    lines = consume((list(map(int, input().split())) for _ in repeat(None)), n)
    agg = list(map(aggregate_time, lines))
    idx = sorted(agg)
    for i in (0,1,-2):
        print(idx[i][1])