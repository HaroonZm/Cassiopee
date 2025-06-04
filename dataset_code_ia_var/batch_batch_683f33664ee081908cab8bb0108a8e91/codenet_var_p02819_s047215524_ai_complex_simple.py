from functools import reduce
from math import isqrt
from itertools import count

x = int(input())
next(
    map(
        lambda n: print(n),
        filter(
            lambda n: not any(map(lambda d: n % d == 0, range(2, isqrt(n) + 1))),
            count(x)
        )
    ),
    None
)