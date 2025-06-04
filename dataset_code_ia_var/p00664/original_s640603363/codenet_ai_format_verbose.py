while True:

    number_of_rows, number_of_columns, number_of_queries = map(int, input().split())

    if number_of_rows == 0:
        break

    list_of_queries = [list(map(int, input().split())) for _ in range(number_of_queries)]
    list_of_queries.reverse()

    is_row_marked = [False] * number_of_rows
    is_column_marked = [False] * number_of_columns

    current_unmarked_rows = number_of_columns
    current_unmarked_columns = number_of_rows

    final_answer = 0

    for query_type, index, flag in list_of_queries:

        if query_type == 0:
            if not is_row_marked[index]:
                is_row_marked[index] = True
                current_unmarked_columns -= 1
                if flag:
                    final_answer += current_unmarked_rows

        else:
            if not is_column_marked[index]:
                is_column_marked[index] = True
                current_unmarked_rows -= 1
                if flag:
                    final_answer += current_unmarked_columns

    print(final_answer)