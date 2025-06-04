import sys
import bisect
input = sys.stdin.readline

N, K, L = map(int, input().split())
a = list(map(int, input().split()))

# On veut trouver le L-ième plus petit nombre des K-ième plus petits éléments
# de toutes sous-séquences contiguës de longueur >= K.
# Pour chaque nombre x, on peut compter combien de sous-séquences ont comme K-ième plus petit élément <= x.
# Utiliser une recherche binaire sur la valeur.

def count_subarrays(x):
    # Pour un x donné, compte le nombre de sous-tableaux dont le K-ième plus petit élément <= x.
    # On transforme a en b où b[i]=1 si a[i] <= x sinon 0.
    # Pour que le K-ieme plus petit <= x, il faut qu'il y ait au moins K éléments <= x dans la sous-séquence.
    # Donc on cherche le nombre de sous-tableaux contigus avec au moins K uns.
    b = [0]*(N+1)
    for i in range(N):
        b[i+1] = b[i] + (1 if a[i] <= x else 0)
    # On compte le nombre de paires (l,r) avec b[r] - b[l] >= K, l<r.
    # Comme b est croissante par l'ajout de 0 ou 1, on peut gérer par deux pointeurs.
    res = 0
    r = 0
    for l in range(N+1):
        while r <= N and b[r] - b[l] < K:
            r += 1
        if r > N:
            break
        res += N - r + 1
    return res

left, right = 1, N
while left < right:
    mid = (left + right) // 2
    c = count_subarrays(mid)
    if c >= L:
        right = mid
    else:
        left = mid + 1

print(left)