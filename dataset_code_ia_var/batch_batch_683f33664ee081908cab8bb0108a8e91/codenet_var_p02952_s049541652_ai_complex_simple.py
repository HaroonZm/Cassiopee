from functools import reduce
from operator import add

N = int(input())

count = reduce(
    add,
    map(lambda x: 1 if len(str(x)) & 1 else 0, range(1, N + 1))
)

print(count)