import sys
input = sys.stdin.readline

# N: nombre de pièces d'art
N = int(input())
items = []
for _ in range(N):
    A, B = map(int, input().split())
    items.append((A, B))

# Trie des œuvres par taille croissante
items.sort(key=lambda x: x[0])

# Préfixe des valeurs : prefix_sum[i] = somme des valeurs des i premiers objets
prefix_sum = [0]
for _, B in items:
    prefix_sum.append(prefix_sum[-1] + B)

# On veut maximiser S - (A_max - A_min)
# Avec les objets triés par taille, pour une sous-liste continue [l, r], 
# A_min = items[l][0], A_max = items[r][0], donc (A_max - A_min) = items[r][0] - items[l][0]
# S = somme des B_i de l à r = prefix_sum[r+1] - prefix_sum[l]
# On itère sur la borne droite r et on trouve la meilleure borne gauche l ≤ r
# le problème revient à, pour chaque r, maximiser (prefix_sum[r+1] - items[r][0] - prefix_sum[l] + items[l][0])
# c'est-à-dire maximiser (- prefix_sum[l] + items[l][0])

# On maintient un minimum strictement croissant de (-prefix_sum[l] + items[l][0]) pour trouver la meilleure valeur

max_value = -10**18  # assez petit pour démarrer
best = -10**18

# Pour chaque r, calcule la valeur courante et update le max
# On stocke les (items[l][0] - prefix_sum[l]) car on maximiser ce terme

min_val = items[0][0] - prefix_sum[0]  # pour l=0
for r in range(N):
    cur = prefix_sum[r+1] - items[r][0] + min_val
    if cur > max_value:
        max_value = cur

    if r+1 < N:
        candidate = items[r+1][0] - prefix_sum[r+1]
        if candidate > min_val:
            min_val = candidate

print(max_value)