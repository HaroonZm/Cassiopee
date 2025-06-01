def main_function(puzzle_piece, rotation_count):
    for vertical_index in range(grid_size - piece_size + 1):
        for horizontal_index in range(grid_size - piece_size + 1):
            if match_and_update_answer(puzzle_piece, vertical_index, horizontal_index):
                break
    if rotation_count != 4:
        rotate_and_process(puzzle_piece, rotation_count)
    else:
        if answer_coordinate:
            print answer_coordinate[0], answer_coordinate[1]
        else:
            print 'NA'

def match_and_update_answer(puzzle_piece, top_row, left_col):
    global answer_coordinate
    first_match_coordinate = None
    for piece_row in range(piece_size):
        for piece_col in range(piece_size):
            piece_value = puzzle_piece[piece_row][piece_col]
            if piece_value != '-1':
                if piece_value == grid[top_row + piece_row][left_col + piece_col]:
                    if first_match_coordinate is None:
                        first_match_coordinate = (left_col + piece_col + 1, top_row + piece_row + 1)
                else:
                    return
    else:
        if answer_coordinate is None:
            answer_coordinate = first_match_coordinate
        elif first_match_coordinate[1] < answer_coordinate[1]:
            answer_coordinate = first_match_coordinate
        elif first_match_coordinate[1] == answer_coordinate[1]:
            if first_match_coordinate[0] < answer_coordinate[0]:
                answer_coordinate = first_match_coordinate
        return True

def rotate_and_process(puzzle_piece, rotation_count):
    rotated_piece = []
    for col_index in range(piece_size):
        temp_list = []
        for row_index in range(piece_size):
            temp_list.append(puzzle_piece[row_index][col_index])
        else:
            temp_list.reverse()
            rotated_piece.append(temp_list)
    else:
        main_function(rotated_piece, rotation_count + 1)

while True:
    grid_size, piece_size = map(int, raw_input().split())
    if grid_size == 0 and piece_size == 0:
        break
    grid = [raw_input().split() for _ in range(grid_size)]
    puzzle_piece = [raw_input().split() for _ in range(piece_size)]
    answer_coordinate = None
    main_function(puzzle_piece, 1)