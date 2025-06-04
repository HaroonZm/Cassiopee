A, B, C = map(int, input().split())

# On essaie de trouver le minimum de jours n tel que les pièces obtenues >= C
# Les pièces obtenues se calculent par:
# - pièces journalières: n * A
# - bonus pour chaque semaine complète (7 jours): (n // 7) * B

def coins(n):
    return n * A + (n // 7) * B

# Recherche binaire pour trouver le plus petit n avec coins(n) >= C
low, high = 1, 10**7  # borne haute suffisamment grande
while low < high:
    mid = (low + high) // 2
    if coins(mid) >= C:
        high = mid
    else:
        low = mid + 1

print(low)