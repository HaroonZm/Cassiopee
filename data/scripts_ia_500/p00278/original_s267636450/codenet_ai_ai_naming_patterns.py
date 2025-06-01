import bisect

INFINITY = int(10**9 + 1)

num_elements, num_queries = map(int, input().split())
indexed_values = [(int(input()), index) for index in range(num_elements)]
indexed_values.sort()
sorted_values = [0] * num_elements
index_map = [0] * num_elements

for sorted_index, (_, original_index) in enumerate(indexed_values):
    sorted_values[sorted_index] = indexed_values[sorted_index][0]
    index_map[original_index] = sorted_index

leader_indices = []

for _ in range(num_queries):
    query = input().split()
    query_type = query[0]
    query_arg = int(query[1]) - 1

    if query_type == 'ADD':
        insertion_position = bisect.bisect_left(leader_indices, index_map[query_arg])
        leader_indices = leader_indices[:insertion_position] + [index_map[query_arg]] + leader_indices[insertion_position:]
    elif query_type == 'REMOVE':
        leader_indices.remove(index_map[query_arg])
    else:  # CHECK
        fail_range = -1
        success_range = INFINITY

        while success_range - fail_range > 1:
            mid_range = (success_range + fail_range) // 2
            covered_count = 0
            previous_right_index = -1

            for leader_index in leader_indices:
                left_index = bisect.bisect_left(sorted_values, sorted_values[leader_index] - mid_range)
                right_index = bisect.bisect_right(sorted_values, sorted_values[leader_index]) - 1

                if left_index <= previous_right_index:
                    left_index = previous_right_index + 1

                covered_count += right_index - left_index + 1
                previous_right_index = right_index

            uncovered_count = num_elements - covered_count
            if uncovered_count <= query_arg + 1:
                success_range = mid_range
            else:
                fail_range = mid_range

        if success_range == INFINITY:
            print('NA')
        else:
            print(success_range)