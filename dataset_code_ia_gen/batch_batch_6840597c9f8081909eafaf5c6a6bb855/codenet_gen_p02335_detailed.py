MOD = 10**9 + 7

# On nous demande de placer n boules indistinguables dans k boîtes distinguables,
# avec au plus une boule par boîte.
# Chaque boule doit être mise dans une boîte (aucune boule ne reste dehors).
# Comme les boules sont indistinguables, le nombre de façons revient à choisir
# simplement dans quelles boîtes vont être placées les boules.
# En effet, placer n boules identiques dans k boîtes avec au plus une boule par boîte revient à
# choisir un sous-ensemble de n boîtes parmi les k boîtes.
# Le nombre de façons est donc C(k, n) si n <= k, sinon 0.

# Pour calculer C(k, n) modulo 10^9+7, on utilise la pré-calculation de factorielles
# et inverse modulaire par Fermat.

MAX = 1000  # d'après la contrainte maximale de n et k

fact = [1] * (MAX + 1)
inv_fact = [1] * (MAX + 1)

def modinv(x):
    # Calcul de l'inverse modulo MOD par exponentiation rapide
    return pow(x, MOD-2, MOD)

def prepare_factorials():
    for i in range(2, MAX + 1):
        fact[i] = fact[i-1] * i % MOD
    inv_fact[MAX] = modinv(fact[MAX])
    for i in range(MAX-1, 0, -1):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

def main():
    n, k = map(int, input().split())
    # Si on ne peut pas mettre toutes les boules (n>k), c'est 0
    if n > k:
        print(0)
        return
    prepare_factorials()
    # Nombre de façons = C(k, n) mod
    print(comb(k, n))

if __name__ == "__main__":
    main()