from functools import reduce
from itertools import islice, count

n,m=map(int,input().split())
p = list(islice((list(map(int, input().split())) for _ in count()), m))
p = sorted(p, key=lambda x: (x[0], x[1]))[1:]
def f(acc, i):
    return acc + (i[1] - n) * (i[0] < n)
ans = reduce(lambda acc, x: acc if x[0]>=n else f(acc,x), p, 0)
print(ans)