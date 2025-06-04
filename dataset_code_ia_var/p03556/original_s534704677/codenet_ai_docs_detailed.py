def find_largest_square(N):
    """
    Trouve le plus grand carré parfait inférieur ou égal à N.

    Args:
        N (int): La borne supérieure pour rechercher les carrés parfaits.

    Returns:
        int: Le plus grand carré parfait inférieur ou égal à N.
    """
    # Initialise la variable de résultat à 0 (carré parfait minimum).
    ans = 0

    # Parcourt les entiers de 0 jusqu'à N inclus.
    for i in range(N + 1):
        # Vérifie si le carré de i dépasse N.
        if i * i > N:
            # Si c'est le cas, on termine la boucle car les carrés suivants seront encore plus grands.
            break
        # Stocke le carré de i comme le plus grand carré parfait trouvé jusqu'à présent.
        ans = i * i

    # Retourne la valeur du plus grand carré parfait trouvée.
    return ans

# Lecture de l'entrée utilisateur avec conversion en entier.
N = int(input())

# Appelle la fonction pour trouver le plus grand carré parfait et l'affiche.
print(find_largest_square(N))