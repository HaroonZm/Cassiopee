from functools import reduce
from itertools import accumulate, chain
from operator import add, mod
from bisect import bisect_right as br

_ = eval
[(lambda x: exec(x))('''while any(
    map(lambda nm: (lambda n, m:
        n > 0 and (lambda kl:
            (lambda pre, meta, foo:
                print(
                    reduce(lambda a, c:
                        max(a,
                            max(
                                [((c - meta[i]) % m) if i < len(meta) else 0
                                 for i in [br(meta, c)]] +
                                [c]
                            )
                        )
                    , pre, 0)
                )
            )(list(accumulate(kl, lambda a, b: (a + b) % m)), [0], kl)
        )(list(map(int, input().split())))
    ), [tuple(map(int, input().split()))], 1
)
)''')]