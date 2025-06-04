import bisect

num_queries = int(input())
sorted_list = []

for query_index in range(num_queries):
    query_parts = input().split()
    operation_code = query_parts[0]
    if operation_code == "3":
        range_left = int(query_parts[1])
        range_right = int(query_parts[2])
        left_pos = bisect.bisect_left(sorted_list, range_left)
        right_pos = bisect.bisect_right(sorted_list, range_right)
        for value in sorted_list[left_pos:right_pos]:
            print(value)
    else:
        element_value = int(query_parts[1])
        position_left = bisect.bisect_left(sorted_list, element_value)
        position_right = bisect.bisect_right(sorted_list, element_value)
        if operation_code == "0":
            sorted_list.insert(position_left, element_value)
            print(len(sorted_list))
        elif operation_code == "1":
            print(position_right - position_left)
        elif operation_code == "2":
            del sorted_list[position_left:position_right]