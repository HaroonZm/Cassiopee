from functools import reduce
from operator import mul
from itertools import takewhile, count

X, Y = map(int, input().split())
exp_iter = takewhile(lambda p: X * (2 ** p) <= Y, count())
ans = reduce(lambda acc, _: acc + 1, exp_iter, 0)
print(ans)