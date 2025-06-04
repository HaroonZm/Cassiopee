def x(a):
    """
    Calcule la plus grande sous-somme possible de toutes les sous-matrices possibles dans une matrice 2D donnée.
    
    Paramètres :
    ----------
    a : list of list of int
        La matrice contenant les valeurs entières (dimensions n x n).

    Retourne :
    -------
    int
        La valeur maximale trouvée dans toutes les sous-matrices (sous-somme maximale).
    """
    m = -10**9  # Initialise la variable de la sous-somme maximale à une très petite valeur
    for c in N:  # Parcourir tous les indices de colonne de début
        p = [0] * n  # Vecteur temporaire pour stocker la somme par ligne
        for e in range(c, n):  # Pour toutes les colonnes de fin possibles à partir de c
            for r in N:  # Pour chaque ligne
                p[r] += a[r][e]  # Ajoute l'élément de la colonne courante à la somme de la ligne
            # Calcule la meilleure sous-somme possible pour le vecteur 'p' (soit la somme pour la sous-matrice [*, c:e])
            m = max(P(p), m)
    return m

def P(a):
    """
    Implémente l'algorithme de Kadane pour trouver la sous-somme maximale dans un tableau 1D.
    
    Paramètres :
    ----------
    a : list of int
        Tableau d'entiers.

    Retourne :
    -------
    int
        La valeur de la plus grande sous-somme trouvée dans le tableau.
    """
    m, c = -10**5, 0  # Initialise m à une petite valeur et c (somme courante) à zéro
    for i in N:  # Pour chaque indice du tableau
        c += a[i]  # Ajoute l'élément courant à la somme courante
        m = max(c, m)  # Met à jour la valeur maximale si nécessaire
        if c < 0:  # Si la somme courante devient négative, on la remet à zéro
            c = 0
    return m

# Lecture des entrées
n = input()  # Lecture du nombre de lignes/colonnes de la matrice carrée
N = range(n)  # Initialise un objet range pour un parcours répété

# Lecture de la matrice depuis l'entrée utilisateur ligne par ligne
# Chaque ligne est convertie en une liste d'entiers
matrix = [map(int, raw_input().split()) for i in N]

# Affiche le résultat maximal de sous-somme calculé pour la matrice
print x(matrix)