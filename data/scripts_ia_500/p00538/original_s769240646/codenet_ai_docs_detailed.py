import sys

# Augmente la limite de récursivité pour permettre des appels récursifs profonds
sys.setrecursionlimit(100000)

# Lecture des entrées : N est le nombre d'éléments,
# A est la liste des éléments
N, *A = map(int, open(0).read().split())

# Initialisation d'une matrice de mémoïsation pour stocker les résultats intermédiaires
# Chaque case memo[p][q] correspond au résultat de la sous-problématique pour l'intervalle p à q
# initialisée à -1 pour indiquer que ce sous-problème n'a pas encore été calculé
memo = [[-1]*N for _ in range(N)]

# Remplissage de la diagonale de la matrice memo
# Si N est impair, le joueur prend l'élément seul A[i] (car il est le seul dans cet intervalle)
# sinon, la valeur est 0 (pas de gain si nombre pair d'éléments)
for i in range(N):
    memo[i][i] = A[i] if N % 2 else 0

def dfs(p, q, t):
    """
    Fonction récursive qui calcule le meilleur score que peut obtenir un joueur
    jouant dans l'intervalle circulaire d'indice p à q inclus selon un tour t donné.

    Args:
        p (int): indice de début de l'intervalle circulaire (modulo N)
        q (int): indice de fin de l'intervalle circulaire (modulo N)
        t (int): indique quel joueur joue (1 pour le premier joueur, 0 pour l'adversaire)

    Returns:
        int: le score maximum réalisable par le joueur t sur l'intervalle [p, q]
    """
    # Si ce sous-problème a déjà été calculé, on retourne son résultat mémorisé
    if memo[p][q] != -1:
        return memo[p][q]

    if t == 1:
        # Tour du premier joueur : maximise son gain en choisissant entre
        # prendre l'élément à l'indice p ou celui à l'indice q
        gain_p = A[p] + dfs((p+1) % N, q, 0)  # prendre A[p], puis tour adversaire
        gain_q = A[q] + dfs(p, (q-1) % N, 0)  # prendre A[q], puis tour adversaire
        memo[p][q] = max(gain_p, gain_q)
    else:
        # Tour de l'adversaire : minimise le gain du premier joueur
        # L'adversaire prend l'élément qui laisse le moins d'options avantageuses
        if A[p] < A[q]:
            memo[p][q] = dfs(p, (q-1) % N, 1)  # adversaire prend A[q]
        else:
            memo[p][q] = dfs((p+1) % N, q, 1)  # adversaire prend A[p]

    return memo[p][q]

# Calcul du meilleur score global réalisable par le premier joueur
ans = 0
for i in range(N):
    # Le premier joueur commence par prendre l'élément A[i], puis c'est au tour de l'adversaire
    # On calcule le score total dans ce cas et on garde le maximum
    ans = max(ans, A[i] + dfs((i+1) % N, (i-1) % N, 0))

# Affichage du résultat final
print(ans)