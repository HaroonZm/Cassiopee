from functools import reduce
from operator import add
import itertools

print(
    reduce(
        add,
        map(
            lambda x: int(x),
            list(itertools.islice((input() for _ in iter(int, 1)), 10))
        )
    )
)