import sys
read_line = sys.stdin.readline
CONST_INT_MAX = (1 << 31) - 1
var_size, var_query_count = map(int, read_line().split())
lst_queries = [list(map(int, read_line().split())) for _ in range(var_query_count)]
SEG_TREE_SIZE = 1 << 17
SEG_TREE_MAX_IDX = SEG_TREE_SIZE - 1
SEG_TREE_MID_IDX = SEG_TREE_MAX_IDX // 2
SEG_TREE_ARRAY_SIZE = 2 * SEG_TREE_SIZE - 1
seg_tree_values = [CONST_INT_MAX] * SEG_TREE_ARRAY_SIZE
seg_tree_lazy = [-1] * SEG_TREE_ARRAY_SIZE

def lazy_propagate(idx):

    if seg_tree_lazy[idx] == -1:
        return
    idx_left = idx * 2 + 1
    idx_right = idx * 2 + 2
    if idx < SEG_TREE_MID_IDX:
        seg_tree_values[idx_left] = seg_tree_values[idx_right] = seg_tree_lazy[idx_left] = seg_tree_lazy[idx_right] = seg_tree_lazy[idx]
        seg_tree_lazy[idx] = -1
        return
    if idx < SEG_TREE_MAX_IDX:
        seg_tree_values[idx_left] = seg_tree_values[idx_right] = seg_tree_lazy[idx]
        seg_tree_lazy[idx] = -1

def update_range(update_left, update_right, update_value, idx, tree_left, tree_right):

    if tree_right <= update_left or update_right <= tree_left:
        return
    if update_left <= tree_left and tree_right <= update_right:
        seg_tree_values[idx] = update_value
        if idx < SEG_TREE_MAX_IDX:
            seg_tree_lazy[idx] = update_value
        return

    lazy_propagate(idx)
    tree_mid = (tree_left + tree_right) // 2
    idx_left = idx * 2 + 1
    idx_right = idx * 2 + 2
    update_range(update_left, update_right, update_value, idx_left, tree_left, tree_mid)
    update_range(update_left, update_right, update_value, idx_right, tree_mid, tree_right)

    seg_tree_values[idx] = min(seg_tree_values[idx_left], seg_tree_values[idx_right])

def range_minimum_query(query_left, query_right, idx, tree_left, tree_right):

    if tree_right <= query_left or query_right <= tree_left:
        return CONST_INT_MAX

    if query_left <= tree_left and tree_right <= query_right:
        return seg_tree_values[idx]

    lazy_propagate(idx)
    tree_mid = (tree_left + tree_right) // 2
    idx_left = idx * 2 + 1
    idx_right = idx * 2 + 2
    left_min = range_minimum_query(query_left, query_right, idx_left, tree_left, tree_mid)
    right_min = range_minimum_query(query_left, query_right, idx_right, tree_mid, tree_right)
    return min(left_min, right_min)

list_result = []
for query in lst_queries:
    if query[0] == 0:
        update_range(query[1], query[2] + 1, query[3], 0, 0, SEG_TREE_SIZE)
    else:
        list_result.append(range_minimum_query(query[1], query[2] + 1, 0, 0, SEG_TREE_SIZE))

print('\n'.join(str(value) for value in list_result))