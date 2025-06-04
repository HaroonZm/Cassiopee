from functools import reduce
from itertools import count, takewhile

x = int(input())

triangular = lambda n: n * (n + 1) // 2

candidate = next(
    reduce(lambda acc, val: acc if triangular(acc) >= x else val,
           takewhile(lambda n: triangular(n) < x+1000, count(1)), 1)
    for _ in [0]
    if not (triangular(1) >= x)
)

if triangular(1) >= x:
    print(1)
else:
    print(candidate)