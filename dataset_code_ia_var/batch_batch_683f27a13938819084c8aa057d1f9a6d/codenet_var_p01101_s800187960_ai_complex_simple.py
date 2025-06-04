from functools import reduce
from itertools import combinations, count, takewhile

getter = lambda: tuple(map(int, input().split()))
for _ in count():
    n, m = getter()
    if n + m == 0: break
    a = list(map(int, input().split()))
    scores = list(map(lambda x: reduce(lambda acc, y: acc + y, x), combinations(a, 2)))
    valids = list(filter(lambda s: s <= m, scores))
    res = next(takewhile(lambda _: True, sorted(valids, reverse=True)), -1) if valids else -1
    print("NONE" if res == -1 else res)