import bisect

while True:

    number_of_rows, number_of_columns, number_of_queries = map(int, raw_input().split())

    if number_of_rows == 0:
        break

    last_update_for_row = [[0, 0] for _ in range(number_of_rows)]
    last_update_for_column = [[0, 0] for _ in range(number_of_columns)]

    for query_index in range(1, number_of_queries + 1):

        update_type, index_to_update, new_value = map(int, raw_input().split())

        if update_type == 0:
            last_update_for_row[index_to_update] = [query_index, new_value]
        else:
            last_update_for_column[index_to_update] = [query_index, new_value]

    query_indices_for_columns_with_one = sorted(
        last_update_for_column[column_index][0] 
        for column_index in range(number_of_columns) 
        if last_update_for_column[column_index][1] == 1
    )

    query_indices_for_columns_with_zero = sorted(
        last_update_for_column[column_index][0] 
        for column_index in range(number_of_columns) 
        if last_update_for_column[column_index][1] == 0
    )

    total_cells_with_one = number_of_rows * sum(
        last_update_for_column[column_index][1] 
        for column_index in range(number_of_columns)
    )

    for current_row_index in range(number_of_rows):

        if last_update_for_row[current_row_index][1] == 0:
            total_cells_with_one -= bisect.bisect(
                query_indices_for_columns_with_one, 
                last_update_for_row[current_row_index][0]
            )
        else:
            total_cells_with_one += bisect.bisect(
                query_indices_for_columns_with_zero, 
                last_update_for_row[current_row_index][0]
            )

    print total_cells_with_one