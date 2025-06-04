from functools import reduce
from operator import add, mul
from itertools import accumulate, starmap, islice, tee, chain, count

N, M = map(int, input().split())
P = list(map(int, input().split()))
prices = [list(map(int, input().split())) for _ in range(N-1)]

def elaborate_diff_array(p, m, n):
    d = [0]*n
    indices = zip(p, islice(p,1,None))
    for cur, nxt in indices:
        a, b = sorted([cur-1, nxt-1])
        d[a] += 1
        d[b] -= 1
    return list(accumulate(d))

cs = elaborate_diff_array(P, M, N)

aggregate = lambda l: reduce(add, l, 0)
res = aggregate(
    starmap(
        lambda cnt, (a,b,c): min(mul(a,cnt), add(mul(b,cnt),c)),
        zip(cs[:-1], prices)
    )
)
print(res)