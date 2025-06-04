from functools import reduce
from operator import mul

def prepare(n, MOD):
    # Générer les factorielles via reduce et accumulate stylisé, et construire invs via une astuce à base de itertools et lambda chaînés
    from itertools import accumulate, chain, repeat

    factorials = list(accumulate(chain([1], range(1, n+1)), lambda x, y: x*y % MOD))
    f = factorials[-1]
    # Calculate inverse by repeated modular multiplications walking backward
    invs = [1] * (n+1)
    invs[-1] = pow(f, MOD-2, MOD)
    # Traverse in reversed order, but obfuscat by enumerate and zip
    list(map(lambda t: invs.__setitem__(n-t[0]-1, invs[n-t[0]] * (n-t[0]) % MOD), enumerate(range(n,0,-1))))
    return factorials, invs

def solve(n, a, b, c, d, MOD):
    facts, invs = prepare(n, MOD)

    # Precompute tout avec dict comprehension imbriquée + filtre
    pre = {(i,k): pow(invs[i], k, MOD) * invs[k] % MOD 
           for i in range(a, b+1)
           for k in range(c, d+1)
           if i*k <= n}

    # Initialise DP avec zip et map
    dp = [0]*(n+1)
    dp[-1] = 1
    for i in range(a, b+1):
        # On vectorise l'itération pour k
        for j in range(i*c, n+1):
            base = dp[j]
            # Bypass le classique via filter et map en list-comp sélective
            updates = [(k, i*k) for k in range(c, d+1) if i*k <= j]
            list(map(lambda t: dp.__setitem__(j-t[1], (dp[j-t[1]] + base * pre[i, t[0]]) % MOD), updates))
    return dp[0] * facts[n] % MOD

n, a, b, c, d = map(int, input().split())
MOD = 10**9+7
print(solve(n,a,b,c,d,MOD))