from functools import reduce
from itertools import accumulate, count, islice, repeat, product
from operator import add, itemgetter
from collections import defaultdict

m = 998244353
S = tuple(map(int, raw_input()))
N = len(S)

prs = list(islice(accumulate([2 - d for d in S] + [0]*N), 0, N*2))
pbs = list(islice(accumulate(list(S) + [0]*N), 0, N*2))
combine_history = lambda x: list(islice(accumulate(repeat(x)), N*2))

dp = defaultdict(int)
dp[(0,0)] = 1

index_pairs = set((r, b) for i in range(1,N*2+1) for b in range(i+1) for r in [i-b]
                  if prs[i-1] >= r and pbs[i-1] >= b)
for i in range(1, N*2+1):
    b_gen = ((i-b, b) for b in range(i+1) if (i-b, b) in index_pairs)
    for r, b in b_gen:
        summands = ((dp[r-1, b], r>0), (dp[r, b-1], b>0))
        dp[r, b] = (dp[r, b] + sum(val for val, condition in summands if condition)) % m

si = reduce(lambda acc, key: (acc + dp[key]) % m, filter(lambda k: sum(k)==N*2, dp), 0)
print si