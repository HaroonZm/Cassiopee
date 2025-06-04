num_rows, num_intervals, num_queries = map(int, input().split())
interval_list = [list(map(int, input().split())) for _ in range(num_intervals)]
query_list = [list(map(int, input().split())) for _ in range(num_queries)]

grid_count = [[0] * num_rows for _ in range(num_rows)]

for interval_idx in range(num_intervals):
    interval_start = interval_list[interval_idx][0]
    interval_end = interval_list[interval_idx][1]
    grid_count[interval_start - 1][interval_end - 1] += 1

prefix_sum_grid = [[0] * num_rows for _ in range(num_rows)]
for row_idx in range(num_rows):
    for col_idx in range(num_rows):
        if col_idx == 0:
            prefix_sum_grid[row_idx][col_idx] = grid_count[row_idx][col_idx]
        else:
            prefix_sum_grid[row_idx][col_idx] = grid_count[row_idx][col_idx] + prefix_sum_grid[row_idx][col_idx - 1]

for query_idx in range(num_queries):
    query_start = query_list[query_idx][0]
    query_end = query_list[query_idx][1]
    query_answer = 0
    for inner_idx in range(query_start, query_end + 1):
        if query_start != 1:
            query_answer += prefix_sum_grid[inner_idx - 1][query_end - 1] - prefix_sum_grid[inner_idx - 1][query_start - 2]
        else:
            query_answer += prefix_sum_grid[inner_idx - 1][query_end - 1]
    print(query_answer)