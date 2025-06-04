from collections import deque
while True:
    stage_count = int(input())
    if stage_count == 0:
        exit()
    stage_grid_list = []
    for stage_idx in range(stage_count):
        cell_values = list(map(int, input().split()))
        cell_grid = [cell_values[:4], cell_values[4:8], cell_values[8:12], cell_values[12:]]
        zone_matrix = [[0 for col_idx in range(3)] for row_idx in range(3)]
        for zone_row in range(3):
            for zone_col in range(3):
                for offset_row in range(2):
                    for offset_col in range(2):
                        zone_matrix[zone_row][zone_col] += cell_grid[zone_row + offset_row][zone_col + offset_col]
        stage_grid_list.append(zone_matrix)

    bfs_queue = deque()
    visited_states = set()
    if stage_grid_list[0][1][1]:
        print(0)
        continue
    bfs_queue.append((0, 1, 1, (0, 0, 0, 0)))
    while bfs_queue:
        current_stage, pos_row, pos_col, step_reset_cnts = bfs_queue.popleft()
        if (pos_row, pos_col) == (0, 0):
            step_reset_cnts = (0, step_reset_cnts[1] + 1, step_reset_cnts[2] + 1, step_reset_cnts[3] + 1)
        elif (pos_row, pos_col) == (0, 2):
            step_reset_cnts = (step_reset_cnts[0] + 1, 0, step_reset_cnts[2] + 1, step_reset_cnts[3] + 1)
        elif (pos_row, pos_col) == (2, 0):
            step_reset_cnts = (step_reset_cnts[0] + 1, step_reset_cnts[1] + 1, 0, step_reset_cnts[3] + 1)
        elif (pos_row, pos_col) == (2, 2):
            step_reset_cnts = (step_reset_cnts[0] + 1, step_reset_cnts[1] + 1, step_reset_cnts[2] + 1, 0)
        else:
            step_reset_cnts = (step_reset_cnts[0] + 1, step_reset_cnts[1] + 1, step_reset_cnts[2] + 1, step_reset_cnts[3] + 1)
        if max(step_reset_cnts) > 6:
            continue
        state_tuple = (current_stage, pos_row, pos_col, step_reset_cnts)
        if state_tuple in visited_states:
            continue
        visited_states.add(state_tuple)
        if current_stage == stage_count - 1:
            print(1)
            break
        for next_row in range(3):
            if not stage_grid_list[current_stage + 1][next_row][pos_col]:
                bfs_queue.append((current_stage + 1, next_row, pos_col, step_reset_cnts))
            if not stage_grid_list[current_stage + 1][pos_row][next_row]:
                bfs_queue.append((current_stage + 1, pos_row, next_row, step_reset_cnts))
    else:
        print(0)