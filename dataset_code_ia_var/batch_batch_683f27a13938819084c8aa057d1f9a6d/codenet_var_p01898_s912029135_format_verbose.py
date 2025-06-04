number_of_rows, number_of_columns = map(int, input().split())

# Construction de la grille avec des bordures pour éviter les débordements d'indices
grid = [list("#" * (number_of_columns + 2))]

for row_index in range(number_of_rows):
    input_row = input()
    # Encadrement de chaque ligne avec des '#'
    grid.append(list("#" + input_row + "#"))

grid.append(list("#" * (number_of_columns + 2)))

# Ensemble des directions à vérifier autour d'une cellule (8 directions)
adjacent_directions = (
    (1, 0),    # droite
    (1, -1),   # haut droite
    (0, -1),   # haut
    (-1, -1),  # haut gauche
    (-1, 0),   # gauche
    (-1, 1),   # bas gauche
    (0, 1),    # bas
    (1, 1)     # bas droite
)

# Parcours de la grille pour appliquer les règles
for current_row in range(1, number_of_rows + 1):

    for current_column in range(1, number_of_columns + 1):

        if grid[current_row][current_column] == "x":

            for delta_column, delta_row in adjacent_directions:

                neighbor_row = current_row + delta_row
                neighbor_column = current_column + delta_column

                if grid[neighbor_row][neighbor_column] == "-":
                    grid[neighbor_row][neighbor_column] = "#"

        if grid[current_row][current_column] == "o":

            if grid[current_row][current_column - 1] == "-":
                grid[current_row][current_column - 1] = "#"

            if grid[current_row][current_column + 1] == "-":
                grid[current_row][current_column + 1] = "#"

# Nettoyage de la première ligne intérieure de la grille
for column_in_first_row in range(1, number_of_columns + 1):

    if grid[1][column_in_first_row] == "-":
        grid[1][column_in_first_row] = "#"

# Comptage des cellules restantes contenant le caractère '-'
remaining_minus_count = sum([row.count("-") for row in grid])

print(remaining_minus_count)