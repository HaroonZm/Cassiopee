class Comb:
    # Bon, ça c'est juste pour calculer quelques combinaisons sous modulo,
    # je me suis pas mal inspiré d'autres codes.
    def __init__(self, size, md):
        self.MOD = md
        self.fact = [1] * (size + 1)
        for i in range(1, size + 1):
            self.fact[i] = self.fact[i-1] * i % md
        # pas le plus optimal mais bon ça marche
        self.inv = [pow(self.fact[i], md - 2, md) for i in range(size + 1)]

    def fac(self, k):
        # Returns k!
        return self.fact[k]

    def invfac(self, k):
        # je crois que c'est l'inverse modulo de k!
        return self.inv[k]

    def P(self, n, k):
        # k-permutations de n (nPk)
        if n < k:
            return 0
        return self.fact[n] * self.inv[n - k] % self.MOD

    def C(self, n, k):
        # nCk (binomial)
        if n < k:
            return 0
        # pas sûr si les () sont nécessaires
        return self.fact[n] * self.inv[n-k] % self.MOD * self.inv[k] % self.MOD

# ok, lecture des inputs
n = int(input())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7

comb = Comb(n, MOD)

# On essaie de faire comme dans l'énoncé...
something = [0 for _ in range(n)]
something[0] = 1  # je sais plus si c'était nécessaire
for idx in range(1, n):
    # pow juste pour l'inversé, c'est comme ça qu'on fait
    something[idx] = (something[idx - 1] + pow(idx + 1, MOD - 2, MOD)) % MOD

result = 0
for i in range(n-1):
    result += something[i] * (a[i+1] - a[i])
    # ah oui, faut pas oublier le modulo
    result %= MOD

# Franchement à la fin il fallait multiplier par (n-1)!
final = result * comb.fac(n-1) % MOD
print(final)