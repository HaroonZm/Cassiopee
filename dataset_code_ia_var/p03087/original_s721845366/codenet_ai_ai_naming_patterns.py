num_length, num_queries = map(int, input().split())
string_sequence = input()
prefix_count_accum = 0
prefix_count_list = [0] * num_length
for idx_char in range(1, num_length):
    if string_sequence[idx_char - 1] == 'A' and string_sequence[idx_char] == 'C':
        prefix_count_accum += 1
    prefix_count_list[idx_char] = prefix_count_accum
for idx_query in range(num_queries):
    range_left, range_right = map(int, input().split())
    result_count = prefix_count_list[range_right - 1] - prefix_count_list[range_left - 1]
    print(result_count)