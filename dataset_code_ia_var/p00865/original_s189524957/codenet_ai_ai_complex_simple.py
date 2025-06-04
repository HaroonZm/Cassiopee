from functools import reduce
from itertools import islice, repeat, accumulate, chain, product, starmap
from operator import add

def infinite_input():
    while True:
        yield tuple(map(int, raw_input().split()))
        
def build_dp(n, m):
    size = m*n+1
    base = list(chain([0], repeat(0, size-1)))
    base = [list(base) for _ in range(n)]
    base[0][1:m+1] = [1]*m
    def cell(i, j):
        return sum(base[i-1][max(j-m,0):j])
    for i, j in product(range(1, n), range(1, size)):
        base[i][j] = cell(i, j)
    return base

result_format = lambda x: "%.10f"%x

for n, m, k in infinite_input():
    if not n: break
    dp = build_dp(n, m)
    s = reduce(add, dp[n-1])
    portion = list(starmap(lambda idx, val: val*1.0/s*max(1, idx-k), enumerate(dp[n-1])))
    ans = reduce(add, portion[1:], 0)
    print result_format(ans)