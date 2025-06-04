from collections import deque

input_height, input_width, input_num_targets = map(int, input().split())
positions_targets = [None] * (input_num_targets + 1)
grid_matrix = ["X" * (input_width + 2)]
grid_append = grid_matrix.append

for row_index in range(input_height):
    input_row = "X" + input() + "X"
    if "S" in input_row:
        positions_targets[0] = (row_index + 1, input_row.index("S"))
    for col_index in range(len(input_row)):
        cell_value = input_row[col_index]
        if cell_value not in ('S', '.', 'X'):
            positions_targets[int(cell_value)] = (row_index + 1, col_index)
    grid_append(input_row)
grid_append("X" * (input_width + 2))

def find_shortest_path_bfs(target_index):
    visited_matrix = [[None] * (input_width + 2) for _ in range(input_height + 2)]
    start_x, start_y = positions_targets[target_index]
    bfs_queue = deque()
    bfs_queue_append = bfs_queue.append
    bfs_queue_popleft = bfs_queue.popleft
    bfs_queue_append((start_x, start_y))
    for step_count in range(10000000):
        current_queue_size = len(bfs_queue)
        for _ in range(current_queue_size):
            curr_x, curr_y = bfs_queue_popleft()
            if grid_matrix[curr_x][curr_y] == 'X' or visited_matrix[curr_x][curr_y] is not None:
                continue
            if (curr_x, curr_y) == positions_targets[target_index + 1]:
                return step_count
            visited_matrix[curr_x][curr_y] = step_count
            bfs_queue_append((curr_x + 1, curr_y))
            bfs_queue_append((curr_x - 1, curr_y))
            bfs_queue_append((curr_x, curr_y + 1))
            bfs_queue_append((curr_x, curr_y - 1))

total_distance = 0
for target_idx in range(input_num_targets):
    bfs_result = find_shortest_path_bfs(target_idx)
    if bfs_result is not None:
        total_distance += bfs_result
print(total_distance)