from itertools import permutations

number_of_preplaced_queens = int(input())

preplaced_queens_positions = [list(map(int, input().split())) for _ in range(number_of_preplaced_queens)]

all_columns = list(range(8))

all_possible_arrangements = list(permutations(all_columns, 8))

def is_valid_non_attacking(chessboard_columns):
    diagonal1 = list(chessboard_columns)
    diagonal2 = list(chessboard_columns)
    for row in range(len(chessboard_columns)):
        diagonal1[row] -= row
        diagonal2[row] += row
    for i, diag1 in enumerate(diagonal1[:-1]):
        if diag1 in diagonal1[i+1:]:
            return False
    for i, diag2 in enumerate(diagonal2[:-1]):
        if diag2 in diagonal2[i+1:]:
            return False
    return True

solution_arrangement = None

for arrangement in all_possible_arrangements:
    is_possible_arrangement = True
    for given_row, given_column in preplaced_queens_positions:
        if arrangement[given_row] != given_column:
            is_possible_arrangement = False
            break
    if is_possible_arrangement:
        if is_valid_non_attacking(arrangement):
            solution_arrangement = arrangement
            break

chessboard_display = [['.'] * 8 for _ in range(8)]

for row_index, queen_column in enumerate(solution_arrangement):
    chessboard_display[row_index][queen_column] = 'Q'
    print(''.join(chessboard_display[row_index]))