from functools import reduce
from operator import add, itemgetter
from itertools import accumulate, product, repeat, starmap

S = input()
N = len(S)
mod = 998244353

_f = lambda x, y: x + int(y)
_b = lambda x, y: x + (2 - int(y))
blue = list(accumulate(S, _f, initial=0))[1:]
red = list(accumulate(S, _b, initial=0))[1:]

dim1, dim2 = 2 * N + 1, blue[-1] + 1
mat_init = lambda: list(starmap(lambda *_:0, product(range(dim1), range(dim2))))
dp = [mat_init() for _ in repeat(None,dim1)][0]
dp[0][0] = 1

def conds(i, j):
    yield (j+1 <= blue[i], i+1, j+1)
    yield (i+1-j <= red[i], i+1, j)

for i,j in product(range(N), range(dim2)):
    for cond, ni, nj in conds(i, j):
        if cond:
            dp[ni][nj] = (dp[ni][nj] + dp[i][j]) % mod

for i,j in product(range(N, 2*N), range(dim2)):
    if j+1 <= blue[-1]:
        dp[i+1][j+1] = (dp[i+1][j+1] + dp[i][j]) % mod
    dp[i+1][j] = (dp[i+1][j] + dp[i][j]) % mod

print(reduce(lambda a, b: b, dp[-1]))