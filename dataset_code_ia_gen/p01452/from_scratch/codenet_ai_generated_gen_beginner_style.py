MOD = 10**9 + 7

N, M, K = map(int, input().split())

# Une solution débutante : on calcule le nombre de chemins avec K détours.
# Chaque détour est un pas vers la gauche ou vers le bas.
# On doit faire exactement N + K pas vers la droite et M + K pas vers le haut,
# et K pas vers la gauche et K pas vers le bas (les détours).
# Le nombre total de pas est (N + K) + (M + K) + K + K = N + M + 4K
# Mais on peut revenir sur ses pas, donc on considère les chemins combinatoires qui contiennent
# (N + K) droites, (M + K) haut, K gauche, K bas.

# Le nombre de chemins est le nombre de permutations d'un mot avec ces lettres:
# D (droite) x (N+K)
# U (haut) x (M+K)
# L (gauche) x K
# B (bas) x K

# Le nombre total de pas est T = N + M + 4K

# Le nombre de chemins est donc:
# C(T, N+K) * C(T-(N+K), M+K) * C(T-(N+K)-(M+K), K)
# C(T-(N+K)-(M+K)-K, K) mais après on aura utilisé tous les K de L et B.

# On calcule les factorielles modulo MOD pour calculer ces combinaisons.

max_val = N + M + 4 * K

fact = [1] * (max_val + 1)
for i in range(1, max_val + 1):
    fact[i] = fact[i - 1] * i % MOD

def inv(a):
    # Fermat inverse modulo, MOD est premier
    return pow(a, MOD - 2, MOD)

inv_fact = [1] * (max_val +1)
inv_fact[max_val] = inv(fact[max_val])
for i in range(max_val-1, -1, -1):
    inv_fact[i] = inv_fact[i +1] * (i+1) % MOD

def comb(n, r):
    if r > n or r < 0:
        return 0
    return fact[n] * inv_fact[r] % MOD * inv_fact[n-r] % MOD

T = N + M + 4 * K

res = comb(T, N + K)
res = (res * comb(T - (N + K), M + K)) % MOD
res = (res * comb(T - (N + K) - (M + K), K)) % MOD
res = (res * comb(T - (N + K) - (M + K) - K, K)) % MOD

print(res % MOD)