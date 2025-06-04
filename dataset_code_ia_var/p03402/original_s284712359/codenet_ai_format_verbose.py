number_of_black_areas, number_of_white_areas = map(int, input().split())

grid_height = 100
grid_width = 100

# Initialisation de la grille :
# Première moitié (lignes 0-49) en blanc ('.'), deuxième moitié (lignes 50-99) en noir ('#')
grid_cells = []

for row_index in range(50):
    grid_cells.append(['.'] * grid_width)

for row_index in range(50):
    grid_cells.append(['#'] * grid_width)

# Dessiner les régions noires séparées dans la moitié supérieure
for black_area_index in range(number_of_white_areas - 1):
    row_in_block, column_in_block = divmod(black_area_index, 50)
    target_row = 2 * row_in_block
    target_column = 2 * column_in_block
    grid_cells[target_row][target_column] = '#'

# Dessiner les régions blanches séparées dans la moitié inférieure
for white_area_index in range(number_of_black_areas - 1):
    row_in_block, column_in_block = divmod(white_area_index, 50)
    target_row = 2 * row_in_block + 51  # Commencer juste après la séparation
    target_column = 2 * column_in_block
    grid_cells[target_row][target_column] = '.'

# Affichage de la grille résultat
print(grid_height, grid_width)

for row in range(grid_height):
    print(''.join(grid_cells[row]))