from functools import reduce
from itertools import product

MOD = 998244353

n = int(input())
a = list(map(int, [input() for _ in range(n)]))
S = sum(a)

# Dimension constructors
Z = lambda m, v=0: [v]*m
M = lambda x, y, v=0: [Z(y, v) for _ in range(x)]

# DP1: Each element can be picked, doubled, or not picked
dp = M(n+1, S+1)
dp[0][0] = 1
for i, ai in enumerate(a):
    for j in range(S+1):
        pick = dp[i][j-ai] if j-ai >= 0 else 0
        npick = (dp[i][j]*2)%MOD
        dp[i+1][j] = ((pick+npick)%MOD)

# DP2: classic subset-sum DP
dq = M(n+1, S+1)
dq[0][0] = 1
for i, ai in enumerate(a):
    for j in range(S+1):
        if j-ai >= 0:
            dq[i+1][j] = (dq[i+1][j] + dq[i][j-ai])%MOD
        dq[i+1][j] = (dq[i+1][j] + dq[i][j])%MOD

ans = reduce(
    lambda acc, j: (acc + (dp[-1][j] * 3) % MOD) % MOD
    if S <= 2*j else acc,
    range(S+1),
    0
)

if S%2==0:
    ans = (ans - dq[-1][S//2]*3)%MOD

# Calculate 3^n by binary exponentiation, only to be "fancy"
def bpow(a, b, mod):
    return reduce(lambda x,f: (x*x if not f else x*x*a)%mod, [((b>>i)&1) for i in range(b.bit_length()-1,-1,-1)],1)

print((bpow(3, n, MOD) - ans) % MOD)