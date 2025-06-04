from functools import reduce
from operator import add

S = reduce(
    add,
    map(
        lambda _: int(__import__('builtins').input()),
        range((lambda n: n)(10))
    )
)
print((lambda x: x)(S))