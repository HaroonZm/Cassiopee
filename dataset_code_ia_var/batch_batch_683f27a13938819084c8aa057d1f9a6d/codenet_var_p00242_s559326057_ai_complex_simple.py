from functools import reduce
from itertools import chain, islice, groupby
from operator import itemgetter, add

sentinel = object()
loop = iter(int, 1)
while True:
    n = next(loop)
    if n == 0:
        break

    stash = lambda: ({}, lambda d, k, v: d.setdefault(k, set()).add(v))
    sets, adder = stash()
    counts = {}

    def inc(d, k):
        d[k] = d.get(k, 0) + 1

    accumulate = lambda i: tuple(chain.from_iterable(map(str.split, (input() for _ in range(i)))))
    items = accumulate(n)
    void = [adder(sets, w[0], w) or inc(counts, w) for w in items]

    k = input()
    results = tuple(sorted(
        sets.get(k, set()),
        key=lambda x: (-counts.get(x, 0), x)
    ))

    print(*(results[:5] if results else ['NA']))