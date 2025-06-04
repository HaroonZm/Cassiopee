# Lecture des dimensions de la salle
number_of_rows, number_of_columns = map(int, input().split())

# Lecture de chaque rangée de sièges comme une liste de caractères
seat_layout = [list(input()) for current_row_index in range(number_of_rows)]

# Création d'une ligne factice de zéros pour simuler les bords de la salle
border_row = ["0" for border_column_index in range(number_of_columns + 2)]

# Ajout de zéros en début et en fin de chaque rangée pour gérer les bords
for row_index in range(number_of_rows):
    seat_layout[row_index].insert(0, "0")
    seat_layout[row_index].append("0")

# Insertion des lignes factices en haut et en bas de la salle
seat_layout.insert(0, border_row)
seat_layout.append(border_row)

# Parcours de chaque siège (hors bordures artificielles)
for seat_row_index in range(1, number_of_rows + 1):
    for seat_column_index in range(1, number_of_columns + 1):

        # Si le siège est occupé par une personne (symbole 'o')
        if seat_layout[seat_row_index][seat_column_index] == "o":
            # Bloquer le siège immédiatement à gauche s'il est libre
            if seat_layout[seat_row_index][seat_column_index - 1] == "-":
                seat_layout[seat_row_index][seat_column_index - 1] = "0"
            # Bloquer le siège immédiatement à droite s'il est libre
            if seat_layout[seat_row_index][seat_column_index + 1] == "-":
                seat_layout[seat_row_index][seat_column_index + 1] = "0"

        # Si le siège est interdit (symbole 'x'), bloquer la zone 3x3 autour
        elif seat_layout[seat_row_index][seat_column_index] == "x":
            for delta_row in range(3):
                for delta_column in range(3):
                    adjacent_row = seat_row_index - 1 + delta_row
                    adjacent_column = seat_column_index - 1 + delta_column
                    if seat_layout[adjacent_row][adjacent_column] == "-":
                        seat_layout[adjacent_row][adjacent_column] = "0"

# Bloquer tous les sièges libres de la première vraie rangée (au contact du bord factice du haut)
for first_row_column_index in range(number_of_columns + 1):
    if seat_layout[1][first_row_column_index] == "-":
        seat_layout[1][first_row_column_index] = "0"

# Compter les sièges restants libres ("-")
available_seat_count = 0
for current_row in seat_layout:
    for seat_status in current_row:
        if seat_status == "-":
            available_seat_count += 1

# Affichage du résultat
print(available_seat_count)