from heapq import heappush, heappop

num_rows, num_cols = map(int, input().split())
grid_values = [list(map(int, input().split())) for row_idx in range(num_rows)]

max_cost = 10**18
min_cost_paths = [[[max_cost] * num_cols for row_idx in range(num_rows)] for step_count in range(num_rows * num_cols + 1)]

neighbor_deltas = ((-1, 0), (0, -1), (1, 0), (0, 1))

priority_queue = [(0, 0, 0, 0)]
while priority_queue:
    current_cost, current_steps, current_col, current_row = heappop(priority_queue)
    if min_cost_paths[current_steps][current_row][current_col] < current_cost or current_steps == num_rows * num_cols:
        continue
    for delta_col, delta_row in neighbor_deltas:
        next_col = current_col + delta_col
        next_row = current_row + delta_row
        if not (0 <= next_col < num_cols) or not (0 <= next_row < num_rows):
            continue
        next_cost = current_cost + grid_values[next_row][next_col] * (current_steps * 2 + 1)
        if next_cost < min_cost_paths[current_steps + 1][next_row][next_col]:
            min_cost_paths[current_steps + 1][next_row][next_col] = next_cost
            heappush(priority_queue, (next_cost, current_steps + 1, next_col, next_row))

final_cost = max_cost
for steps_used in range(num_rows * num_cols + 1):
    final_cost = min(final_cost, min_cost_paths[steps_used][num_rows - 1][num_cols - 1])

print(final_cost)