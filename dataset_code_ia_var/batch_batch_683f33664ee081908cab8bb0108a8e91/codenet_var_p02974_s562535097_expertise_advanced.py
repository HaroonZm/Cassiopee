from functools import lru_cache

mod = 10**9 + 7

N, K = map(int, input().split())

@lru_cache(maxsize=None)
def dp(i, j, k):
    if k < 0 or k > K or j < 0 or j > N or i > N:
        return 0
    if i == 0 and j == 0 and k == 0:
        return 1
    if i == 0:
        return 0

    res = 0
    # Ouvrir une nouvelle paire
    res += dp(i-1, j-1, k - 2*(j-1) - 2) if j >= 1 and k >= 2*(j-1) + 2 else 0
    # Créer une paire individuelle
    res += dp(i-1, j, k - 2*j) if k >= 2*j else 0
    # Ajouter à une paire existante
    if j + 1 <= N and k >= 2*(j+1):
        res += (j+1) * dp(i-1, j+1, k - 2*(j+1))
        res += (j+1) * dp(i-1, j+1, k - 2*(j+1))
    # Fermer une paire
    if j + 2 <= N and k >= 2*(j+2) - 2:
        res += ((j+2)*(j+2)) * dp(i-1, j+2, k - 2*(j+2) + 2)
    return res % mod

print(dp(N, 0, K))