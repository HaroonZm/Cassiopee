while True:

    number_of_name_value_pairs, number_of_queries = map(int, input().split())

    if number_of_name_value_pairs == 0:
        break

    entry_names, entry_points = zip(
        *[
            [
                entry_string.strip("*") if index_in_pair == 0 else int(entry_string)
                for index_in_pair, entry_string in enumerate(input().split())
            ]
            for _ in range(number_of_name_value_pairs)
        ]
    )

    query_strings = [input() for _ in range(number_of_queries)]

    total_points = 0

    for current_query in query_strings:
        for entry_index, entry_name in enumerate(entry_names):
            if current_query.endswith(entry_name):
                total_points += entry_points[entry_index]

    print(total_points)