# Lecture des dimensions de la grille et du nombre de cases noires souhaité
number_of_rows, number_of_columns, required_black_cells = map(int, input().split())

# Lecture de la grille elle-même, chaque ligne étant une liste de caractères
grid = [list(input().strip()) for row_index in range(number_of_rows)]

# Initialisation du compteur de solutions valides
valid_configurations_count = 0

# Vecteur pour les lignes sélectionnées (utilisé pour générer les sous-ensembles)
selected_rows_vector = [0 for _ in range(number_of_rows)]

# Parcourir tous les sous-ensembles possibles de lignes
for row_subset_mask in range(2**number_of_rows):
    
    # Vecteur pour les colonnes sélectionnées
    selected_columns_vector = [0 for _ in range(number_of_columns)]
    
    # Ensemble des indices de lignes actuellement sélectionnées
    selected_rows_set = set(range(number_of_rows))
    for row_index in range(number_of_rows):
        if selected_rows_vector[row_index] == 0:
            selected_rows_set.discard(row_index)
    selected_rows_list = list(selected_rows_set)
    
    # Génération du prochain sous-ensemble de lignes via Gray code-like itération
    for row_index in range(number_of_rows):
        if selected_rows_vector[number_of_rows - row_index - 1] == 0:
            selected_rows_vector[number_of_rows - row_index - 1] = 1
            for reset_index in range(number_of_rows - row_index, number_of_rows):
                selected_rows_vector[reset_index] = 0
            break
    
    # Parcourir tous les sous-ensembles possibles de colonnes
    for column_subset_mask in range(2**number_of_columns):
        
        # Ensemble des indices de colonnes actuellement sélectionnées
        selected_columns_set = set(range(number_of_columns))
        for column_index in range(number_of_columns):
            if selected_columns_vector[column_index] == 0:
                selected_columns_set.discard(column_index)
        selected_columns_list = list(selected_columns_set)
        
        # Génération du prochain sous-ensemble de colonnes
        for column_index in range(number_of_columns):
            if selected_columns_vector[number_of_columns - column_index - 1] == 0:
                selected_columns_vector[number_of_columns - column_index - 1] = 1
                for reset_index in range(number_of_columns - column_index, number_of_columns):
                    selected_columns_vector[reset_index] = 0
                break
        
        # Compter le nombre de cases noires restantes après suppression
        current_black_cells_count = 0
        for row in selected_rows_list:
            for column in selected_columns_list:
                if grid[row][column] == '#':
                    current_black_cells_count += 1
        
        # Si ce sous-ensemble laisse exactement le bon nombre de cases noires
        if current_black_cells_count == required_black_cells:
            valid_configurations_count += 1

# Affichage du nombre total de configurations valides
print(valid_configurations_count)