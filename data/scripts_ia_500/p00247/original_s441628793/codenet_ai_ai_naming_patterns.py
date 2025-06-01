from collections import deque

def run_ice_maze_game():
    direction_vectors = ((1, 0), (0, -1), (-1, 0), (0, 1))

    def dfs_mark_ice(x_coord, y_coord, ice_index):
        for dx, dy in direction_vectors:
            adj_x, adj_y = x_coord + dx, y_coord + dy
            if map_grid[adj_y][adj_x] == "X":
                map_grid[adj_y][adj_x] = ice_index
                ice_counts[ice_index] += 1
                dfs_mark_ice(adj_x, adj_y, ice_index)

    while True:
        width, height = map(int, input().split())
        if width == 0:
            break
        map_grid = [list("#" * (width + 2))] + [list("#" + input() + "#") for _ in range(height)] + [list("#" * (width + 2))]

        ice_index_counter = 0
        ice_counts = []
        start_x = start_y = None
        goal_x = goal_y = None

        for y in range(1, height + 1):
            for x in range(1, width + 1):
                cell = map_grid[y][x]
                if cell == "S":
                    start_x, start_y = x, y
                    map_grid[y][x] = "."
                elif cell == "G":
                    goal_x, goal_y = x, y
                    map_grid[y][x] = "."
                elif cell == "X":
                    map_grid[y][x] = ice_index_counter
                    ice_counts.append(1)
                    dfs_mark_ice(x, y, ice_index_counter)
                    ice_index_counter += 1

        queue = deque()
        init_counters = [cnt // 2 for cnt in ice_counts]
        queue.append((0, start_x, start_y, init_counters, 0))
        visited_states = {(start_x, start_y, 0): True}
        hash_values = [150 ** i for i in range(len(ice_counts))]

        while queue:
            current_score, current_x, current_y, current_counters, current_hash = queue.popleft()
            if (current_x, current_y) == (goal_x, goal_y):
                print(current_score)
                break
            for dx, dy in direction_vectors:
                next_x, next_y = current_x + dx, current_y + dy
                next_cell = map_grid[next_y][next_x]
                if next_cell == "#":
                    continue
                elif next_cell == ".":
                    state_key = (next_x, next_y, current_hash)
                    if state_key in visited_states:
                        continue
                    visited_states[state_key] = True
                    queue.append((current_score + 1, next_x, next_y, current_counters[:], current_hash))
                else:
                    ice_num = next_cell
                    if current_counters[ice_num] <= 0:
                        continue
                    updated_counters = current_counters[:]
                    updated_counters[ice_num] -= 1
                    updated_hash = current_hash + hash_values[ice_num]
                    state_key = (next_x, next_y, updated_hash)
                    if state_key in visited_states:
                        continue
                    visited_states[state_key] = True
                    queue.append((current_score + 1, next_x, next_y, updated_counters, updated_hash))

run_ice_maze_game()