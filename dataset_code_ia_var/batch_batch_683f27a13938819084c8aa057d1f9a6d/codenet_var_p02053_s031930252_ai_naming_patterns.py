INF_CONST = 1e11
height_input, width_input = [int(value_input) for value_input in input().split()]
grid_list = [["" for _ in range(width_input)] for _ in range(height_input)]
black_positions_set = set()
for row_idx in range(height_input):
    grid_list[row_idx] = list(str(input()))
    for col_idx in range(width_input):
        if grid_list[row_idx][col_idx] == "B":
            black_positions_set.add((row_idx, col_idx))

max_sum_index = 0
min_sum_index = INF_CONST
max_diff_index = 0
min_diff_index = INF_CONST
for pos_tuple in black_positions_set:
    row_cur, col_cur = pos_tuple
    max_sum_index = max(row_cur + col_cur, max_sum_index)
    min_sum_index = min(row_cur + col_cur, min_sum_index)
    max_diff_index = max(row_cur - col_cur, max_diff_index)
    min_diff_index = min(row_cur - col_cur, min_diff_index)
print(max(max_sum_index - min_sum_index, max_diff_index - min_diff_index))