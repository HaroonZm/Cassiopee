import sys
from functools import lru_cache
from operator import mul
from itertools import accumulate
from math import comb

read = sys.stdin.read
write = sys.stdout.write

def solve():
    MOD = 10**9 + 7

    N, *A = map(int, read().split())

    # Use optimal precomputations with functions and comprehensions
    L = 10**5
    def precompute_fact_invfact(limit):
        fact = [1]*(limit+1)
        for i in range(1, limit+1):
            fact[i] = fact[i-1] * i % MOD
        invfact = [1]*(limit+1)
        invfact[-1] = pow(fact[-1], MOD-2, MOD)
        for i in range(limit, 0, -1):
            invfact[i-1] = invfact[i] * i % MOD
        return fact, invfact

    fact, invfact = precompute_fact_invfact(L)

    L0 = 1000
    pw10 = [1] * (L0+1)
    for i in range(1, L0+1):
        pw10[i] = pw10[i-1] * 10 % MOD

    C = [0]*5
    V = [0]*5
    z = False

    for a in A:
        if a == 0:
            z = True
        l = len(str(a))
        idx = l-1
        C[idx] += 1
        V[idx] += a

    S = [0]*(N+1)
    r = 0
    for i in range(N+1):
        r += invfact[i]
        S[i] = fact[i] * r % MOD

    # Efficient factorial ratios and combinations with lru_cache
    @lru_cache(None)
    def fact_ratio(a, b):
        return fact[a] * invfact[b] % MOD

    @lru_cache(None)
    def nCk(n, k):
        if k < 0 or k > n: return 0
        return fact[n] * invfact[k] % MOD * invfact[n-k] % MOD

    # Precompute falling factorials and combs as lists of lists for speed
    F = [[fact_ratio(i, i-j) for j in range(i+1)] for i in range(N+1)]
    CM = [[nCk(i, j) for j in range(i+1)] for i in range(N+1)]

    @lru_cache(None)
    def _S(idx):
        return S[idx]

    def calc(C):
        c1, c2, c3, c4, c5 = C
        l0 = sum(C)
        res = 0
        F1, F2, F3, F4, F5 = F[c1], F[c2], F[c3], F[c4], F[c5]
        G1 = F[c1-1] if c1 > 0 else None
        for d5 in range(c5+1):
            v5 = F5[d5]
            for d1 in range(c1+1):
                v1 = v5 * CM[d1+d5][d1] % MOD
                if z and d1 < c1 and G1:
                    p1 = F1[d1]
                    p2 = G1[d1]
                else:
                    p1 = F1[d1]
                    p2 = 0
                for d2 in range(c2+1):
                    v2 = v1 * F2[d2] * CM[d2+d1+d5][d2] % MOD
                    for d3 in range(c3+1):
                        e = d1 + d2*2 + d3*3 + d5*5
                        f = d1 + d2 + d3 + d5
                        v3 = v2 * F3[d3] * CM[f][d3] % MOD
                        for d4 in range(c4+1):
                            l = f + d4
                            v4 = v3 * F4[d4] * CM[l][d4] % MOD
                            add = ((p1 * S[l0-l] - p2 * S[l0-1-l]) % MOD) * pw10[e + d4*4] % MOD
                            res = (res + add * v4) % MOD
        return res % MOD

    c1, c2, c3, c4, c5 = C
    ans = 0
    for i, delta in enumerate([(1,0,0,0,0), (0,1,0,0,0), (0,0,1,0,0), (0,0,0,1,0), (0,0,0,0,1)]):
        C_adj = [c1-delta[0], c2-delta[1], c3-delta[2], c4-delta[3], c5-delta[4]]
        if C_adj[i] < 0: continue
        ans = (ans + calc(tuple(C_adj)) * V[i]) % MOD

    write(f"{ans}\n")
solve()