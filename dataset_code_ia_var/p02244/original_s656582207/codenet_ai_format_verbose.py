NUMBER_OF_QUEENS = 8  # Number of queens

number_of_preplaced_queens = int(input())

queen_positions_per_row = [-1 for unused_index in range(NUMBER_OF_QUEENS)]

occupied_columns = [0 for unused_index in range(NUMBER_OF_QUEENS)]  # 0: free, 1: occupied
occupied_positive_diagonals = [0 for unused_index in range(2 * NUMBER_OF_QUEENS - 1)]  # "/" diagonals
occupied_negative_diagonals = [0 for unused_index in range(2 * NUMBER_OF_QUEENS - 1)]  # "\" diagonals

def place_queens_in_all_rows(current_row_index):

    if current_row_index == NUMBER_OF_QUEENS:
        # All queens placed successfully
        return True

    elif queen_positions_per_row[current_row_index] != -1:
        # This row already has a pre-placed queen
        if place_queens_in_all_rows(current_row_index + 1):
            return True
        else:
            return False

    else:
        for candidate_column_index in range(NUMBER_OF_QUEENS):

            if (occupied_columns[candidate_column_index] == 1 or
                occupied_positive_diagonals[current_row_index + candidate_column_index] == 1 or
                occupied_negative_diagonals[current_row_index - candidate_column_index + NUMBER_OF_QUEENS - 1] == 1):
                # Conflict detected, skip this position
                continue

            queen_positions_per_row[current_row_index] = candidate_column_index
            occupied_columns[candidate_column_index] = 1
            occupied_positive_diagonals[current_row_index + candidate_column_index] = 1
            occupied_negative_diagonals[current_row_index - candidate_column_index + NUMBER_OF_QUEENS - 1] = 1

            if place_queens_in_all_rows(current_row_index + 1):
                return True
            else:
                # Backtrack, unmark the column, diagonals, and remove queen
                queen_positions_per_row[current_row_index] = -1
                occupied_columns[candidate_column_index] = 0
                occupied_positive_diagonals[current_row_index + candidate_column_index] = 0
                occupied_negative_diagonals[current_row_index - candidate_column_index + NUMBER_OF_QUEENS - 1] = 0

        return False

def print_queen_positions_board():
    for row_index in range(NUMBER_OF_QUEENS):
        current_row_characters = ['.' for unused_index in range(NUMBER_OF_QUEENS)]
        queen_column_in_row = queen_positions_per_row[row_index]
        current_row_characters[queen_column_in_row] = 'Q'
        print(''.join(current_row_characters))

for preplaced_queen_index in range(number_of_preplaced_queens):
    preplaced_row, preplaced_column = map(int, input().split())
    queen_positions_per_row[preplaced_row] = preplaced_column
    occupied_columns[preplaced_column] = 1
    occupied_positive_diagonals[preplaced_row + preplaced_column] = 1
    occupied_negative_diagonals[preplaced_row - preplaced_column + NUMBER_OF_QUEENS - 1] = 1

place_queens_in_all_rows(0)
print_queen_positions_board()