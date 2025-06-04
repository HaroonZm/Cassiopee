"""
Ce script calcule le nombre de manières de remplir un tableau de N éléments avec certaines contraintes de répétition, modulo M. 
K correspond à la taille maximale des blocs consécutifs admissibles selon une règle parité, avec un traitement spécial si K est pair ou impair.

Entrée : 
    N, K, M : trois entiers lus sur une même ligne.
Sortie : 
    Un entier représentant la solution modulo M.
"""

# Lecture des trois entiers N (taille), K (contrainte), M (modulo)
N, K, M = map(int, input().split())

# Détermine la taille maximale pour le DP à 3 dimensions (pour le cas impair)
L = (N + 1) // 2 + 1

def even(n, k):
    """
    Calcule le nombre de manières de remplir une séquence de longueur n, 
    où il n'y a jamais plus de k éléments identiques consécutifs.
    
    Utilise un DP où dp[i][j] représente le nombre de façons de construire
    une séquence de longueur i, se terminant par exactement j éléments consécutifs
    identiques.

    Args:
        n (int): longueur de la séquence à remplir.
        k (int): contrainte sur la longueur maximale de répétition.
    Returns:
        int: nombre de séquences valides modulo M.
    """
    # Initialisation du tableau DP: dp[position][longueur_bloc_actuel]
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    # Cas de base : une séquence vide est valide
    dp[0][0] = 1
    for i in range(n):
        for j in range(k + 1):
            # Ajouter un nouvel élément différent (réinitialise le bloc à 0)
            dp[i + 1][0] = (dp[i + 1][0] + dp[i][j]) % M
            # Ajouter le même élément actuel, si la limite de répétition n'est pas atteinte
            if j != k:
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % M
    # Somme de toutes les séquences complètes, pour tous les états de répétition
    return sum(dp[n]) % M

def loop(x, y):
    """
    Détecte si une configuration n'est pas autorisée selon les règles 
    combinatoires du problème (utilisé seulement pour K impair/patterns spéciaux).

    Args:
        x (int): nombre d'éléments consécutifs de parité différente.
        y (int): nombre d'éléments consécutifs de même parité.
    Returns:
        bool: True si la configuration est interdite, False sinon.
    """
    return (2 * x >= K + 1 and 2 * y >= K + 3)

if K % 2 == 0:
    # CAS K pair : Le problème se sépare en deux sous-parties indépendantes
    # Calcul sur chaque sous-partie puis on multiplie les résultats
    res1 = even(N // 2, K // 2)
    res2 = even((N + 1) // 2, K // 2)
    print(res1 * res2 % M)
else:
    # CAS K impair : Utilisation d'un DP à 3 dimensions 
    # dp[x][y][z] : nombre de façons de construire une séquence avec:
    # x éléments consécutifs de parité différente, 
    # y éléments de parité identique, 
    # et z = le maximum "potentiel" jusqu'où on peut allonger un bloc.
    dp0 = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(L + 1)]
    # Cas initial : aucune case placée, limite de bloc au max
    dp0[0][0][L] = 1

    for i in range(N):
        # Prépare DP de la prochaine étape
        dp1 = [[[0] * (L + 1) for _ in range(L + 1)] for _ in range(L + 1)]
        for x in range(L + 1):
            for y in range(L + 1):
                if loop(x, y):
                    # Ignore les patterns invalides selon la règle de loop
                    continue
                # Pour chaque z possible, où z > max(x, y)
                for z in range(max(x, y) + 1, L + 1):
                    if dp0[x][y][z] == 0:
                        # Pas de façon possible d'atteindre cet état, on saute
                        continue
                    # Cas où l'on ajoute un élément de parité différente
                    dp1[y][x + 1][z] = (dp1[y][x + 1][z] + dp0[x][y][z]) % M
                    # Cas où l'on ajoute un élément de même parité, mise à jour de z
                    # (1) Si le bloc actuel de même parité est plus long que l'autre, on garde z, sinon on remet z à L
                    if y > x:
                        zz = z
                    else:
                        zz = L
                    # (2) Si un motif spécial (le pattern "↖") est autorisé, on raffine zz
                    if 2 * y >= K + 3 and x > 0:
                        zz = min(zz, 1 + y - x + K // 2)
                    dp1[y][0][zz] = (dp1[y][0][zz] + dp0[x][y][z]) % M
        # Passage à l'étape suivante
        dp0 = dp1

    # Accumulation de toutes les configurations valides en respectant loop()
    ret = 0
    for x in range(L + 1):
        for y in range(L + 1):
            if loop(x, y):
                continue
            for z in range(max(x, y) + 1, L + 1):
                ret = (ret + dp0[x][y][z]) % M
    print(ret)