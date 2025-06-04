def bublesort(arr, n):
    """
    Trie la liste 'arr' en utilisant l'algorithme de tri à bulles.
    Compte et retourne le nombre de permutations effectuées durant le tri.

    Paramètres :
        arr (list[int]): Liste d'entiers à trier.
        n (int): Nombre d'éléments dans la liste.

    Retourne :
        tuple: (nombre_de_permutations, liste_triee)
            nombre_de_permutations (int): Nombre d'échanges effectués pour trier la liste.
            liste_triee (list[int]): La liste triée en ordre croissant.
    """
    count = 0  # Initialise le compteur de permutations à zéro
    # On effectue 'n - 1' passes sur le tableau
    for j in range(n - 1):
        # Pour chaque passe, on compare les éléments adjacents de la fin vers le début
        for i in range(n - 1, 0, -1):
            # Si l'élément précédent est plus grand, on échange les deux
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]  # Echange des valeurs
                count += 1  # Incrémente le nombre de permutations
    return count, arr


# Lecture de l'entrée utilisateur :
# Demande à l'utilisateur de saisir le nombre d'éléments de la liste
a = int(input())
# Demande la saisie de la liste d'entiers, séparés par des espaces, et conversion en liste d'entiers
b = list(map(int, input().split()))

# Appel à la fonction de tri à bulles et récupération du nombre de permutations et de la liste triée
A, B = bublesort(b, a)

# Affichage des résultats :
# Imprime la liste triée sur une seule ligne, séparée par des espaces
print(*B)
# Imprime le nombre de permutations effectuées
print(A)