from functools import partial, reduce
from itertools import count, islice, cycle, chain

g = lambda: (tuple(map(int, input().split())) for _ in count())
stop = lambda x: x == (0,0)
s = "#."
alt = lambda i, j: s[(i+j)%2]

printer = partial(print, end="")

for H, W in (t for t in g() if not stop(t)):
    grid = (
        chain.from_iterable(
            (alt(i, j) for j in range(W)) + ('\n',)
            for i in range(H)
        )
    )
    _ = list(map(printer, grid))
    print()