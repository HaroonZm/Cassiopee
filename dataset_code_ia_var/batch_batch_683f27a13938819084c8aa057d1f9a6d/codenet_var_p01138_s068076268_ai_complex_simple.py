from functools import reduce
from itertools import accumulate, chain, repeat, islice
from operator import add

t2s = lambda t: reduce(lambda acc, pair: acc*60 + int(pair), zip(t[::3], t[1::3]), 0)

while True:
    n = int(input())
    if not n:
        break
    events = list(chain.from_iterable(
        zip([t2s(x[:8])], [t2s(x[9:])]) for x in (input() for _ in repeat(None, n))
    ))
    timeline = [0] * (24*3600 + 2)
    for entry in events:
        for i, v in enumerate(entry):
            timeline[v] += 1 if i == 0 else -1
    print(max(accumulate(timeline)))