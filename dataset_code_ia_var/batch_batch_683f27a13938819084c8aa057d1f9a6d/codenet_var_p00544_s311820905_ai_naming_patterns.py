rows_count, cols_count = map(int, input().split())
grid_rows = []
for row_idx in range(rows_count):
    grid_rows.append(list(input()))

white_prefix_sum = []
blue_prefix_sum = []
red_prefix_sum = []
white_cumulative = 0
blue_cumulative = 0
red_cumulative = 0

for row_idx in range(rows_count):
    white_cumulative += grid_rows[row_idx].count('B') + grid_rows[row_idx].count('R')
    white_prefix_sum.append(white_cumulative)
for row_idx in range(rows_count):
    blue_cumulative += grid_rows[row_idx].count('W') + grid_rows[row_idx].count('R')
    blue_prefix_sum.append(blue_cumulative)
for row_idx in range(rows_count):
    red_cumulative += grid_rows[row_idx].count('W') + grid_rows[row_idx].count('B')
    red_prefix_sum.append(red_cumulative)

result_options = []
for white_end_idx in range(1, rows_count - 1):
    for blue_end_idx in range(white_end_idx + 1, rows_count):
        white_count = white_prefix_sum[white_end_idx - 1]
        blue_count = blue_prefix_sum[blue_end_idx - 1] - blue_prefix_sum[white_end_idx - 1]
        red_count = red_prefix_sum[rows_count - 1] - red_prefix_sum[blue_end_idx - 1]
        total_changes = white_count + blue_count + red_count
        result_options.append(total_changes)

print(min(result_options))