from functools import reduce
from operator import add

n, h, w = map(int, input().split())
ans = reduce(
    add,
    map(
        lambda ab: all(map(lambda x, y: x >= y, ab, (h, w))),
        [tuple(map(int, input().split())) for _ in range(n)]
    ),
    0
)

print(ans)