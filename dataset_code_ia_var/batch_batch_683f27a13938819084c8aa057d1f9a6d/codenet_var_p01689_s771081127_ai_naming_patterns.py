def bfs_search(start_row, start_col, target_row, target_col):
    bfs_visited = [[-1 for col_idx in range(map_width)] for row_idx in range(map_height)]
    bfs_row_offset = [1, -1, 0, 0]
    bfs_col_offset = [0, 0, 1, -1]
    bfs_queue_rows = [start_row]
    bfs_queue_cols = [start_col]
    bfs_visited[start_row][start_col] = 1
    while len(bfs_queue_cols) != 0:
        current_row = bfs_queue_rows.pop(0)
        current_col = bfs_queue_cols.pop(0)
        for dir_idx in range(4):
            new_row = current_row + bfs_row_offset[dir_idx]
            new_col = current_col + bfs_col_offset[dir_idx]
            if 0 <= new_row < map_height and 0 <= new_col < map_width:
                if new_row == target_row and new_col == target_col:
                    return "Yes"
                if bfs_visited[new_row][new_col] == -1 and map_layout[new_row][new_col] == ".":
                    bfs_visited[new_row][new_col] = 1
                    bfs_queue_rows.append(new_row)
                    bfs_queue_cols.append(new_col)
    return "No"

map_height, map_width, max_distance, num_events = map(int, input().split())
map_layout = [input() for _ in range(map_height)]
effect_radius = list(map(int, input().split()))
event_list = [list(map(int, input().split())) for _ in range(num_events)]
effect_map = [[0 for _ in range(map_width)] for _ in range(map_height)]
for event_col, event_row, event_step in event_list:
    if event_step == max_distance:
        for fill_row in range(map_height):
            for fill_col in range(map_width):
                effect_map[fill_row][fill_col] += 1
    if event_step < max_distance:
        for fill_row in range(event_row - effect_radius[event_step], event_row + effect_radius[event_step] + 1):
            for fill_col in range(event_col - effect_radius[event_step], event_col + effect_radius[event_step] + 1):
                if 0 <= fill_row < map_height and 0 <= fill_col < map_width:
                    effect_map[fill_row][fill_col] += 1
    if event_step != 0:
        for clear_row in range(event_row - effect_radius[event_step - 1], event_row + effect_radius[event_step - 1] + 1):
            for clear_col in range(event_col - effect_radius[event_step - 1], event_col + effect_radius[event_step - 1] + 1):
                if 0 <= clear_row < map_height and 0 <= clear_col < map_width:
                    effect_map[clear_row][clear_col] -= 1

valid_targets = []
for check_row in range(map_height):
    for check_col in range(map_width):
        if map_layout[check_row][check_col] == "D":
            start_pos_row = check_row
            start_pos_col = check_col
        if effect_map[check_row][check_col] == num_events and map_layout[check_row][check_col] != "#":
            valid_targets.append([check_row, check_col])

if len(valid_targets) == 0:
    print("Broken")
    quit()

path_outcomes = ["Broken" for _ in range(len(valid_targets))]
for outcome_idx in range(len(valid_targets)):
    target_row, target_col = valid_targets[outcome_idx]
    if start_pos_row == target_row and start_pos_col == target_col:
        path_outcomes[outcome_idx] = "Yes"
    else:
        path_outcomes[outcome_idx] = bfs_search(start_pos_row, start_pos_col, target_row, target_col)

for result_idx in range(1, len(path_outcomes)):
    if path_outcomes[result_idx] != path_outcomes[result_idx - 1]:
        print("Unknown")
        quit()

print(path_outcomes[0])