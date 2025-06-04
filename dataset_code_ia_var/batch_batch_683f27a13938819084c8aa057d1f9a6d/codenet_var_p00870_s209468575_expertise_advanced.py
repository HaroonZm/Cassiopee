from functools import reduce
import sys

readline = sys.stdin.readline
write = sys.stdout.write

def solve():
    N, M = map(int, readline().split())
    if not (N or M):
        return False

    ca = ord('a')
    E = [list(map(lambda c: ord(c) - ca, readline().strip())) for _ in range(N)]
    F = ''.join((readline().strip() for _ in range(M)))
    L = sum(map(len, E))

    MOD, BASE = 10**9 + 9, 37
    ALL = (1 << N) - 1
    bALL = (1 << (1 << N)) - 1

    # pré-calcul des puissances
    pw = [1] * (L + 2)
    for i in range(1, L + 2):
        pw[i] = pw[i - 1] * BASE % MOD

    V = [reduce(lambda v, c: (v * BASE + c) % MOD, e, 0) for e in E]
    K = [len(e) for e in E]
    P = [pw[k] for k in K]

    # S[j] : bitmask où tous les sous-ensembles contenant j ont leur bit retourné à 0
    S = [
        bALL ^ reduce(lambda agg, s: agg | (1 << s), (s for s in range(ALL + 1) if s & (1 << i)), 0)
        for i in range(N)
    ]

    A = len(F)
    dp = [1] * (A + 1)
    H = [0] * (A + 2)
    # calcul H[i] : hash du préfixe F[:i]
    for i, ch in enumerate(F, 1):
        H[i] = (H[i - 1] * BASE + ord(ch) - ca) % MOD

    ans = 0
    for i in range(1, A + 1):
        r = 1
        for j, (v, k, p, s_mask) in enumerate(zip(V, K, P, S)):
            if i >= k:
                cur_hash = (H[i] - H[i - k] * p) % MOD
                if cur_hash == v:
                    r |= (dp[i - k] & s_mask) << (1 << j)
        dp[i] = r
        if r & (1 << ALL):
            ans += 1

    write(f"{ans}\n")
    return True

while solve():
    pass