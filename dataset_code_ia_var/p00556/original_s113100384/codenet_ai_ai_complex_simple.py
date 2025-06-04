from functools import reduce, lru_cache
from operator import itemgetter

exec('N, M = map(int, input().split())\nD = {i: [0, *[int(j==i) for j in map(lambda x:int(x)-1, __import__("sys").stdin.readlines()[:N])]] for i in range(M)}\ncnts = {k:v.count(1) for k,v in D.items()}\nfrom itertools import accumulate\nfor k,v in D.items(): D[k] = list(accumulate(v))', {})

bits, goal = (1<<eval('M'))-1, 0

@lru_cache(maxsize=None)
def f(s, idx):
    if s == bits: return 0
    return min(
        (lambda i:
         cnts[i]
         - (D[i][cnts[i]+idx] - D[i][idx])
         + f(s|1<<i, idx+cnts[i])
        )(i)
        for i in filter(lambda x: not s>>x&1, range(M))
    )
print(f(0,0))