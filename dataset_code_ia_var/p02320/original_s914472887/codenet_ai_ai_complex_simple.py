from functools import reduce
from collections import Counter, defaultdict
from itertools import islice, repeat, chain
N, W, *L = map(int, open(0).read().split())
T = tuple(zip(*[iter(L)]*3))
d = Counter(chain.from_iterable(repeat(((v,w),),m) for v,w,m in T))
M = defaultdict(list)
for (v,w), m in d.items():
    c, a = m, 1
    r = []
    while c:
        k=min(a, c)
        r.append((v*k, w*k))
        c -= k
        a <<= 1
    M[(v,w)].extend(r)
dp = [0]*(W+1)
for S in M.values():
    for val, wt in S:
        dp = [max(dp[j], dp[j-wt]+val) if j>=wt else dp[j] for j in range(W+1)]
print(reduce(lambda x,y:x if x>y else y, dp))