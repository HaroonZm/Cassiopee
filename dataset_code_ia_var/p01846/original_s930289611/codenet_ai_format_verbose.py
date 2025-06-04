while True:

    fen_notation_input = input()

    if fen_notation_input == '#':

        break

    source_row_index, source_col_index, dest_row_index, dest_col_index = map(lambda x: int(x) - 1, input().split())

    board_representation = []

    for row_index, row_string in enumerate(fen_notation_input.split('/')):

        board_representation.append([])

        for character in row_string:

            if character == 'b':

                board_representation[row_index].append('b')

            else:

                board_representation[row_index] += ['.'] * int(character)

    board_representation[source_row_index][source_col_index] = '.'

    board_representation[dest_row_index][dest_col_index] = 'b'

    fen_rows_after_move = []

    for row_cells in board_representation:

        fen_row_string = ''

        empty_cell_count = 0

        for cell_content in row_cells:

            if cell_content == 'b':

                if empty_cell_count > 0:

                    fen_row_string += str(empty_cell_count)

                empty_cell_count = 0

                fen_row_string += 'b'

            else:

                empty_cell_count += 1

        if empty_cell_count > 0:

            fen_row_string += str(empty_cell_count)

        fen_rows_after_move.append(fen_row_string)

    print('/'.join(fen_rows_after_move))