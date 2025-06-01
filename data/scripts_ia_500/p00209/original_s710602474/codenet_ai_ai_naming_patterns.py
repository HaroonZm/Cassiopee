def execute_main(input_piece, rotation_count):
    for top_row in range(grid_size - piece_size + 1):
        for left_col in range(grid_size - piece_size + 1):
            if check_match(input_piece, top_row, left_col):
                break
    if rotation_count != 4:
        rotate_and_recurse(input_piece, rotation_count)
    else:
        if answer_coordinate:
            print answer_coordinate[0], answer_coordinate[1]
        else:
            print 'NA'

def check_match(input_piece, top_row, left_col):
    global answer_coordinate
    first_match_pos = None
    for piece_row in range(piece_size):
        for piece_col in range(piece_size):
            if input_piece[piece_row][piece_col] != '-1':
                if input_piece[piece_row][piece_col] == grid[top_row + piece_row][left_col + piece_col]:
                    if first_match_pos is None:
                        first_match_pos = (int(left_col + piece_col + 1), int(top_row + piece_row + 1))
                        if answer_coordinate:
                            if first_match_pos[1] > answer_coordinate[1]:
                                return
                            elif first_match_pos[1] == answer_coordinate[1]:
                                if first_match_pos[0] > answer_coordinate[0]:
                                    return
                else:
                    return
    else:
        answer_coordinate = first_match_pos
        return True

def rotate_and_recurse(input_piece, rotation_count):
    rotated_piece = []
    for col in range(piece_size):
        column_elements = []
        for row in range(piece_size):
            column_elements.append(input_piece[row][col])
        column_elements.reverse()
        rotated_piece.append(column_elements)
    execute_main(rotated_piece, rotation_count + 1)

while True:
    grid_size, piece_size = map(int, raw_input().split())
    if grid_size == 0 and piece_size == 0:
        break
    grid = [raw_input().split() for _ in range(grid_size)]
    piece = [raw_input().split() for _ in range(piece_size)]
    answer_coordinate = None
    execute_main(piece, 1)