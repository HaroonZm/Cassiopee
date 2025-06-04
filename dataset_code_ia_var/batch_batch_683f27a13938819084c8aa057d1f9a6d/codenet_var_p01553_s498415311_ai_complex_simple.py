from functools import reduce
from itertools import chain, repeat, accumulate, starmap, product

n = int(input())
s = "".join(chain.from_iterable(map(lambda x: filter(lambda c: c != '-', x), [input() for _ in range(n)])))
L = len(s)
mod = 10**9+7

make_matrix = lambda x, y, v=0: list(map(lambda _: list(repeat(v, y)), repeat(None, x)))

dp = make_matrix(L+1, L+1)
reduce(lambda _, __: dp.__setitem__(_, list(map(int, repeat(0,L+1)))), range(L+1), None)
dp[0][0] = 1

for i, si in enumerate(s):
    if si == "D":
        update = lambda j: (
            dp[i+1].__setitem__(j, (dp[i+1][j] + dp[i][j]*j)%mod),
            dp[i+1].__setitem__(j-1, (dp[i+1][j-1] + dp[i][j]*pow(j,2,mod))%mod)
        )
        list(map(update, range(1, L+1)))
    else:
        update = lambda j: (
            dp[i+1].__setitem__(j+1, (dp[i+1][j+1] + dp[i][j]) % mod),
            dp[i+1].__setitem__(j,   (dp[i+1][j]   + dp[i][j]*j) % mod)
        )
        list(map(update, range(L)))
print(reduce(lambda a,b: b, accumulate(dp[L][0:1])))