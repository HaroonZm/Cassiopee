from itertools import accumulate

INF = 10 ** 20  # Une valeur très grande utilisée comme initialisation pour la minimisation

# Lecture du nombre d'éléments
n = int(input())

# Initialisation des listes pour stocker les capacités (c_lst) et les poids (w_lst)
c_lst = []
w_lst = []

# Lecture des paires (capacité, poids) pour chaque élément
for _ in range(n):
    c, w = map(int, input().split())
    c_lst.append(c)
    w_lst.append(w)

# Calcul de la somme cumulée des poids (w_acc) pour faciliter les calculs d'intervalles
# w_acc[i] correspond à la somme des poids des éléments jusqu'à l'indice i-1
w_acc = [0] + list(accumulate(w_lst))

# Initialisation de la matrice connect qui mémorisera si un intervalle [left, right] est connectable
# None signifie non encore calculé, True/False signifie le résultat connu
connect = [[None] * n for _ in range(n)]

# Un seul élément est toujours connectable avec lui-même
for i in range(n):
    connect[i][i] = True

def can_connect(left, right):
    """
    Détermine si l'on peut connecter tous les éléments dans l'intervalle [left, right].

    La connexion est valide si :
    - Soit la capacité du premier élément est suffisante pour supporter les poids des autres éléments de l'intervalle,
      ET le sous-intervalle [left+1, right] est connectable
    - Soit la capacité du dernier élément est suffisante pour supporter les poids des autres éléments de l'intervalle,
      ET le sous-intervalle [left, right-1] est connectable

    Args:
        left (int): indice de début de l'intervalle
        right (int): indice de fin de l'intervalle

    Returns:
        bool: True si l'intervalle est connectable, False sinon
    """
    # Si le résultat a déjà été calculé, on le renvoie directement (mémoization)
    if connect[left][right] is not None:
        return connect[left][right]

    # Calcul du poids total des éléments sauf le premier dans l'intervalle [left, right]
    weight_excl_first = w_acc[right + 1] - w_acc[left + 1]
    # Calcul du poids total des éléments sauf le dernier dans l'intervalle [left, right]
    weight_excl_last = w_acc[right] - w_acc[left]

    # Vérification de la connectivité par la gauche et par la droite
    can_connect_left = (c_lst[left] >= weight_excl_first) and can_connect(left + 1, right)
    can_connect_right = (c_lst[right] >= weight_excl_last) and can_connect(left, right - 1)

    # Stockage du résultat dans la matrice connect et retour
    connect[left][right] = can_connect_left or can_connect_right
    return connect[left][right]

# Calcul de la connectivité pour tous les intervalles possibles
for i in range(n):
    for j in range(i + 1, n):
        can_connect(i, j)

# Initialisation du tableau dp pour calculer le nombre minimal de connexions nécessaires
# dp[i] représente le minimum de connexions pour connecter les éléments jusqu'à l'indice i-1 inclus
dp = [INF] * (n + 1)
dp[0] = 0  # Aucun élément nécessite zéro connexion

# Calcul dynamique pour trouver le minimal
for i in range(n):
    for j in range(i, n):
        if connect[i][j]:
            # Mise à jour du dp pour couvrir l'intervalle de i à j en une connexion
            dp[j + 1] = min(dp[j + 1], dp[i] + 1)
        else:
            # Si l'intervalle [i, j] n'est pas connectable, inutile d'étendre à des j plus grands
            break

# Impression du nombre minimal de connexions nécessaires pour tous les éléments
print(dp[n])