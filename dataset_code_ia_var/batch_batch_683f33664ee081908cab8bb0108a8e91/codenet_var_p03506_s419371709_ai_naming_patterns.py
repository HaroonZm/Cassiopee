import sys

read_input_line = sys.stdin.readline
node_count, query_count = map(int, read_input_line().split())
query_value_pairs = [tuple(map(int, read_input_line().split())) for query_index in range(query_count)]

result_list = []
if node_count == 1:
    for value_a, value_b in query_value_pairs:
        result_list.append(min(value_a, value_b))
else:
    for value_a, value_b in query_value_pairs:
        current_a, current_b = value_a, value_b
        while current_a != current_b:
            if current_a > current_b:
                current_a, current_b = current_b, current_a
            current_b = (current_b + node_count - 2) // node_count
        result_list.append(current_a)
print(*result_list, sep='\n')