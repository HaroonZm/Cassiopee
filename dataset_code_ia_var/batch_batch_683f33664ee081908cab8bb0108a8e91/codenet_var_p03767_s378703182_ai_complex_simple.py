from functools import reduce
from operator import itemgetter

N = int(input())
a = list(map(int, input().split()))

sorted_a = sorted(a, key=lambda x: -x)
indices = map(lambda x: 2 * x + 1, range(N))
elements = list(map(sorted_a.__getitem__, indices))
ans = reduce(lambda acc, val: acc + val, elements, 0)
print(ans)