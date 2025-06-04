import sys
sys.setrecursionlimit(10**9)

def segment_tree_build(tree, data, node, left, right):
    if left == right:
        tree[node] = data[left]
    else:
        mid = (left + right) // 2
        segment_tree_build(tree, data, 2 * node, left, mid)
        segment_tree_build(tree, data, 2 * node + 1, mid + 1, right)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

def segment_tree_query_max(tree, node, left, right, query_left, query_right):
    if query_left > query_right:
        return 0
    if query_left == left and query_right == right:
        return tree[node]
    mid = (left + right) // 2
    left_result = segment_tree_query_max(tree, 2 * node, left, mid, query_left, min(query_right, mid))
    right_result = segment_tree_query_max(tree, 2 * node + 1, mid + 1, right, max(query_left, mid + 1), query_right)
    return max(left_result, right_result)

def segment_tree_update(tree, node, left, right, update_pos, update_value):
    if left == right:
        tree[node] = update_value
    else:
        mid = (left + right) // 2
        if update_pos <= mid:
            segment_tree_update(tree, 2 * node, left, mid, update_pos, update_value)
        else:
            segment_tree_update(tree, 2 * node + 1, mid + 1, right, update_pos, update_value)
        tree[node] = max(tree[2 * node], tree[2 * node + 1])

def segment_tree_initialize(size, base_data):
    tree = [0] * (4 * size)
    segment_tree_build(tree, base_data, 1, 0, size - 1)
    return tree

def process_flowers():
    num_flowers = int(raw_input())
    heights = list(map(int, raw_input().split()))
    beauties = list(map(int, raw_input().split()))
    height_to_beauty = {}
    for idx in range(num_flowers):
        height_to_beauty[heights[idx]] = beauties[idx]

    dp_array = [0] * num_flowers
    seg_tree = segment_tree_initialize(num_flowers, dp_array)
    for idx in range(num_flowers - 1, -1, -1):
        curr_height = heights[idx]
        current_max = segment_tree_query_max(seg_tree, 1, 0, num_flowers - 1, curr_height - 1, num_flowers - 1)
        dp_array[curr_height - 1] += height_to_beauty[curr_height] + current_max
        segment_tree_update(seg_tree, 1, 0, num_flowers - 1, curr_height - 1, dp_array[curr_height - 1])

    print(max(seg_tree))

process_flowers()