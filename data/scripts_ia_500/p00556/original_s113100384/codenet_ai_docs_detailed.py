N, M = map(int, input().split())
# N : nombre total d'éléments
# M : nombre de catégories ou groupes

# Initialisation d'une matrice pour le calcul des sommes cumulées
# D[i][j] comptera le nombre d'éléments du groupe i dans les j premiers éléments (1-based)
D = [[0]*(N+1) for i in range(M)]

# Liste qui comptera le nombre total d'éléments pour chaque groupe
cnts = [0]*M

# Lecture des éléments et mise à jour des compteurs et de la matrice D
for i in range(N):
    v = int(input())
    cnts[v-1] += 1  # Compter le nombre d'éléments dans chaque groupe v-1
    D[v-1][i+1] = 1  # Marquer la présence de l'élément du groupe v-1 à la position i+1

# Calcul des sommes cumulées pour chaque groupe (pré-calcul pour accélérer les requêtes ultérieures)
for i in range(M):
    d = D[i]
    for j in range(1, N+1):
        d[j] += d[j-1]

# Memoisation pour la programmation dynamique, avec 2^M états possibles
# Chaque bit de 'state' représente si un groupe a été traité (1) ou pas (0)
memo = [None]*(2**M)
memo[2**M-1] = 0  # Cas de base : tous les groupes traités, coût 0

def dfs(state, idx):
    """
    Fonction de recherche en profondeur avec mémoïsation pour calculer le nombre minimal de corrections.
    
    Args:
        state (int): Entier représentant l'état actuel des groupes traités. Chaque bit i indique si le groupe i est traité (1) ou non (0).
        idx (int): Position actuelle dans la séquence d'éléments.

    Returns:
        int: Nombre minimal de corrections nécessaires à partir de cet état.
    """
    # Si on a déjà calculé le résultat pour cet état, on le retourne directement
    if memo[state] is not None:
        return memo[state]
    
    res = N  # Initialisation à un maximum de corrections possible (toute la séquence)
    
    # On essaie de traiter chaque groupe non encore traité
    for i in range(M):
        if state & (1 << i) == 0:  # Si le groupe i n'a pas encore été traité
            # Calculer combien d'éléments de ce groupe sont hors de la séquence attendue
            need = cnts[i] - (D[i][cnts[i] + idx] - D[i][idx])
            # Appel récursif avec le groupe i marqué comme traité et l'indice avancé de la taille du groupe
            res = min(res, need + dfs(state | (1 << i), idx + cnts[i]))
    
    memo[state] = res  # Mémoriser le résultat pour éviter les calculs redondants
    return res

# Appel initial du DFS avec aucun groupe traité et l'indice initial à 0
print(dfs(0, 0))