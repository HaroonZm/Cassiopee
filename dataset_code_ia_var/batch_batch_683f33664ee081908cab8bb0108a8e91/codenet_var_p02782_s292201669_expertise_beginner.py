MOD = 10**9 + 7
r1, c1, r2, c2 = map(int, input().split())
n = (2 * 10 ** 6) + 2

# Pré-calcul des factorielles modulo MOD
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = (fact[i-1] * i) % MOD

# Calcul du facteur inverse modulaire avec la répétition rapide
def modinv(a):
    result = 1
    b = MOD - 2
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % MOD
        a = (a * a) % MOD
        b //= 2
    return result

# Fonction pour calculer les combinaisons nCk modulo MOD
def comb(n, k):
    if n < 0 or k < 0 or n < k:
        return 0
    return (fact[n] * modinv(fact[k]) % MOD) * modinv(fact[n-k]) % MOD

# Fonction f(x, y)
def f(x, y):
    return comb(x + y, y)

# Fonction g(x, y)
def g(x, y):
    return f(x + 1, y + 1)

result = (g(r2, c2) - g(r2, c1-1) - g(r1 - 1, c2) + g(r1 - 1, c1 - 1)) % MOD
print(result)