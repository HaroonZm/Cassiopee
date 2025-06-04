from functools import reduce
from operator import add

(*_,), = (map(int, input().split()) for _ in range(1))
n, h, w = _

ab = [tuple(map(int, input().split())) for _ in range(n)]

ans = reduce(
    add,
    (
        (a >= h and b >= w)**1
        for a, b in ab
    ),
    0
)

print(ans)