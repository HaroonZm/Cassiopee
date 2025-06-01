def solve():
    """
    Résout un problème basé sur une grille hexagonale étendue par des zéros autour.

    Le programme lit une largeur W et une hauteur H, puis lit H lignes
    représentant une grille de 0 et 1. Cette grille est entourée d'une bordure
    de zéros (pour faciliter la gestion des bords).

    Il effectue ensuite une exploration en largeur (BFS) depuis la case (0,0)
    située dans cette bordure externe, en utilisant une file deque.
    Le but est de parcourir toutes les cases "externes" accessibles.

    Pour chaque case visitée lors de l'exploration, la somme des valeurs des cases
    voisines dans la grille initiale est ajoutée au résultat.

    Les voisins sont différents selon la parité de la coordonnée y,
    ce qui correspond aux coordonnées hexagonales décalées.

    Enfin, il affiche la somme totale calculée.

    Entrées :
        - W (int) : largeur de la grille initiale sans bordure
        - H (int) : hauteur de la grille initiale sans bordure
        - H lignes contenant chacune W valeurs entières (0 ou 1)

    Sortie :
        - Un entier, la somme calculée en parcourant la grille étendue.
    """
    from collections import deque
    from copy import deepcopy

    # Lecture des dimensions de la grille
    W, H = map(int, input().split())

    # Lecture de la grille avec ajout d'une bordure de 0 tout autour
    # Chaque ligne est entourée d'un 0 à gauche et à droite,
    # et on ajoute une ligne de 0 au-dessus et en-dessous.
    a = [[0]*(W+2)] + [list(map(int, ("0 "+input()+" 0").split())) for _ in range(H)] + [[0]*(W+2)]

    result = 0  # Initialisation du compteur de résultat

    # Création d'une copie de la grille servant à suivre les cases visitées
    visited = deepcopy(a)

    # Initialisation d'une file double-ended queue pour BFS avec la case (0, 0)
    dq = deque([(0, 0)])

    # Références rapides aux méthodes d'ajout et de suppression de la deque
    append, popleft = dq.append, dq.popleft

    # Parcours en largeur tant que la file n'est pas vide
    while dq:
        x, y = popleft()
        # Définition des voisins selon la parité de y (coordonnées hexagonales)
        neighbour = [(-1, 0), (1, 0)]  # voisins gauche et droite toujours présents
        if y % 2 == 0:
            # Pour lignes paires, voisins haut-gauche, haut, bas-gauche, bas
            neighbour += [(-1, -1), (0, -1), (-1, 1), (0, 1)]
        else:
            # Pour lignes impaires, voisins haut, haut-droite, bas, bas-droite
            neighbour += [(0, -1), (1, -1), (0, 1), (1, 1)]

        # Ajout au résultat des valeurs des cases voisines dans la grille
        for dx, dy in neighbour:
            nx, ny = x + dx, y + dy
            # Vérification des limites de la grille étendue
            if 0 <= nx < W + 2 and 0 <= ny < H + 2:
                result += a[ny][nx]

        # Exploration des cases voisines accessibles non encore visitées
        for dx, dy in neighbour:
            nx, ny = x + dx, y + dy
            # Vérification que la case est dans la grille et non visitée
            if 0 <= nx < W + 2 and 0 <= ny < H + 2 and visited[ny][nx] == 0:
                # Marquage de la case comme visitée
                visited[ny][nx] = 1
                # Ajout de la case à la file pour exploration ultérieure
                append((nx, ny))

    # Affichage du résultat final
    print(result)


if __name__ == "__main__":
    solve()