def print_grid(grid):
    """
    Affiche la grille (matrice) de caractères ligne par ligne.

    Args:
        grid (list of list of str): La grille à afficher, chaque sous-liste représente une ligne.
    """
    for row in grid:
        for cell in row:
            print(cell, end="")
        print("")


def main():
    """
    Point d'entrée du programme.
    Le programme lit un nombre de cas, puis pour chaque cas, lit la taille d'une grille carrée.
    Il construit ensuite un motif en spirale avec le caractère '#' au sein de cette grille,
    puis affiche la grille pour chaque cas de test.
    """
    # Lire le nombre de cas de tests à traiter
    a = int(input())

    for j in range(a):
        # Lire la taille de la grille (n x n)
        n = int(input())

        # Initialiser une grille n x n remplie d'espaces
        grid = [[" " for _ in range(n)] for _ in range(n)]

        # Direction de déplacement : 0 = haut, 1 = droite, 2 = bas, 3 = gauche
        direction = 1  # On commence vers la droite

        # Remplir la première colonne de '#' pour initialiser la spirale
        for i in range(n):
            grid[i][0] = "#"

        # Position de départ (haut-gauche de la grille)
        x = 0  # colonne
        y = 0  # ligne

        # Générer la spirale dans la grille
        # On exécute n-1 "pas" (couches ou segments de la spirale)
        for m in range(n - 1):
            # Calculer la longueur du segment courant.
            # Diminue de 2 tous les deux segments pour former la spirale.
            segment_length = n - 1 - (m // 2) * 2

            # Tracer le segment courant dans la direction appropriée
            for i in range(segment_length):
                if direction == 0:      # Vers le haut
                    y -= 1
                elif direction == 1:    # Vers la droite
                    x += 1
                elif direction == 2:    # Vers le bas
                    y += 1
                elif direction == 3:    # Vers la gauche
                    x -= 1
                # Marquer la case courante comme faisant partie de la spirale
                grid[y][x] = "#"

            # Changer la direction (cycle dans l'ordre : haut, droite, bas, gauche)
            direction = (direction + 1) % 4

        # Afficher la grille générée pour ce cas de test
        print_grid(grid)

        # Afficher une ligne vide sauf après le dernier cas
        if j != a - 1:
            print("")


if __name__ == "__main__":
    main()