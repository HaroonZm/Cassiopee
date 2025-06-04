from functools import lru_cache, reduce
from operator import mul, add

MOD = 10 ** 9 + 7
n, a, b = map(int, input().split())

(a, b) if a <= b else (b, a)
a, b = min(a, b), max(a, b)

@lru_cache(maxsize=None)
def weird_ones(l):
    if l <= a + 1: return 0
    dp = {(1,1):1}
    for i in range(1, l):
        next_dp = {}
        for (j, c), val in dp.items():
            if j + 1 <= l:
                next_dp[(j+1,0)] = (next_dp.get((j+1,0),0)+val*(c==0))%MOD
                next_dp[(j+1,1)] = (next_dp.get((j+1,1),0)+val)%MOD
            if j + a < l:
                next_dp[(j+a,0)] = (next_dp.get((j+a,0),0)+val*(c==1))%MOD
        dp = next_dp
    return (dp.get((l,1),0)-1) % MOD

ones_dp = [0] * b
list(map(lambda l: ones_dp.__setitem__(l, weird_ones(l)), range(a+2,b)))

@lru_cache(maxsize=None)
def odd_edge(l):
    if l <= a: return 0
    dp = {(a,0):1}
    for i in range(1, l):
        next_dp = {}
        for (j, c), val in dp.items():
            if j + 1 <= l:
                next_dp[(j+1,0)] = (next_dp.get((j+1,0),0)+val*(c==0))%MOD
                next_dp[(j+1,1)] = (next_dp.get((j+1,1),0)+val)%MOD
            if j + a < l:
                next_dp[(j+a,0)] = (next_dp.get((j+a,0),0)+val*(c==1))%MOD
        dp = next_dp
    return dp.get((l,1),0)%MOD

zero_edge_dp = [0]*b
list(map(lambda l: zero_edge_dp.__setitem__(l, odd_edge(l)), range(a+1,b)))

main_dp = [[0,0] for _ in range(n+1)]
main_dp[0] = [1,1]
for l in filter(lambda x: x >= a+1 and x < b, range(n+1)):
    main_dp[l][1] = zero_edge_dp[l] if l < len(zero_edge_dp) else 0

for i in range(n):
    for j in filter(lambda k: k<n+1, range(i+1,min(n+1,i+b))):
        main_dp[j][1] = (main_dp[j][1] + main_dp[i][0]) % MOD
    for j in filter(lambda k: k<n+1, range(i+1,min(n+1,i+a))):
        main_dp[j][0] = (main_dp[j][0] + main_dp[i][1]) % MOD
    for l in filter(lambda l: l>=a+2 and l<b, range(a+2,b)):
        if i+l<=n:
            main_dp[i+l][1] = (main_dp[i+l][1] + main_dp[i][0] * ones_dp[l]) % MOD

main_dp[n][0] = reduce(lambda result, l: (result + main_dp[n-l][0]*zero_edge_dp[l])%MOD,
                       filter(lambda l:l>=a+1 and l<b, range(a+1,b)),
                       main_dp[n][0])

print((pow(2,n,MOD) - sum(main_dp[n])) % MOD)