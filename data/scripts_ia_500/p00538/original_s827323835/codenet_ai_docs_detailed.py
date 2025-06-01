import sys

# Augmente la limite de récursion pour permettre des appels récursifs profonds
sys.setrecursionlimit(10000)

# Lecture de la taille 'n' de la séquence depuis l'entrée utilisateur
n = int(input())

# Lecture de la séquence de n entiers, puis réplication 3 fois de suite pour gérer les indices circulaires
A = [int(input()) for i in range(n)] * 3

# Initialisation d'une matrice 2D dp de taille (2n x 2n) pour la mémoïsation,
# contenant -1 pour indiquer des sous-problèmes non encore calculés
dp = [[-1 for i in range(n * 2)] for j in range(n * 2)]

def dfs(i, j):
    """
    Fonction récursive de mémoïsation utilisant le paradigme DFS pour calculer la valeur optimale
    sur un intervalle donné [i, j] dans la séquence A.

    Args:
        i (int): Index de début de l'intervalle (inclus).
        j (int): Index de fin de l'intervalle (inclus).

    Returns:
        int: La valeur optimale calculée pour l'intervalle [i, j].
    """
    # Si le résultat est déjà calculé, on le retourne directement (mémoïsation)
    if dp[i][j] != -1:
        # Résultat déjà calculé, pas besoin de recomputation
        pass
    # Condition de base quand la longueur de l'intervalle est de n éléments (j - i == n - 1)
    elif (j - i == n - 1):
        dp[i][j] = 0
    # Cas où la longueur de l'intervalle est un nombre pair
    elif (j - i) % 2 == 0:
        # On compare l'élément avant i et l'élément après j pour déterminer la branche à suivre
        if A[i - 1] > A[j + 1]:
            dp[i][j] = dfs(i - 1, j)
        else:
            dp[i][j] = dfs(i, j + 1)
    # Cas où la longueur de l'intervalle est impaire
    else:
        # Calcul du max entre deux options possibles, incluant les valeurs associées dans A
        dp[i][j] = max(
            dfs(i - 1, j) + A[i - 1],
            dfs(i, j + 1) + A[j + 1]
        )
    return dp[i][j]

# Variable pour stocker la meilleure valeur trouvée
ans = 0

# On teste tous les indices de départ possibles dans la séquence initiale
for i in range(n):
    # Calcule le maximum en considérant l'intervalle commençant et finissant à i, plus la valeur A[i]
    ans = max(ans, dfs(i, i) + A[i])

# Affichage de la meilleure valeur optimale trouvée
print(ans)