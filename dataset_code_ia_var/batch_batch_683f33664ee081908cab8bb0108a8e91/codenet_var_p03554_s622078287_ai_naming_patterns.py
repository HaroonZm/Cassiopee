input_length = int(input())
input_values = list(map(int, input().split()))
operation_ranges = [[] for _ in range(input_length)]
query_count = int(input())
for query_index in range(query_count):
    left_endpoint, right_endpoint = map(int, input().split())
    operation_ranges[right_endpoint - 1].append(left_endpoint - 1)

zero_count = input_values.count(0)

prefix_data = [(-1) ** ((input_values[i] == 1) + 1) for i in range(input_length)]
for prefix_index in range(1, input_length):
    prefix_data[prefix_index] += prefix_data[prefix_index - 1]
prefix_data = [0] + prefix_data

for operation_index in range(input_length):
    operation_ranges[operation_index].sort(reverse=True)

segment_size = input_length + 1
tree_capacity = 2 ** (segment_size - 1).bit_length()
segment_tree_data = [None] * (2 * tree_capacity)
NEG_INF = (-2 ** 31, -2 ** 31)

def segment_tree_update(range_left, range_right, value_tuple):
    left = range_left + tree_capacity
    right = range_right + tree_capacity
    while left < right:
        if right & 1:
            right -= 1
            if segment_tree_data[right - 1]:
                segment_tree_data[right - 1] = max(value_tuple, segment_tree_data[right - 1])
            else:
                segment_tree_data[right - 1] = value_tuple
        if left & 1:
            if segment_tree_data[left - 1]:
                segment_tree_data[left - 1] = max(value_tuple, segment_tree_data[left - 1])
            else:
                segment_tree_data[left - 1] = value_tuple
            left += 1
        left >>= 1
        right >>= 1

def segment_tree_query_recursive(index):
    node = index + tree_capacity - 1
    result = NEG_INF
    while node >= 0:
        if segment_tree_data[node]:
            result = max(result, segment_tree_data[node])
        node = (node - 1) // 2
    return result

def segment_tree_query(index):
    return segment_tree_query_recursive(index)[1]

for position in range(input_length + 1):
    segment_tree_update(position, position + 1, (-prefix_data[position], -prefix_data[position]))
if operation_ranges[0]:
    segment_tree_update(1, 2, (0, 0))

for current_position in range(1, input_length):
    previous_value = segment_tree_query(current_position)
    segment_tree_update(current_position + 1, current_position + 2,
                        (previous_value + prefix_data[current_position] - prefix_data[current_position + 1],
                         previous_value + prefix_data[current_position] - prefix_data[current_position + 1]))
    for operation_left in operation_ranges[current_position]:
        left_value = segment_tree_query(operation_left)
        segment_tree_update(operation_left + 1, current_position + 2, (left_value, left_value))

final_result = input_length - (zero_count + segment_tree_query(input_length) + prefix_data[input_length])
print(final_result)