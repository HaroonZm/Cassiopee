height_count, width_count = list(map(int, input().split(' ')))
grid_values = [list(map(int, input().split(' '))) for _ in range(height_count)]

max_path_length = height_count * width_count

min_time_dp = [[[float('inf') for path_len in range(max_path_length)] for col in range(width_count)] for row in range(height_count)]
min_time_dp[0][0][0] = 0

for path_len in range(1, max_path_length):
    path_skip_flag = False
    for row_idx in range(height_count):
        for col_idx in range(width_count):
            if row_idx + col_idx > path_len:
                path_skip_flag = True
                continue
            adj_cells = [
                (row_idx-1, col_idx), (row_idx+1, col_idx),
                (row_idx, col_idx-1), (row_idx, col_idx+1)
            ]
            valid_adjs = [
                (adj_row, adj_col)
                for adj_row, adj_col in adj_cells
                if 0 <= adj_row < height_count and 0 <= adj_col < width_count
            ]
            min_adj_time = float('inf')
            for adj_row_idx, adj_col_idx in valid_adjs:
                operation_time = grid_values[row_idx][col_idx] * (path_len-1) * 2 + grid_values[row_idx][col_idx] + min_time_dp[adj_row_idx][adj_col_idx][path_len-1]
                min_adj_time = min(min_adj_time, operation_time)
            min_time_dp[row_idx][col_idx][path_len] = min_adj_time
        if path_skip_flag:
            continue

print(min(min_time_dp[height_count-1][width_count-1]))