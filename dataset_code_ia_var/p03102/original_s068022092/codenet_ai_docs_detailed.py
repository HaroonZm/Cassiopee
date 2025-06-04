def actual(n, m, C, B, A):
    """
    Calcule le nombre de tableaux (lignes) dans A pour lesquels la somme pondérée (produit scalaire avec B plus C)
    est strictement supérieure à zéro.

    Args:
        n (int): Le nombre de tableaux (lignes) dans A.
        m (int): Le nombre d'éléments dans chaque tableau (colonnes).
        C (int): La constante ajoutée à la somme pondérée pour chaque ligne.
        B (list of int): Le vecteur de coefficients utilisé dans le produit scalaire.
        A (list of list of int): La matrice contenant les tableaux à analyser.

    Returns:
        int: Nombre de lignes satisfaisant la condition (produit scalaire + C > 0).
    """
    # Initialise un compteur pour suivre combien de lignes vérifient la condition
    cnt = 0

    # Parcourt chaque ligne du tableau A
    for A_i in A:
        # Calcule le produit scalaire entre la ligne A_i et le vecteur B
        ab = sum([a * b for a, b in zip(A_i, B)])

        # Vérifie si la somme pondérée plus la constante C est strictement positive
        if ab + C > 0:
            cnt += 1  # Incrémente le compteur si la condition est satisfaite

    # Retourne le nombre total de lignes satisfaisant la condition
    return cnt

# Lecture de l'entrée utilisateur :
# N : nombre de tableaux (lignes)
# M : nombre d'éléments dans chaque tableau (colonnes)
# C : constante à ajouter
N, M, C = map(int, input().split())

# Lecture du vecteur B de taille M
B = list(map(int, input().split()))

# Lecture des N lignes de la matrice A, chaque ligne contenant M entiers
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))

# Appel de la fonction et affichage du résultat
print(actual(N, M, C, B, A))