import bisect  # Importe le module bisect pour travailler avec les fonctions de bissection sur des listes triées

while True:  # Démarre une boucle infinie, qui ne s'arrêtera que si une condition est remplie à l'intérieur
    # Lit une ligne de l'entrée utilisateur, la découpe selon les espaces et convertit chaque morceau en entier
    # Les valeurs lues sont stockées respectivement dans n et S
    n, S = map(int, raw_input().split())

    # Vérifie si la valeur lue pour n est égale à zéro, ce qui indique qu'il faut arrêter le programme
    if n == 0:
        break  # Sort de la boucle infinie, terminant le programme

    A = []  # Initialise une liste vide qui contiendra les n entiers fournis par l'utilisateur

    # Démarre une boucle pour lire exactement n entiers depuis l'entrée utilisateur
    for i in range(n):  # La variable i varie de 0 à n-1, incluant n éléments
        value = int(raw_input())  # Lit une ligne, la convertit en entier et la stocke dans value
        A.append(value)  # Ajoute la valeur lue à la fin de la liste A

    A.sort()  # Trie la liste A par ordre croissant. Le tri est fait sur place, modifiant A elle-même

    ans = 0  # Initialise la variable ans à 0 ; elle servira à accumuler la réponse finale

    # Démarre une boucle pour inspecter chaque élément de A à partir du second élément (indice 1 jusqu'à n-1)
    for i in range(1, n):
        # Calcule la valeur recherchée pour le couple courant : S - A[i]
        # Prend la sous-liste A[:i], qui contient tous les éléments avant l'indice i (non inclus)
        # bisect.bisect renvoie l'indice d'insertion de S-A[i] dans la sous-liste triée, c'est-à-dire le nombre
        # d'éléments <= S-A[i] dans A[:i], soit le nombre de paires (j, i) avec j < i et A[j] <= S-A[i]
        index = bisect.bisect(A[:i], S - A[i])
        # i représente le nombre total d'indices j possibles (< i), donc i - index est le nombre d'indices j où A[j] > S - A[i]
        # max(0, i - index) est utilisé pour éviter les valeurs négatives qui n'auraient pas de sens dans ce contexte
        pair_count = max(0, i - index)
        # Ajoute le nombre de paires valides trouvées pour i à la somme totale
        ans += pair_count

    # Affiche la valeur finale calculée après avoir examiné toutes les paires pour cette instance du problème
    print ans  # Affiche le résultat pour ce jeu de données d'entrée avant de demander le suivant