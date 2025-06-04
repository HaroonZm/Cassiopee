from functools import reduce
from itertools import chain, repeat, starmap, product, combinations
from collections import defaultdict

sentinel = lambda: (lambda: (_ for _ in ()).throw(StopIteration))()

while True:
    try:
        n, m = starmap(int, zip(*[iter(input().split())]*2))
        n, m = next(n), next(m)
    except Exception:
        break
    if not n and not m:
        break
    gobble = map(lambda _: int(input(), 2), range(n))
    h = lambda l: reduce(lambda d, b: defaultdict(int, chain(d.items(), ((k ^ b, max(d.get(k ^ b, 0), v+1)) for k, v in d.items()))), l, defaultdict(int, {0: 0}))
    print(h(gobble)[0])