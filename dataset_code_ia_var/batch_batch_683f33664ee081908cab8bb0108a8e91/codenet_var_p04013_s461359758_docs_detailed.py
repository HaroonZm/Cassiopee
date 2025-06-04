def count_combinations_with_average():
    """
    Lit les entrées standard, puis calcule le nombre de manières de choisir des sous-ensembles non vides
    du tableau d'entiers donnés tels que la moyenne arithmétique de leurs éléments soit égale à une valeur cible 'a'.
    Affiche le résultat calculé.
    Entrée:
        - n (int): le nombre d'éléments dans la liste.
        - a (int): la moyenne cible recherchée.
        - x (list of int): une liste de n entiers représentant les éléments disponibles.
    Sortie:
        - (int): le nombre de sous-ensembles non vides dont la moyenne vaut exactement 'a'.
    """
    # Lecture des entrées : n = nombre d'éléments, a = moyenne cible
    n, a = map(int, input().split())
    # Lecture de la liste des éléments disponibles
    x = list(map(int, input().split()))

    # Initialisation du tableau dynamique 3D :
    # t[i][j][k] représente le nombre de façons de choisir j éléments parmi les i premiers
    # tels que leur somme soit exactement k
    # Dimensions:
    #   - Pour chaque nombre d'éléments pris i (de 0 à n)
    #   - Pour chaque taille de sous-ensemble j (de 0 à i+1)
    #   - Pour chaque somme k possible (0 à 50*j, car chaque x[i] <= 50)
    t = [[[0] * (50 * (j + 1) + 1) for j in range(i + 2)] for i in range(n + 1)]

    # Initialisation de la table : il existe exactement 1 façon de choisir 0 éléments (sous-ensemble vide) avec une somme de 0
    t[0][0][0] = 1

    # Remplissage du tableau dynamique
    for i in range(1, n + 1):
        # Pour chaque taille possible de sous-ensemble (de 0 à i inclus)
        for j in range(i + 1):
            # Pour chaque somme possible jusqu'à la somme maximale pour j éléments (car max(x[i-1])=50)
            for k in range(50 * j + 1):
                if j >= 1 and k >= x[i - 1]:
                    # Deux options :
                    # 1. Prendre x[i-1] : on ajoute t[i-1][j-1][k-x[i-1]]
                    # 2. Ne pas prendre x[i-1] : on ajoute t[i-1][j][k]
                    t[i][j][k] = t[i - 1][j - 1][k - x[i - 1]] + t[i - 1][j][k]
                else:
                    # On ne peut que ne pas prendre x[i-1] dans ce cas
                    t[i][j][k] = t[i - 1][j][k]

    # Calcul du résultat final
    ans = 0
    # Pour chaque taille de sous-ensemble non vide i (de 1 à n)
    # On ajoute le nombre de façons de choisir i éléments dont la somme vaut exactement i*a (donc moyenne == a)
    for i in range(1, n + 1):
        ans += t[n][i][i * a]

    # Affichage du résultat
    print(ans)

# Appel de la fonction principale
count_combinations_with_average()