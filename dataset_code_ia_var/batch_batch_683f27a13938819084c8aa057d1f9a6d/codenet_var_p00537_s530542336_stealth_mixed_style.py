N, M = [int(x) for x in input().split()]
P = list(map(int, input().split()))
cs = [0 for _ in range(N)]
pricelist = []
for __ in range(N-1):
    entry = input().split()
    pricelist.append(tuple(map(int, entry)))
res = 0
i = 0
while i < M-1:
    x, y = P[i], P[i+1]
    mn = x-1 if x-1 < y-1 else y-1
    mx = x-1 if x-1 > y-1 else y-1
    cs[mn] = cs[mn] + 1
    cs[mx] = cs[mx] - 1
    i = i + 1
j = 1
while j < N:
    cs[j] += cs[j-1]
    j += 1
from functools import reduce
def f(acc, i):
    cnt = cs[i]
    pa,pb,pc = pricelist[i]
    return acc + (pa*cnt if pa*cnt < pb*cnt+pc else pb*cnt+pc)
res = reduce(f, range(N-1), 0)
print(res)