import sys

sys_input = sys.stdin.readline

input_count = int(sys_input())
input_base_list = list(map(int, sys_input().split()))
query_operations = [[] for idx in range(input_count)]
query_count = int(sys_input())
for query_idx in range(query_count):
    left_idx, right_idx = map(int, sys_input().split())
    query_operations[right_idx-1].append(left_idx-1)

zero_count = input_base_list.count(0)

prefix_data_list = [(-1) ** ((input_base_list[i] == 1) + 1) for i in range(input_count)]
for idx in range(1, input_count):
    prefix_data_list[idx] += prefix_data_list[idx-1]
prefix_data_list = [0] + prefix_data_list

for op_list in query_operations:
    op_list.sort(reverse=True)

segment_size = input_count + 1
segment_leaf_size = 2 ** (segment_size - 1).bit_length()
segment_data = [None] * (2 * segment_leaf_size)
segment_inf = (-2 ** 31, -2 ** 31)

def segment_update(update_left, update_right, update_value):
    left_ptr = update_left + segment_leaf_size
    right_ptr = update_right + segment_leaf_size
    while left_ptr < right_ptr:
        if right_ptr & 1:
            right_ptr -= 1
            if segment_data[right_ptr - 1]:
                segment_data[right_ptr - 1] = max(update_value, segment_data[right_ptr - 1])
            else:
                segment_data[right_ptr - 1] = update_value
        if left_ptr & 1:
            if segment_data[left_ptr - 1]:
                segment_data[left_ptr - 1] = max(update_value, segment_data[left_ptr - 1])
            else:
                segment_data[left_ptr - 1] = update_value
            left_ptr += 1
        left_ptr >>= 1
        right_ptr >>= 1

def segment_raw_query(query_idx):
    segment_idx = query_idx + segment_leaf_size - 1
    result = segment_inf
    while segment_idx >= 0:
        if segment_data[segment_idx]:
            result = max(result, segment_data[segment_idx])
        segment_idx = (segment_idx - 1) // 2
    return result

def segment_query(query_idx):
    return segment_raw_query(query_idx)[1]

for idx in range(input_count + 1):
    segment_update(idx, idx + 1, (-prefix_data_list[idx], -prefix_data_list[idx]))
if query_operations[0]:
    segment_update(1, 2, (0, 0))

for idx in range(1, input_count):
    seg_current = segment_query(idx)
    segment_update(idx + 1, idx + 2, (seg_current + prefix_data_list[idx] - prefix_data_list[idx + 1], seg_current + prefix_data_list[idx] - prefix_data_list[idx + 1]))
    for left_idx in query_operations[idx]:
        left_value = segment_query(left_idx)
        segment_update(left_idx + 1, idx + 2, (left_value, left_value))

print(input_count - (zero_count + segment_query(input_count) + prefix_data_list[input_count]))