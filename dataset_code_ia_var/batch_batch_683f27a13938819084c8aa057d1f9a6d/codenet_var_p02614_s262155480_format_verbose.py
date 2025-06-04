from itertools import product

number_of_rows, number_of_columns, number_of_target_hashes = map(int, input().split())

grid_rows = [input() for _ in range(number_of_rows)]

number_of_ways_to_achieve_target = 0

for row_mask in product([0, 1], repeat=number_of_rows):

    for column_mask in product([0, 1], repeat=number_of_columns):

        current_hash_count = 0

        for row_index in range(number_of_rows):

            for column_index in range(number_of_columns):

                is_row_selected = (row_mask[row_index] == 0)
                is_column_selected = (column_mask[column_index] == 0)
                is_cell_hash = (grid_rows[row_index][column_index] == '#')

                if is_row_selected and is_column_selected and is_cell_hash:
                    current_hash_count += 1

        if current_hash_count == number_of_target_hashes:
            number_of_ways_to_achieve_target += 1

print(number_of_ways_to_achieve_target)