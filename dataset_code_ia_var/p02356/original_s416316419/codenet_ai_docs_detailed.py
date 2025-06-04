def solve(A, x):
    """
    Calcule le nombre de sous-tableaux consécutifs dans A dont la somme des éléments est inférieure ou égale à x.

    Paramètres:
        A (list of int): Le tableau d'entiers à examiner.
        x (int): La valeur limite supérieure pour la somme des sous-tableaux.

    Retourne:
        int: Le nombre de sous-tableaux consécutifs où la somme <= x.
    """
    i = 0  # Pointeur de début du sous-tableau courant
    total = 0  # Somme courante des éléments du sous-tableau
    res = 0  # Compteur du nombre de sous-tableaux valides

    # On parcourt tous les éléments du tableau comme extrémité droite des sous-tableaux
    for j in range(len(A)):
        total += A[j]  # Ajoute l'élément courant à la somme

        # Réduit la fenêtre jusqu'à ce que la somme soit <= x
        while total > x:
            total -= A[i]  # Retire l'élément le plus à gauche
            i += 1         # Déplace la borne gauche du sous-tableau à droite

        # Pour chaque position j, il existe (j - i + 1) sous-tableaux valides terminant en j
        res += j - i + 1

    return res

# Lecture de la taille du tableau N et du nombre de requêtes Q
N, Q = map(int, input().split())

# Lecture du tableau d'entiers A
A = list(map(int, input().split()))

# Lecture des Q valeurs cibles sous forme de liste X
X = list(map(int, input().split()))

# Pour chaque valeur cible x, calcul du résultat et affichage
for x in X:
    print(solve(A, x))