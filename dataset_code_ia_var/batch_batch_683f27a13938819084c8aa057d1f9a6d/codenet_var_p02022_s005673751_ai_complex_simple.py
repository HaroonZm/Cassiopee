from functools import reduce
from operator import mul

n, m = map(int, input().split())
sp = list(map(int, input().split()))
cl = list(map(int, input().split()))

sum_sp = reduce(lambda x, y: x + y, sp)
ans = reduce(lambda acc, val: acc + reduce(mul, [sum_sp, val]), cl, 0)

print(ans)