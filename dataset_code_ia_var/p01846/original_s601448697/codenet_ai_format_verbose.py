while True:

    fen_input_string = input()
    if fen_input_string == '#':
        break

    fen_rows_list = fen_input_string.split('/')

    source_row_index, source_column_index, destination_row_index, destination_column_index = map(int, input().split())

    source_row_index -= 1
    source_column_index -= 1
    destination_row_index -= 1
    destination_column_index -= 1

    expanded_grid_representation = ['' for _ in fen_rows_list]

    for row_index, fen_row in enumerate(fen_rows_list):

        for character in fen_row:
            if character == 'b':
                expanded_grid_representation[row_index] += 'b'
            else:
                expanded_grid_representation[row_index] += '.' * int(character)

    expanded_grid_representation[source_row_index] = (
        expanded_grid_representation[source_row_index][:source_column_index] +
        '.' +
        expanded_grid_representation[source_row_index][source_column_index + 1:]
    )

    expanded_grid_representation[destination_row_index] = (
        expanded_grid_representation[destination_row_index][:destination_column_index] +
        'b' +
        expanded_grid_representation[destination_row_index][destination_column_index + 1:]
    )

    compressed_row_list = []

    for expanded_row in expanded_grid_representation:

        compressed_row_representation = ''
        consecutive_empty_counter = 0

        for cell_character in expanded_row:

            if cell_character == 'b':
                if consecutive_empty_counter != 0:
                    compressed_row_representation += str(consecutive_empty_counter)
                    consecutive_empty_counter = 0
                compressed_row_representation += 'b'
            else:
                consecutive_empty_counter += 1

        if consecutive_empty_counter != 0:
            compressed_row_representation += str(consecutive_empty_counter)
            consecutive_empty_counter = 0

        compressed_row_list.append(compressed_row_representation)

    print('/'.join(compressed_row_list))