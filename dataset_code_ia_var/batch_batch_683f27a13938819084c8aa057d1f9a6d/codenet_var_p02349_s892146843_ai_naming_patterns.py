import sys
input_stream = sys.stdin.readline
output_stream = sys.stdout.write

element_count, query_count = map(int, input_stream().split())

fenwick_tree = [0] * (element_count + 1)

def fenwick_add(index, value):
    while index <= element_count:
        fenwick_tree[index] += value
        index += index & -index

def fenwick_prefix_sum(index):
    result = 0
    while index:
        result += fenwick_tree[index]
        index -= index & -index
    return result

result_list = []
for query_index in range(query_count):
    query_data = list(map(int, input_stream().split()))
    query_type = query_data[0]
    if query_type == 1:
        query_position = query_data[1]
        result_list.append(str(fenwick_prefix_sum(query_position)))
    else:
        range_start, range_end, delta = query_data[1], query_data[2], query_data[3]
        fenwick_add(range_start, delta)
        if range_end < element_count:
            fenwick_add(range_end + 1, -delta)

output_stream("\n".join(result_list))
output_stream("\n")