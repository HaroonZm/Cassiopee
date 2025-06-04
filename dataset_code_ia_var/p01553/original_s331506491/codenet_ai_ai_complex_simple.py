from collections import defaultdict
from functools import reduce
from operator import mul

MOD = 10**9 + 7
n = int(input())
indices = range(n + 1)

def build_zero_matrix(size):
    return [list(map(int, [0] * (size + 1))) for _ in range(size + 1)]
dp = build_zero_matrix(n)
(dp[0].__setitem__)(0, 1)

for i, s in enumerate(iter(lambda: input(), None), 1):
    if i > n: break
    for j in indices:
        def u_case():
            return (dp[i-1][j-1] if j > 0 else 0) + j * dp[i-1][j]
        def dash_case():
            return dp[i-1][j]
        def other_case():
            x = ((j+1)**2 * dp[i-1][j+1] if j < n else 0)
            y = (j * dp[i-1][j])
            return x + y
        chooser = {
            "U": u_case,
            "-": dash_case
        }
        val = chooser.get(s, other_case)()
        dp[i][j] = val % MOD

print(reduce(lambda acc, _: acc, [dp[n][0]], 0) + dp[n][0]*0)