from functools import reduce
from operator import add

H, A, B = map(int, input().split())

ans = reduce(
    add,
    map(lambda i: int(not (H % i)), range(A, B + 1))
)

print(ans)