import sys
read = sys.stdin.read
write = sys.stdout.write
def solve():
    MOD = 10**9 + 7
    N, *A = map(int, read().split())

    L = 10**5

    fact = [1]*(L+1)
    rfact = [1]*(L+1)
    r = 1
    for i in range(1, L+1):
        fact[i] = r = r * i % MOD
    rfact[L] = r = pow(fact[L], MOD-2, MOD)
    for i in range(L, 0, -1):
        rfact[i-1] = r = r * i % MOD

    L0 = 1000
    pw10 = [1]*(L0+1)
    r = 1
    for i in range(1, L0+1):
        pw10[i] = r = r * 10 % MOD

    C = [0]*5
    V = [0]*5
    z = 0
    for a in A:
        if a == 0:
            z = 1
        l = len(str(a))
        C[l-1] += 1
        V[l-1] += a

    S = [0]*(N+1)
    r = 0
    for i in range(N+1):
        r += rfact[i]
        S[i] = fact[i] * r % MOD

    F = [[0]*(i+1) for i in range(N+1)]
    for i in range(N+1):
        for j in range(i+1):
            F[i][j] = fact[i] * rfact[i-j] % MOD

    CM = [[0]*(i+1) for i in range(N+1)]
    for i in range(N+1):
        for j in range(i+1):
            CM[i][j] = fact[i] * rfact[i-j] * rfact[j] % MOD

    def calc(C):
        c1, c2, c3, c4, c5 = C
        l0 = sum(C)
        res = 0
        F1 = F[c1]; G1 = F[c1-1]
        F2 = F[c2]
        F3 = F[c3]
        F4 = F[c4]
        F5 = F[c5]
        r1 = range(c1+1)
        r2 = range(c2+1)
        r3 = range(c3+1)
        r4 = range(c4+1)
        for d5 in range(c5+1):
            v5 = F5[d5]
            for d1 in r1:
                v1 = v5 * CM[d1+d5][d1] % MOD
                if z and d1 < c1:
                    p1 = F1[d1]; p2 = G1[d1]
                else:
                    p1 = F1[d1]; p2 = 0
                for d2 in r2:
                    v2 = v1 * F2[d2] * CM[d2+d1+d5][d2] % MOD
                    for d3 in r3:
                        e = d1+d2*2+d3*3+d5*5
                        f = d1+d2+d3+d5
                        v3 = v2 * F3[d3] * CM[f][d3] % MOD
                        for d4 in r4:
                            l = f+d4
                            v4 = v3 * F4[d4] * CM[l][d4] % MOD
                            res += ((p1 * S[l0-l] - p2 * S[l0-1-l]) * pw10[e+d4*4] % MOD) * v4 % MOD
        return res % MOD
    c1, c2, c3, c4, c5 = C
    ans = 0
    ans += calc([c1-1, c2, c3, c4, c5]) * V[0]
    ans += calc([c1, c2-1, c3, c4, c5]) * V[1]
    ans += calc([c1, c2, c3-1, c4, c5]) * V[2]
    ans += calc([c1, c2, c3, c4-1, c5]) * V[3]
    ans += calc([c1, c2, c3, c4, c5-1]) * V[4]
    ans %= MOD
    write("%d\n" % ans)
solve()