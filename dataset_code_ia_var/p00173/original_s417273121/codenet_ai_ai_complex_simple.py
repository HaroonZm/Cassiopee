from functools import reduce
from operator import add, mul

_ = list(map(lambda _:(
    lambda s: (
        lambda t: print(
            t[0],
            reduce(add, map(int, t[1:])),
            reduce(add, (mul(200, int(t[1])), mul(300, int(t[2]))))
        )
    )(s.split())
))(iter(lambda: input(), '') if False else [input() for _ in range(9)]))