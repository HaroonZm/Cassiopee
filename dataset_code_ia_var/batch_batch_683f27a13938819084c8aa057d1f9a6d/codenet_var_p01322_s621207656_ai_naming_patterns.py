while True:
    row_count, query_count = map(int, input().split())
    if row_count == 0:
        break

    name_list, value_list = zip(*[[field.strip("*") if idx == 0 else int(field) for idx, field in enumerate(input().split())] for _ in range(row_count)])

    query_list = [input() for _ in range(query_count)]
    total_sum = sum(
        value_list[idx]
        for query in query_list
        for idx, name in enumerate(name_list)
        if query.endswith(name)
    )
    print(total_sum)