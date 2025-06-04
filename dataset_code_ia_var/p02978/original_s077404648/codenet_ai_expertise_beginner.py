N = int(input())
A = list(map(int, input().split()))

# On va utiliser un dictionnaire pour mémoriser les résultats déjà calculés
memo = {}

def dp(i, j, L, R):
    # On regarde si le résultat a déjà été calculé
    if (i, j, L, R) in memo:
        return memo[(i, j, L, R)]
    # Si il ne reste qu'un seul élément à traiter
    if i == j:
        sortie = (L + R) * A[i]
        memo[(i, j, L, R)] = sortie
        return sortie
    # Cas où i dépasse j, il n'y a plus rien à faire
    if i > j:
        return 0

    # On va essayer toutes les coupures possibles
    minimum = 10 ** 18
    for k in range(i, j + 1):
        gauche = dp(i, k - 1, L, L + R)
        droite = dp(k + 1, j, L + R, R)
        val = gauche + droite + A[k] * (L + R)
        if val < minimum:
            minimum = val

    memo[(i, j, L, R)] = minimum
    return minimum

# On lance l'algo en ignorant les extrémités de la liste (A[0] et A[N-1])
resultat = dp(1, N - 2, 1, 1)
# Puis on ajoute les bords
print(resultat + A[0] + A[-1])