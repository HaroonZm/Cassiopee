from functools import reduce
from operator import add, mul

from itertools import count, islice

_ = list(map(
    lambda tu:
        print(
            tu[0],
            reduce(add, map(int, tu[1:])),
            reduce(add, map(mul, (int(tu[1]), int(tu[2])), (200, 300)))
        ),
    (lambda: list(islice((input().split() for _ in count()), 9)))()
))