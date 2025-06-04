import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
p = list(map(int, input().split()))

# Limite pratique sur le m à cause des grands calculs de division
# mais on doit gérer jusqu'à 10^18, donc approche inclue doit être mathématique.

# Probabilité que le k-ième nombre soit sélectionné
prob = [x/100 for x in p]

# On utilise un dictionnaire pour mémoriser LCM -> prob
# On fait une DP sur les nombres choisis avec inclusion-exclusion probabiliste.

from math import gcd

def lcm(x, y):
    return x//gcd(x,y)*y

dp = {1: 1.0}  # LCM 1 avec probabilité 1 (ensemble vide)

for i in range(n):
    next_dp = dict(dp)
    x = a[i]
    px = prob[i]
    for L, pr in dp.items():
        newL = lcm(L, x) if L != 0 else x
        # Ajouter a[i]
        next_dp[newL] = next_dp.get(newL, 0.0) + pr * px
        # Ne pas ajouter a[i]
        next_dp[L] = next_dp.get(L, 0.0) + pr * (1-px)
    # Les deux sont déjà incrémentés, on corrige les doubles ajouts
    # On a compté pr deux fois, il faut soustraire une fois pr
    for k in dp:
        next_dp[k] -= dp[k]
    dp = next_dp

# dp contient maintenant les probabilités pour chaque LCM

# Correction : la boucle précédente double la somme, c'est incorrect.
# Refaire ce calcul plus simplement:

dp = {1:1.0}
for i in range(n):
    ndp = dict()
    x = a[i]
    px = prob[i]
    for L, pr in dp.items():
        ndp[L] = ndp.get(L,0.0) + pr*(1 - px)
        newL = lcm(L, x)
        ndp[newL] = ndp.get(newL,0.0) + pr*px
    dp = ndp

# dp now sums to 1, representing the probability distribution of the LCM of selected elements

# Expected count = sum over L != 1 of dp[L]*floor(m/L)
# For L=1 (empty set), count=0

ans = 0.0
for L, pr in dp.items():
    if L == 1:
        continue
    ans += pr * (m // L)

print(f"{ans:.10f}")