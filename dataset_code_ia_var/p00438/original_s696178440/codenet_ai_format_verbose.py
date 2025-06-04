import sys
import copy

def main():
    current_input_line = sys.stdin.readline()

    # Traiter chaque cas jusqu'à ce qu'une ligne "0 0" soit rencontrée
    while current_input_line.split() != ["0", "0"]:
        process_single_case(current_input_line)
        current_input_line = sys.stdin.readline()

def process_single_case(case_header_line):
    # Extraire la taille du champ
    field_dimensions = [int(dimension) for dimension in case_header_line.split()]

    # Lire le nombre d'obstacles
    number_of_restricted_cells = int(sys.stdin.readline())
    restricted_cells_positions = []

    # Lire les positions interdites et les stocker dans une liste
    for restricted_cell_index in range(number_of_restricted_cells):
        restricted_position_line = sys.stdin.readline()
        restricted_position = [int(coordinate) for coordinate in restricted_position_line.split()]
        restricted_cells_positions.append(restricted_position)

    # Calculer et afficher le nombre de chemins possibles
    print(
        compute_number_of_paths(field_dimensions, restricted_cells_positions)
    )

def compute_number_of_paths(field_dimensions, restricted_cells):
    number_of_columns = field_dimensions[0]
    number_of_rows = field_dimensions[1]

    path_counts_per_column = []

    for current_row in range(number_of_rows):
        for current_column in range(number_of_columns):

            current_position = [current_column + 1, current_row + 1]

            if current_row == 0:
                # Première ligne
                if current_position in restricted_cells:
                    path_counts_per_column.append(0)
                elif current_column == 0:
                    # Première case : seul un chemin existe si elle n'est pas interdite
                    path_counts_per_column.append(1)
                else:
                    path_counts_per_column.append(path_counts_per_column[current_column - 1])

            else:
                if current_position in restricted_cells:
                    path_counts_per_column[current_column] = 0
                elif current_column != 0:
                    path_counts_per_column[current_column] = (
                        path_counts_per_column[current_column - 1] + path_counts_per_column[current_column]
                    )
                # current_column == 0 et current_row > 0
                # pas besoin de changer la valeur car on ne peut venir que du haut

    return path_counts_per_column[len(path_counts_per_column) - 1]

if __name__ == "__main__":
    main()