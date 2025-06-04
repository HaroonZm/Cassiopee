from functools import reduce
from operator import add

bs = lambda v: reduce(
    lambda acc, i: acc + reduce(
        lambda c, j: c + ((lambda x, y: v.__setitem__(j + (x > y), min(x, y)) or v.__setitem__(j + (x < y), max(x, y)) or int(x > y))(v[j], v[j + 1])),
        range(len(v) - i - 1), 0
    ),
    range(len(v)), 0
)

import sys
from itertools import islice, starmap, repeat
it = iter(sys.stdin.readline, '')
while True:
    n = int(next(it))
    if not n:
        break
    v = list(starmap(int, zip(islice(it, n), repeat(None))))
    print(bs(v))