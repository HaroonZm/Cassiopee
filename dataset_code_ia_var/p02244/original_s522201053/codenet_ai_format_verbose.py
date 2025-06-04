from sys import stdin

BOARD_SIZE = 8
UNASSIGNED = -1
ASSIGNED = 1

row_queen_positions = [UNASSIGNED] * BOARD_SIZE
column_status = [UNASSIGNED] * BOARD_SIZE
positive_diagonal_status = [UNASSIGNED] * (2 * BOARD_SIZE - 1)
negative_diagonal_status = [UNASSIGNED] * (2 * BOARD_SIZE - 1)

mandatory_queen_positions = [[False] * BOARD_SIZE for _ in range(BOARD_SIZE)]

number_of_mandatory_positions = int(stdin.readline())

for _ in range(number_of_mandatory_positions):
    input_row, input_column = map(int, stdin.readline().split())
    mandatory_queen_positions[input_row][input_column] = True

def print_chessboard():
    for current_row in range(BOARD_SIZE):
        for current_column in range(BOARD_SIZE):
            if mandatory_queen_positions[current_row][current_column] and row_queen_positions[current_row] != current_column:
                return
    for current_row in range(BOARD_SIZE):
        for current_column in range(BOARD_SIZE):
            if row_queen_positions[current_row] == current_column:
                print("Q", end="")
            else:
                print(".", end="")
        print("")

def solve_n_queens(row_index):
    if row_index == BOARD_SIZE:
        print_chessboard()
        return

    for column_index in range(BOARD_SIZE):
        if (column_status[column_index] == ASSIGNED or
            positive_diagonal_status[row_index + column_index] == ASSIGNED or
            negative_diagonal_status[row_index - column_index + BOARD_SIZE - 1] == ASSIGNED):
            continue

        row_queen_positions[row_index] = column_index
        column_status[column_index] = positive_diagonal_status[row_index + column_index] = negative_diagonal_status[row_index - column_index + BOARD_SIZE - 1] = ASSIGNED

        solve_n_queens(row_index + 1)

        row_queen_positions[row_index] = column_status[column_index] = positive_diagonal_status[row_index + column_index] = negative_diagonal_status[row_index - column_index + BOARD_SIZE - 1] = UNASSIGNED

solve_n_queens(0)