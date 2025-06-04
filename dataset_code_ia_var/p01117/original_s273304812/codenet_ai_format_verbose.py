while True:

    number_of_columns, number_of_rows = map(int, input().split())

    if number_of_columns == 0:
        break

    scores_matrix = [
        list(map(int, input().split()))
        for row_index in range(number_of_rows)
    ]

    maximum_column_sum = 0

    for column_index in range(number_of_columns):

        current_column_sum = sum(
            scores_matrix[row_index][column_index]
            for row_index in range(number_of_rows)
        )

        maximum_column_sum = max(maximum_column_sum, current_column_sum)

    print(maximum_column_sum)