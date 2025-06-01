H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# La position de la scierie est (0,0)
# Le problème décrit le temps nécessaire pour abattre tous les arbres
# permettant de relier le coin nord-ouest au coin sud-est.
# En pratique, il faut que le chemin entre (0,0) et (H-1,W-1) soit déboisé.
# La seule façon de le faire est d'abattre tous les arbres sur ce chemin,
# ou dans toute cellule où les arbres existent, car on ne peut se déplacer
# que dans les cases sans arbre.
# Pour chaque case avec des arbres (x, y), il faut:
# - parcourir le chemin (0,0)->(x,y) aller-retour
# - abattre tous les arbres (temps = nombre d'arbres * temps par arbre)
# Le coût pour chaque arbre dans (x,y) est donc:
# nombre_arbres * distance_aller_retour
# La distance est la distance de Manhattan = abs(x-0)+abs(y-0)
# Aller-retour multiplie par 2
# La somme pour toutes les cases ≠ (0,0) est la réponse.

time = 0
for i in range(H):
    for j in range(W):
        if A[i][j] > 0:
            dist = i + j
            time += A[i][j] * (2 * dist)
print(time)