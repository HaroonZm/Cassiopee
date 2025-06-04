def segment_tree_update(index_update, value_update):
    node_index = 2 ** segment_tree_level - 1 + index_update
    segment_tree[node_index] = value_update
    parent_index = (node_index - 1) // 2
    while parent_index >= 0:
        segment_tree[parent_index] = max(segment_tree[2 * parent_index + 1], segment_tree[2 * parent_index + 2])
        if parent_index == 0:
            break
        parent_index = (parent_index - 1) // 2

def segment_tree_query_max(left_query, right_query):
    left_index = 2 ** segment_tree_level - 1 + left_query
    right_index = 2 ** segment_tree_level - 1 + right_query
    max_value = 0
    while left_index < right_index:
        if left_index % 2 == 0:
            max_value = max(max_value, segment_tree[left_index])
        if right_index % 2 == 1:
            max_value = max(max_value, segment_tree[right_index])
        left_index //= 2
        right_index = right_index // 2 - 1

    if left_index == right_index:
        max_value = max(max_value, segment_tree[left_index])
    return max_value

input_size = int(input())
height_list = list(map(int, input().split()))
value_list = list(map(int, input().split()))

segment_tree_level = 0
while 2 ** segment_tree_level < input_size + 1:
    segment_tree_level += 1
segment_tree = [0] * (2 ** (segment_tree_level + 1) - 1)

for current_index in range(input_size):
    current_max = segment_tree_query_max(0, height_list[current_index])
    leaf_index = 2 ** segment_tree_level - 1 + height_list[current_index]
    if segment_tree[leaf_index] < value_list[current_index] + current_max:
        segment_tree_update(height_list[current_index], value_list[current_index] + current_max)

result_max = 0
for query_index in range(input_size + 1):
    leaf_index = 2 ** segment_tree_level - 1 + query_index
    result_max = max(result_max, segment_tree[leaf_index])

print(result_max)