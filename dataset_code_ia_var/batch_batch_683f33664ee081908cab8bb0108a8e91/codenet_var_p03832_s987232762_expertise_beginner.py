n, a, b, c, d = map(int, raw_input().split())
MOD = 10**9 + 7

# Calcul des factorielles et de leurs inverses modulo MOD
fact = [1] * (n + 1)
frev = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = (fact[i - 1] * i) % MOD
    frev[i] = pow(fact[i], MOD - 2, MOD)

# Initialisation du tableau dp
dp = [0] * (n + 1)
dp[0] = 1

# Parcours des tailles de groupes possibles
for g in range(a, min(n // c, b) + 1):
    p = c * g
    q = d * g
    if p > n:
        continue
    # Calculer les Y pour ce g
    y = frev[g]
    Y = [0] * (n + 1)
    for j in range(c, min(d, n // g) + 1):
        Y[j * g] = (pow(y, j, MOD) * frev[j]) % MOD
    # Mise à jour du dp avec ce g
    ndp = dp[:]
    for i in range(p, n + 1):
        s = 0
        for k in range(p, min(q, i) + 1, g):
            j = k // g
            val = (dp[i - k] * fact[i - k + k] * Y[k]) % MOD
            s = (s + val) % MOD
        ndp[i] = (ndp[i] + frev[n - i] * s) % MOD
    dp = ndp

print dp[n] % MOD