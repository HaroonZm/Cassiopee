from functools import reduce
from operator import add

N = int(input())
a = list(map(int, input().split()))

ans = reduce(lambda acc, _: acc + 1, dict.fromkeys(a, 0), 0)

print(ans)