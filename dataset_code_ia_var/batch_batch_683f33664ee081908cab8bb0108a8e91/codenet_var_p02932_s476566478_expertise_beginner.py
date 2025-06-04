import sys

def main():
    import sys

    # Lecture de l'entrée
    N, M, L, R = map(int, sys.stdin.readline().split())

    MOD = 10**9 + 7

    # Préparation des factorielles et inverses
    X = 1000
    fact = [1] * (X * X)
    for i in range(1, X * X):
        fact[i] = fact[i - 1] * i % MOD

    # Calcul des inverses de factorielles via Fermat (car MOD est premier)
    fact_inv = [1] * (X * X)
    fact_inv[X * X - 1] = pow(fact[X * X - 1], MOD - 2, MOD)
    for i in range(X * X - 2, -1, -1):
        fact_inv[i] = fact_inv[i + 1] * (i + 1) % MOD

    # Calcul des combinaisons alternées
    U = N - M
    comb = []
    for k in range(U + 1):
        val = fact[U] * fact_inv[k] % MOD * fact_inv[U - k] % MOD
        if k % 2 == 1:
            val = -val
        comb.append(val % MOD)

    # Calcul de P
    P = [0] * (R + 1)
    for idx, x in enumerate(comb):
        i = idx + M
        for j in range(0, R+1, i):
            P[j] = (P[j] + x) % MOD

    # Correction de P
    for i in range(M, R + 1):
        P[i] = (P[i] - P[i - M]) % MOD

    # Calcul de Q
    Q = []
    for i in range(R + 1):
        val = fact[N + i] * fact_inv[i] % MOD * fact_inv[N] % MOD
        Q.append(val)

    # Fonction f
    def f(RR):
        total = fact[RR + N] * fact_inv[RR] % MOD * fact_inv[N] % MOD
        x = 0
        for i in range(RR + 1):
            x = (x + Q[RR - i] * P[i]) % MOD
        coef = fact[N] * fact_inv[M] % MOD * fact_inv[N - M] % MOD
        return (total - x * coef) % MOD

    answer = (f(R) - f(L - 1)) % MOD
    print(answer)

if __name__ == "__main__":
    main()