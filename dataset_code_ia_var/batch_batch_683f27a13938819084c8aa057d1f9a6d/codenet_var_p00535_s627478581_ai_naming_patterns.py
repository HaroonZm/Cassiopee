import queue as mino_queue

input_dims = list(map(int, input().split()))
grid_chars = [[] for row_idx in range(input_dims[0])]
grid_clues = [[] for row_idx in range(input_dims[0])]
process_queues = [None, None]
process_queues[0] = mino_queue.Queue()
process_queues[1] = mino_queue.Queue()
neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for row_idx in range(input_dims[0]):
    grid_chars[row_idx] = list(input())
    for col_idx in range(input_dims[1]):
        grid_clues[row_idx].append(0)
        if grid_chars[row_idx][col_idx] != '.':
            grid_chars[row_idx][col_idx] = int(grid_chars[row_idx][col_idx])

for row_idx in range(1, input_dims[0] - 1):
    for col_idx in range(1, input_dims[1] - 1):
        for offset in neighbor_offsets:
            neighbor_row = row_idx + offset[0]
            neighbor_col = col_idx + offset[1]
            if grid_chars[neighbor_row][neighbor_col] == '.':
                grid_clues[row_idx][col_idx] += 1

step_counter = 0

for row_idx in range(input_dims[0]):
    for col_idx in range(input_dims[1]):
        if grid_chars[row_idx][col_idx] != '.' and grid_chars[row_idx][col_idx] <= grid_clues[row_idx][col_idx]:
            grid_chars[row_idx][col_idx] = '.'
            process_queues[0].put((row_idx, col_idx))

if process_queues[0].empty():
    quit()

active_queue_idx = 0
while not process_queues[active_queue_idx].empty():
    while not process_queues[active_queue_idx].empty():
        cell_pos = process_queues[active_queue_idx].get()
        for offset in neighbor_offsets:
            neighbor_row = cell_pos[0] + offset[0]
            neighbor_col = cell_pos[1] + offset[1]
            grid_clues[neighbor_row][neighbor_col] += 1
            if (
                grid_chars[neighbor_row][neighbor_col] != '.'
                and grid_chars[neighbor_row][neighbor_col] == grid_clues[neighbor_row][neighbor_col]
            ):
                grid_chars[neighbor_row][neighbor_col] = '.'
                process_queues[active_queue_idx ^ 1].put((neighbor_row, neighbor_col))
    active_queue_idx ^= 1
    step_counter += 1

print(step_counter)