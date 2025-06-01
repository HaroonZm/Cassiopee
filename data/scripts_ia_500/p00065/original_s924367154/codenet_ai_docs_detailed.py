def count_x_occurrences_dict_a():
    """
    Lit des paires de nombres entiers séparés par une virgule depuis l'entrée standard,
    jusqu'à ce qu'une ligne vide soit rencontrée. Pour chaque paire (x, y),
    compte le nombre d'occurrences de chaque valeur de x et les stocke dans un dictionnaire.

    Returns:
        dict: Un dictionnaire où les clés sont les valeurs de x et les valeurs sont leurs fréquences dans l'entrée.
    """
    A = {}  # Initialisation du dictionnaire pour stocker les counts des x
    while True:
        S = input()  # Lecture d'une ligne d'entrée
        if S == '':
            # Arrêt de la boucle si la ligne est vide
            break
        x, y = map(int, S.split(','))  # Séparation de la ligne en deux entiers x et y
        if x in A:
            # Si x est déjà présent en clé, incrémenter son compteur
            A[x] += 1
        else:
            # Sinon, initialiser le compteur à 1
            A[x] = 1
    return A


def count_x_occurrences_dict_b():
    """
    Lit des paires de nombres entiers séparés par une virgule depuis l'entrée standard,
    jusqu'à la fin de fichier (EOF). Pour chaque paire (x, y),
    compte le nombre d'occurrences de chaque valeur de x et les stocke dans un dictionnaire.

    Returns:
        dict: Un dictionnaire où les clés sont les valeurs de x et les valeurs sont leurs fréquences dans l'entrée.
    """
    B = {}  # Initialisation du dictionnaire pour stocker les counts des x
    while True:
        try:
            line = input()  # Lecture d'une ligne d'entrée
            x, y = map(int, line.split(','))  # Séparation de la ligne en deux entiers x et y
        except EOFError:
            # Arrêt de la boucle lors de la fin du flux d'entrée
            break
        if x in B:
            # Si x est déjà présent en clé, incrémenter son compteur
            B[x] += 1
        else:
            # Sinon, initialiser le compteur à 1
            B[x] = 1
    return B


def print_sum_of_common_keys(A, B):
    """
    Affiche la somme des occurrences de chaque clé présente à la fois dans le dictionnaire A et B.
    Pour chaque clé commune, affiche la clé suivie de la somme des occurrences dans A et B.

    Args:
        A (dict): Dictionnaire contenant les compteurs de clés à partir de la première entrée.
        B (dict): Dictionnaire contenant les compteurs de clés à partir de la seconde entrée.
    """
    for key in A.keys():
        if key in B:
            # Affiche la clé ainsi que la somme des compteurs associés dans A et B
            print(key, A[key] + B[key])


# Utilisation des fonctions définies pour reproduire le comportement du script original
A = count_x_occurrences_dict_a()
B = count_x_occurrences_dict_b()
print_sum_of_common_keys(A, B)