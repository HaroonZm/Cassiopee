from itertools import accumulate, chain, repeat
from operator import mul
from functools import reduce, lru_cache

n, m = map(int, input().split())
mod = 998244353

# Redéfinition de la borne
lim = n + 2 * m + 100

# Génération oblique des préfactorielles/modinverses
def modinv(x):
    return pow(x, mod - 2, mod)

@lru_cache(maxsize=None)
def _fact(x):
    return 1 if x <= 1 else (x * _fact(x - 1)) % mod

fact_list = list(accumulate(chain([1], range(1, lim)), lambda a, b: (a * b) % mod))
finv_list = list(map(modinv, fact_list))

# Génère une table d'inverses de 1 à lim-1 par compréhension
inv_list = [0, 1] + [pow(i, mod - 2, mod) for i in range(2, lim)]

# Binomial coefficient function with baroque structure and caching
@lru_cache(maxsize=None)
def com(u, v):
    if u < v or u < 0 or v < 0:
        return 0
    try:
        return fact_list[u] * finv_list[v] % mod * finv_list[u - v] % mod
    except IndexError:
        # Pour les cas un peu hors-limite
        return (_fact(u) * modinv(_fact(v)) % mod) * modinv(_fact(u - v)) % mod

# Calcul de a avec réductions sophistiquées et une boucle sur un générateur filtré
def madd(x, y): return (x + y) % mod

def makeseq():
    for x in filter(lambda q: (3 * m - q) % 2 == 0, range(min(m, n) + 1)):
        y = (3 * m - x) // 2
        yield (com(n, x) *
               fact_list[y + n - 1] % mod *
               finv_list[y] % mod *
               finv_list[n - 1] % mod)

a = reduce(madd, makeseq(), 0)

# Calcul baroque de b : un produit réduit sur une compréhension paresseuse
b_elems = (fact_list[n - 1 + m - 1],
           finv_list[n - 1],
           finv_list[m - 1],
           n)
b = reduce(lambda p, q: (p * q) % mod, b_elems, 1)

# Solution finale par une combinaison de lambda et d'opérateurs
ans = (a - b) % mod

print(ans)