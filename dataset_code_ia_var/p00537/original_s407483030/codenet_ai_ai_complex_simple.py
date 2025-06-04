from functools import reduce
from operator import add, sub, mul
from itertools import accumulate, islice, starmap

n, m = map(int, input().split())
u = [0]*n
a = list(map(int, input().split()))
pairs = list(zip(a, a[1:]))
def upd(lst, x, y):
    return list(map(add, lst, [1 if i==min(x,y)-1 else -1 if i==max(x,y)-1 else 0 for i in range(n)]))
u = reduce(lambda acc, pair: upd(acc, pair[0], pair[1]), pairs, u)
u = list(accumulate(u))
inputs = [tuple(map(int, input().split())) for _ in range(n-1)]
cost = lambda d,b,c,x: min(d*x, b*x+c)
ans = sum(starmap(lambda dbc, x: cost(*dbc, x), zip(inputs, islice(u,1,None))))
print(ans)