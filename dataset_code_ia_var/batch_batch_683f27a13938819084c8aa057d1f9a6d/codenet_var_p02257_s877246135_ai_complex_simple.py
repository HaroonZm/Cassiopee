from functools import reduce
from itertools import count, takewhile
from operator import mul
import sys

n = int(sys.stdin.readline())

def is_prime(x):
    return bool(
        x > 1 and
        reduce(mul, (
            x % d != 0
            for d in takewhile(lambda y:y*y<=x, count(2))
        ), True)
    )

print(
    sum(map(
        lambda _: is_prime(int(sys.stdin.readline())),
        range(n)
    ))
)