import sys

# Lecture de la saisie utilisateur
N_M_L_R = input().split()
N = int(N_M_L_R[0])
M = int(N_M_L_R[1])
L = int(N_M_L_R[2])
R = int(N_M_L_R[3])

MOD = 10**9 + 7
X = 1000

# Calcul des factorielles (1D)
fact = [1] * (X * X)
for i in range(1, X * X):
    fact[i] = (fact[i-1] * i) % MOD

# Calcul des inverses de factorielles (1D)
fact_inv = [1] * (X * X)
fact_inv[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(X * X - 2, -1, -1):
    fact_inv[i] = (fact_inv[i+1] * (i+1)) % MOD

U = N - M

# Calcul des combinaisons avec alternance des signes
comb = []
for k in range(0, U+1):
    c = fact[U]
    c = (c * fact_inv[k]) % MOD
    c = (c * fact_inv[U - k]) % MOD
    if k % 2 == 1:
        c = (-c) % MOD
    comb.append(c)

# Calcul du tableau P
P = [0] * (R+1)
for idx, x in enumerate(comb):
    pos = idx + M
    j = 0
    while j <= R:
        P[j] = (P[j] + x) % MOD
        j += pos

# Correction du tableau P
for i in range(R, M-2, -1):
    if i - M >= 0:
        P[i] = (P[i] - P[i - M]) % MOD

# Calcul de Q
Q = []
for i in range(R+1):
    q = fact[N + i]
    q = (q * fact_inv[i]) % MOD
    q = (q * fact_inv[N]) % MOD
    Q.append(q)

def f(limit):
    if limit < 0:
        return 0
    total = fact[limit + N]
    total = (total * fact_inv[limit]) % MOD
    total = (total * fact_inv[N]) % MOD

    x = 0
    for t in range(limit+1):
        x = (x + (Q[t] * P[t]) % MOD) % MOD

    coef = (fact[N] * fact_inv[M]) % MOD
    coef = (coef * fact_inv[N - M]) % MOD

    resultat = (total - x * coef) % MOD
    return resultat

answer = (f(R) - f(L - 1)) % MOD
print(answer)