import itertools

queen_positions_by_row = [-1] * 8

number_of_pre_placed_queens = int(input())

rows_with_pre_placed_queens = []

for _ in range(number_of_pre_placed_queens):
    pre_placed_row, pre_placed_column = list(map(int, input().split()))
    rows_with_pre_placed_queens.append(pre_placed_row)
    queen_positions_by_row[pre_placed_row] = pre_placed_column

def are_queen_positions_valid_for_rows(number_of_rows_checked):
    for checked_row in range(number_of_rows_checked):
        if is_conflict_with_existing_queens(queen_positions_by_row[checked_row], checked_row):
            return False
    return True

def is_conflict_with_existing_queens(test_column, test_row):
    for existing_row in range(test_row):
        existing_column = queen_positions_by_row[existing_row]
        if (existing_column - existing_row == test_column - test_row) or (existing_column + existing_row == test_column + test_row):
            return True
    return False

def display_chessboard_and_exit():
    queen_positions_as_pairs = []
    for row_index in range(8):
        queen_positions_as_pairs.append([row_index, queen_positions_by_row[row_index]])
    for row in range(8):
        for column in range(8):
            if [row, column] in queen_positions_as_pairs:
                print("Q", end="")
            else:
                print(".", end="")
        print()
    exit()

def place_queens_recursively(total_number_of_rows, current_row):
    if current_row == total_number_of_rows:
        if are_queen_positions_valid_for_rows(8):
            display_chessboard_and_exit()
    else:
        if current_row in rows_with_pre_placed_queens:
            place_queens_recursively(total_number_of_rows, current_row + 1)
        else:
            for proposed_column in range(total_number_of_rows):
                if proposed_column not in queen_positions_by_row:
                    queen_positions_by_row[current_row] = proposed_column
                    place_queens_recursively(total_number_of_rows, current_row + 1)
                    for reset_row in range(current_row + 1, 8):
                        if reset_row not in rows_with_pre_placed_queens:
                            queen_positions_by_row[reset_row] = -1

place_queens_recursively(8, 0)