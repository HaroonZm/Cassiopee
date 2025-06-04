from itertools import permutations
from copy import deepcopy

EMPTY_CELL = "."
QUEEN_CELL = "Q"
BOARD_SIZE = 8

chess_board = [[EMPTY_CELL] * BOARD_SIZE for _ in range(BOARD_SIZE)]

number_of_fixed_queens = int(input())

fixed_queens_positions = [
    list(map(int, input().split())) for _ in range(number_of_fixed_queens)
]

def is_safe_to_place_queen(row_index, column_index, current_board):
    # Check rows and columns for another queen
    for idx in range(BOARD_SIZE):
        if current_board[idx][column_index] == QUEEN_CELL:
            return False
        if current_board[row_index][idx] == QUEEN_CELL:
            return False
    # Check diagonals for another queen
    for offset in range(-BOARD_SIZE, BOARD_SIZE):
        new_row = row_index + offset
        new_col_main_diagonal = column_index + offset
        new_col_anti_diagonal = column_index - offset
        if 0 <= new_row < BOARD_SIZE and 0 <= new_col_main_diagonal < BOARD_SIZE:
            if current_board[new_row][new_col_main_diagonal] == QUEEN_CELL:
                return False
        if 0 <= new_row < BOARD_SIZE and 0 <= new_col_anti_diagonal < BOARD_SIZE:
            if current_board[new_row][new_col_anti_diagonal] == QUEEN_CELL:
                return False
    return True

def solve_eight_queens_with_fixed_positions():
    for queen_columns_permutation in permutations(range(BOARD_SIZE)):
        candidate_board = deepcopy(chess_board)

        for board_row_index, board_column_index in enumerate(queen_columns_permutation):
            candidate_board[board_row_index][board_column_index] = QUEEN_CELL

        if not all(
            candidate_board[fixed_queen_row][fixed_queen_col] == QUEEN_CELL
            for fixed_queen_row, fixed_queen_col in fixed_queens_positions
        ):
            continue

        placement_is_valid = True
        for board_row_index, board_column_index in enumerate(queen_columns_permutation):
            candidate_board[board_row_index][board_column_index] = EMPTY_CELL

            if not is_safe_to_place_queen(
                board_row_index, board_column_index, candidate_board
            ):
                placement_is_valid = False
                break

            candidate_board[board_row_index][board_column_index] = QUEEN_CELL

        if placement_is_valid:
            return candidate_board

solved_chess_board = solve_eight_queens_with_fixed_positions()

for row in solved_chess_board:
    print(
        "".join(
            QUEEN_CELL if cell == QUEEN_CELL else EMPTY_CELL
            for cell in row
        )
    )