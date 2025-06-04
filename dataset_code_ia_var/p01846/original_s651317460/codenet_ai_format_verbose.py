continue_program_loop = True

while continue_program_loop:

    fen_notation_input = input()

    if fen_notation_input == '#':
        break

    fen_rows = fen_notation_input.split('/')

    chessboard_rows = []

    for row_string in fen_rows:
        expanded_row = ''
        for character in row_string:
            if character == 'b':
                expanded_row += 'b'
            else:
                expanded_row += '.' * int(character)
        chessboard_rows.append(list(expanded_row))

    original_row_index, original_col_index, new_row_index, new_col_index = map(int, input().split())

    # Remove the bishop from original position
    chessboard_rows[original_row_index - 1][original_col_index - 1] = '.'

    # Place the bishop at new position
    chessboard_rows[new_row_index - 1][new_col_index - 1] = 'b'

    fen_row_outputs = []
    for row in chessboard_rows:
        row_string = ''.join(row)
        fen_row = ''
        empty_count = 0
        for square in row_string:
            if square == '.':
                empty_count += 1
            else:
                if empty_count > 0:
                    fen_row += str(empty_count)
                    empty_count = 0
                fen_row += 'b'
        if empty_count > 0:
            fen_row += str(empty_count)
        fen_row_outputs.append(fen_row)

    print('/'.join(fen_row_outputs))