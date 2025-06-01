from functools import reduce
from operator import add
import sys

n = int(next(sys.stdin))

prices = list(map(lambda x: int(x.strip()), (next(sys.stdin) for _ in range(n))))

total = reduce(add, prices, 0)

ans = list(map(lambda x: x//1, [total / n]))[0]

print(ans)