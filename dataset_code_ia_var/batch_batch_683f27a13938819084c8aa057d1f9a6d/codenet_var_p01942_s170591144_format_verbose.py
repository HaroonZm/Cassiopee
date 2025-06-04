from heapq import heappush, heappop

height_grid, width_grid, expiration_duration, num_queries = map(int, input().split())

event_priority_queue = []
cell_state_grid = [[0] * (width_grid + 1) for _ in range(height_grid + 1)]
active_objects_BIT = [[0] * (width_grid + 1) for _ in range(height_grid + 1)]
expired_objects_BIT = [[0] * (width_grid + 1) for _ in range(height_grid + 1)]

def query_prefix_sum(BIT_structure, max_row, max_col):
    prefix_sum = 0
    row_pointer = max_row
    while row_pointer:
        col_pointer = max_col
        row_elements = BIT_structure[row_pointer]
        while col_pointer:
            prefix_sum += row_elements[col_pointer]
            col_pointer -= col_pointer & -col_pointer
        row_pointer -= row_pointer & -row_pointer
    return prefix_sum

def update_BIT(BIT_structure, update_row, update_col, delta_value):
    row_pointer = update_row
    while row_pointer <= height_grid:
        col_pointer = update_col
        row_elements = BIT_structure[row_pointer]
        while col_pointer <= width_grid:
            row_elements[col_pointer] += delta_value
            col_pointer += col_pointer & -col_pointer
        row_pointer += row_pointer & -row_pointer

for query_index in range(num_queries):

    input_data = list(map(int, input().split()))
    current_time, command_type, *parameters = input_data

    while event_priority_queue and event_priority_queue[0][0] <= current_time:
        event_time, cell_row, cell_col = heappop(event_priority_queue)
        update_BIT(active_objects_BIT, cell_row, cell_col, -1)
        update_BIT(expired_objects_BIT, cell_row, cell_col, 1)
        cell_state_grid[cell_row][cell_col] = 2

    if command_type == 0:
        target_row, target_col = parameters
        cell_state_grid[target_row][target_col] = 1
        update_BIT(active_objects_BIT, target_row, target_col, 1)
        heappush(event_priority_queue, (current_time + expiration_duration, target_row, target_col))

    elif command_type == 1:
        target_row, target_col = parameters
        if cell_state_grid[target_row][target_col] == 2:
            update_BIT(expired_objects_BIT, target_row, target_col, -1)
            cell_state_grid[target_row][target_col] = 0

    else:
        row_start, col_start, row_end, col_end = parameters
        total_active = (
            query_prefix_sum(active_objects_BIT, row_end, col_end)
            - query_prefix_sum(active_objects_BIT, row_end, col_start - 1)
            - query_prefix_sum(active_objects_BIT, row_start - 1, col_end)
            + query_prefix_sum(active_objects_BIT, row_start - 1, col_start - 1)
        )
        total_expired = (
            query_prefix_sum(expired_objects_BIT, row_end, col_end)
            - query_prefix_sum(expired_objects_BIT, row_end, col_start - 1)
            - query_prefix_sum(expired_objects_BIT, row_start - 1, col_end)
            + query_prefix_sum(expired_objects_BIT, row_start - 1, col_start - 1)
        )
        print(total_expired, total_active)