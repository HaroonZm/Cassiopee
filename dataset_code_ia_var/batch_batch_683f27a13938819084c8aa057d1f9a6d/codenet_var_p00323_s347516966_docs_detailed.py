def process_and_print():
    """
    Lit un nombre n, puis lit n paires d'entiers depuis l'entrée.
    Pour chaque paire, calcule la somme, incrémente un compteur dans une liste.
    Ensuite, combine les éléments consécutifs de la liste, gérant les retenues (comme une addition binaire).
    Imprime chaque position où il reste un 1 à la fin du processus, suivie du nombre 0.
    """
    N = 200020  # Taille maximale pour couvrir toutes les sommes possibles
    a = [0] * N  # Liste pour stocker les compteurs pour chaque somme (index)
    n = int(input())  # Nombre de paires à traiter

    # Pour chaque paire de l'entrée standard
    for _ in range(n):
        # Lit une ligne, la sépare en deux entiers, calcule la somme de la paire
        s = sum(map(int, input().split()))
        # Incrémente le compteur à l'indice correspondant à cette somme
        a[s] += 1

    # Parcourt tout le tableau sauf le dernier élément pour gérer la retenue
    for i in range(N - 1):
        # Ajoute la moitié entière de a[i] au suivant (transférant la retenue)
        a[i + 1] += a[i] // 2
        # Garde seulement le bit de poids faible (0 ou 1) à la position actuelle
        a[i] &= 1
        # Si le bit de poids faible est 1, imprime l'indice suivi de 0
        if a[i]:
            print(i, 0)

# Appel de la fonction principale
process_and_print()