def main():
    import sys
    from itertools import chain

    while True:
        number_of_columns, number_of_rows = map(int, sys.stdin.readline().split())

        if number_of_columns == 0 and number_of_rows == 0:
            break

        flat_matrix_elements = list(
            chain.from_iterable(
                map(int, sys.stdin.readline().split())
                for _ in range(number_of_rows)
            )
        )

        maximum_column_sum = 0

        for column_index in range(number_of_columns):

            current_column_sum = sum(
                flat_matrix_elements[column_index::number_of_columns]
            )

            if maximum_column_sum < current_column_sum:
                maximum_column_sum = current_column_sum

        print(maximum_column_sum)

if __name__ == '__main__':
    main()