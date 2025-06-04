from bisect import bisect

while True:

    number_of_rows, number_of_columns, number_of_operations = map(int, raw_input().split())

    if number_of_rows == 0:
        break

    row_operations = [[0, 0] for _ in range(number_of_rows)]
    column_operations = [[0, 0] for _ in range(number_of_columns)]

    for operation_index in range(1, number_of_operations + 1):

        target_type, target_index, flip_state = map(int, raw_input().split())

        if target_type == 0:
            row_operations[target_index] = [operation_index, flip_state]
        else:
            column_operations[target_index] = [operation_index, flip_state]

    column_flip_timestamps = [
        sorted(
            column_operations[column_index][0]
            for column_index in range(number_of_columns)
            if column_operations[column_index][1] == 1
        ),
        sorted(
            column_operations[column_index][0]
            for column_index in range(number_of_columns)
            if column_operations[column_index][1] == 0
        )
    ]

    total_flipped_cells = number_of_rows * sum(
        column_operations[column_index][1] for column_index in range(number_of_columns)
    )

    for row_index in range(number_of_rows):

        last_row_operation_timestamp, last_row_flip_state = row_operations[row_index]
        timestamps_list = column_flip_timestamps[last_row_flip_state]

        num_columns_flipped_before_row = bisect(timestamps_list, last_row_operation_timestamp)
        total_flipped_cells -= ((-1) ** last_row_flip_state) * num_columns_flipped_before_row

    print total_flipped_cells