from itertools import combinations
import numpy as np

# Lecture des dimensions de la grille et du nombre de cases visées
grid_height, grid_width, target_black_cells = map(int, input().split())

# Lecture de la grille de caractères
grid_cells = [list(input()) for row_index in range(grid_height)]

# Création d'une matrice binaire pour représenter les cases noires
black_cell_matrix = np.zeros((grid_height, grid_width), dtype=int)

# Comptage des cases noires dans la grille et stockage dans la matrice
for row_index in range(grid_height):
    for col_index in range(grid_width):
        if grid_cells[row_index][col_index] == "#":
            black_cell_matrix[row_index][col_index] = 1

# Calcul du nombre total de cases noires dans la grille
total_black_cells = np.sum(black_cell_matrix)

# Initialisation du compteur de combinaisons valides
number_of_valid_combinations = 0

# Parcours de toutes les combinaisons de lignes à masquer
for number_of_rows_to_hide in range(grid_height + 1):
    for rows_to_hide_indices in combinations(range(grid_height), number_of_rows_to_hide):

        # Parcours de toutes les combinaisons de colonnes à masquer
        for number_of_columns_to_hide in range(grid_width + 1):
            for columns_to_hide_indices in combinations(range(grid_width), number_of_columns_to_hide):

                # Calcul du nombre de cases noires masquées par le masquage choisi
                black_cells_hidden = 0

                # Ajout des cases noires masquées dans les lignes sélectionnées
                for row_index in rows_to_hide_indices:
                    for col_index in range(grid_width):
                        black_cells_hidden += black_cell_matrix[row_index][col_index]
                
                # Ajout des cases noires masquées dans les colonnes sélectionnées
                for col_index in columns_to_hide_indices:
                    for row_index in range(grid_height):
                        black_cells_hidden += black_cell_matrix[row_index][col_index]
                
                # Correction du double comptage des cases situées à l’intersection des lignes et colonnes masquées
                for row_index in rows_to_hide_indices:
                    for col_index in columns_to_hide_indices:
                        black_cells_hidden -= black_cell_matrix[row_index][col_index]
                
                # Si le nombre de cases noires restantes correspond à la cible, incrémenter le compteur
                if target_black_cells == total_black_cells - black_cells_hidden:
                    number_of_valid_combinations += 1

# Affichage du résultat final
print(number_of_valid_combinations)