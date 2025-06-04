number_of_rows, number_of_columns, required_hash_count = map(int, input().split())

grid_rows = [input() for _ in range(number_of_rows)]

matching_configurations_count = 0

current_hash_count = 0

for row_mask in range(2 ** number_of_rows):

    for column_mask in range(2 ** number_of_columns):

        for row_index in range(number_of_rows):

            for column_index in range(number_of_columns):

                is_cell_selected = ((row_mask >> row_index) & 1) and ((column_mask >> column_index) & 1)

                if grid_rows[row_index][column_index] == "#" and is_cell_selected:

                    current_hash_count += 1

        if current_hash_count == required_hash_count:

            matching_configurations_count += 1

        current_hash_count = 0

print(matching_configurations_count)