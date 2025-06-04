import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def solve():
    """
    Lit une description d'une grille, simule une série de pliages et
    répond à des questions sur la valeur des cellules après opérations.

    Entrée formatée comme suit depuis stdin :
      - Première ligne : quatre entiers (largeur, hauteur, nombre de pliages, nombre de questions)
      - Suivent 't' lignes décrivant les pliages (ope, axis)
      - Suivent 'p' lignes décrivant les requêtes (px, py)

    Affiche une réponse pour chaque requête, correspondant à la valeur dans la
    cellule de la grille finale après tous les pliages.

    Arrête le programme si la largeur (grid_wid) lue est 0.
    """
    grid_wid, grid_hei, t, p = map(int, input().split())
    if grid_wid == 0:
        exit()

    # Initialisation de la grille : chaque cellule vaut 1
    grid = [[1] * grid_wid for _ in range(grid_hei)]

    # Lecture des instructions de pliage : chaque pliage est (ope, axis)
    fold = [list(map(int, input().split())) for _ in range(t)]

    # Lecture des positions des pins (questions à répondre)
    pin = [list(map(int, input().split())) for _ in range(p)]

    # Définition des bornes du sous-rectangle actif de la grille
    # [L, R): abscisses (colonnes), [B, H): ordonnées (lignes)
    L = 0
    R = grid_wid
    B = 0
    H = grid_hei

    # Exécution des pliages successifs
    for ope, axis in fold:
        if ope == 1:  # Pliage horizontal (le long d'une colonne)
            current_width = R - L
            if axis > current_width / 2:
                # Pliage du côté droit, ensuite on inverse la grille horizontalement
                alter_axis = current_width - axis
                for i in range(alter_axis):
                    for j in range(grid_hei):
                        # Addition des couches superposées après le pliage
                        grid[j][axis - i - 1 + L] += grid[j][axis + i + L]
                        grid[j][axis + i + L] = 0
                # Inversion des colonnes (miroir horizontal)
                for j in range(grid_hei):
                    grid[j] = list(reversed(grid[j]))
                # Mise à jour des indices de la sous-grille étudiée
                L, R = grid_wid - R + alter_axis, grid_wid - L
            else:
                # Pliage du côté gauche, sans inversion
                for i in range(axis):
                    for j in range(grid_hei):
                        grid[j][axis + i + L] += grid[j][axis - i - 1 + L]
                        grid[j][axis - i - 1 + L] = 0
                L += axis

        if ope == 2:  # Pliage vertical (le long d'une ligne)
            current_hei = H - B
            if axis > current_hei / 2:
                # Pliage par le bas, puis inverse la grille verticalement
                alter_axis = current_hei - axis
                for i in range(alter_axis):
                    for j in range(grid_wid):
                        grid[axis - i - 1 + B][j] += grid[axis + i + B][j]
                        grid[axis + i + B][j] = 0
                # Inversion des lignes (miroir vertical)
                grid = list(reversed(grid))
                # Mise à jour des indices de la sous-grille étudiée
                B, H = grid_hei - H + alter_axis, grid_hei - B
            else:
                # Pliage du haut, sans inversion
                for i in range(axis):
                    for j in range(grid_wid):
                        grid[axis + i + B][j] += grid[axis - i - 1 + B][j]
                        grid[axis - i - 1 + B][j] = 0
                B += axis

    # Traitement et affichage des réponses pour chaque question
    for px, py in pin:
        # Les indices de la grille sont décalés d'après les limites de la zone active
        ans = grid[B + py][L + px]
        print(ans)

while True:
    solve()