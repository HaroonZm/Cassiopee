from functools import reduce
from operator import itemgetter
from itertools import islice, chain, starmap

while (lambda f: (lambda *a, **k: f(f, *a, **k)))(lambda self: (
    (n := int(input())) and (
        lambda tt: (
            lambda aa: print(
                *map(itemgetter(0),
                    islice(chain(aa, reversed(aa)), 0, 2) + [aa[-2][0]]
                ), sep='\n')
            )
        )(
            sorted(
                tt.items(),
                key=itemgetter(1)
            )
        )
    )(
        reduce(
            lambda d, l: d | {l[0]: sum(starmap(lambda x, y: 60*x + y, zip(l[1::2], l[2::2])))},
            (list(map(int, input().split()))
                for _ in range(n)),
            {}
        )
    )
) or None )():
    pass