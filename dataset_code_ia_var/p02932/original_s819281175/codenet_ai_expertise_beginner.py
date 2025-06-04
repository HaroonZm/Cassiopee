import sys

# Lecture de l'entrée
N, M, L, R = map(int, input().split())

MOD = 10 ** 9 + 7

# Pré-calcul des factorielles et des inverses
taille = 6 * 10 ** 5 + 101
fact = [1] * taille
for i in range(1, taille):
    fact[i] = fact[i-1] * i % MOD

fact_inv = [1] * taille
fact_inv[-1] = pow(fact[-1], MOD-2, MOD)
for i in range(taille-2, -1, -1):
    fact_inv[i] = fact_inv[i+1] * (i+1) % MOD

# Calcul des combinaisons, signe alterné sur les termes impairs
U = N - M
comb = []
sign = 1
for k in range(U+1):
    val = fact[U] * fact_inv[k] % MOD * fact_inv[U-k] % MOD
    if k % 2 == 1:
        val = -val
    comb.append(val % MOD)

# Construction du tableau P avec opérations de type convolution
P = [0] * (R+1)
for i, x in enumerate(comb):
    div = i + M
    for j in range(0, R+1, div):
        P[j] = (P[j] + x) % MOD

for i in range(M, R+1):
    P[i] = (P[i] - P[i-M]) % MOD

# Calcul du tableau Q
Q = []
for i in range(R+1):
    a = fact[N+i] * fact_inv[i] % MOD * fact_inv[N] % MOD
    Q.append(a)

def f(r):
    total = fact[r+N] * fact_inv[r] % MOD * fact_inv[N] % MOD
    x = 0
    for i in range(r+1):
        x = (x + Q[r-i] * P[i]) % MOD
    coef = fact[N] * fact_inv[M] % MOD * fact_inv[N-M] % MOD
    return (total - x * coef) % MOD

answer = (f(R) - f(L-1)) % MOD
print(answer)