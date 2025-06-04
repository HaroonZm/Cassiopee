# AOJ 1516: Nasty Boys
# Version à lisibilité maximisée avec des noms de variables explicites

row_mapping_for_letters = [0, 0, 0, 1, 1, 1, 2, 2, 2]
column_mapping_for_letters = [0, 1, 2, 0, 1, 2, 0, 1, 2]
ascii_code_for_A = ord('A')

for test_case_index in range(1000):

    character_sequence = list(input())

    current_index_in_sequence = 0

    current_row = row_mapping_for_letters[ord(character_sequence[current_index_in_sequence]) - ascii_code_for_A]
    current_column = column_mapping_for_letters[ord(character_sequence[current_index_in_sequence]) - ascii_code_for_A]

    current_index_in_sequence += 1

    path_is_valid = True

    while current_index_in_sequence < len(character_sequence) and path_is_valid:

        path_is_valid = False

        next_row = row_mapping_for_letters[ord(character_sequence[current_index_in_sequence]) - ascii_code_for_A]
        next_column = column_mapping_for_letters[ord(character_sequence[current_index_in_sequence]) - ascii_code_for_A]

        current_index_in_sequence += 1

        if next_row == current_row:
            if abs(next_column - current_column) == 1:
                path_is_valid = True
        elif next_column == current_column:
            if abs(next_row - current_row) == 1:
                path_is_valid = True

        current_row = next_row
        current_column = next_column

    if path_is_valid:
        print(*character_sequence, sep='')