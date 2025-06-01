def count_duplicates():
    """
    Lit un nombre entier N, puis lit N lignes contenant chacune deux entiers.
    Chaque paire est triée et ajoutée dans un ensemble pour garantir l'unicité.
    Affiche ensuite le nombre d'éléments en double, c'est-à-dire la différence entre N et la taille de l'ensemble.

    Exemple d'entrée :
    3
    1 2
    2 1
    3 4

    Exemple de sortie :
    1

    Car la paire (1,2) et (2,1) sont considérées identiques après tri.
    """
    # Lecture du nombre total d'éléments
    N = int(input())

    # Initialisation d'un ensemble pour stocker les paires uniques
    s = set()

    # Parcours de chaque paire fournie en entrée
    for _ in range(N):
        # Lecture de deux entiers et les trier pour normaliser l'ordre
        pair = tuple(sorted(map(int, input().split())))
        # Ajout de la paire triée à l'ensemble
        s.add(pair)

    # Le nombre de doublons est le total moins le nombre d'éléments uniques
    duplicates = N - len(s)

    # Affichage du résultat
    print(duplicates)


# Appel de la fonction principale
count_duplicates()