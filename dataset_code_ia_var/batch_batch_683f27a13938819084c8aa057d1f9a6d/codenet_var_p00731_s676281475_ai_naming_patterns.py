import sys
from collections import defaultdict
from heapq import heappush, heappop

INFINITY_COST = 1000000

def get_next_positions(curr_row, curr_col, is_direction_reversed):
    if (curr_col == 0 and is_direction_reversed) or (curr_col == grid_width - 1 and not is_direction_reversed):
        return []
    move_step = 1 - 2 * is_direction_reversed
    next_positions = [(r, curr_col + move_step) for r in range(max(0, curr_row - 2), min(grid_height, curr_row + 3))]
    if (curr_col == 1 and is_direction_reversed) or (curr_col == grid_width - 2 and not is_direction_reversed):
        return next_positions
    for r in range(max(0, curr_row - 1), min(grid_height, curr_row + 2)):
        next_positions.append((r, curr_col + 2 * move_step))
    if (curr_col == 2 and is_direction_reversed) or (curr_col == grid_width - 3 and not is_direction_reversed):
        return next_positions
    next_positions.append((curr_row, curr_col + 3 * move_step))
    return next_positions

def shortest_path_dijkstra(start_positions, goal_positions):
    min_cost = defaultdict(lambda: INFINITY_COST)
    priority_queue = []
    for sy, sx in start_positions:
        for direction_flag in range(2):
            min_cost[(sy, sx, direction_flag)] = 0
            heappush(priority_queue, (0, sy, sx, direction_flag))

    while priority_queue:
        curr_cost, row, col, direction_flag = heappop(priority_queue)
        possible_moves = get_next_positions(row, col, direction_flag)
        next_direction_flag = direction_flag ^ 1
        for new_row, new_col in possible_moves:
            if grid_field[new_row][new_col] == "X":
                continue
            move_cost = 0 if grid_field[new_row][new_col] == "S" or grid_field[new_row][new_col] == "T" else grid_field[new_row][new_col]
            total_cost = curr_cost + move_cost
            if total_cost < min_cost[(new_row, new_col, next_direction_flag)]:
                min_cost[(new_row, new_col, next_direction_flag)] = total_cost
                heappush(priority_queue, (total_cost, new_row, new_col, next_direction_flag))

    result = INFINITY_COST
    for gy, gx in goal_positions:
        for direction_flag in range(2):
            if min_cost[(gy, gx, direction_flag)] < result:
                result = min_cost[(gy, gx, direction_flag)]
    return result if result < INFINITY_COST else -1

def process_grid(grid_width_input, grid_height_input, grid_map_input):
    global grid_width, grid_height, grid_field
    grid_width = grid_width_input
    grid_height = grid_height_input
    grid_field = grid_map_input

    start_points = []
    target_points = []
    for row_index in range(grid_height):
        for col_index in range(grid_width):
            cell_value = grid_field[row_index][col_index]
            if cell_value.isdecimal():
                grid_field[row_index][col_index] = int(cell_value)
            elif cell_value == "S":
                start_points.append((row_index, col_index))
            elif cell_value == "T":
                target_points.append((row_index, col_index))
    print(shortest_path_dijkstra(start_points, target_points))

while True:
    input_line = sys.stdin.readline()
    if not input_line:
        break
    grid_width_input, grid_height_input = map(int, input_line.split())
    if grid_width_input == 0:
        break
    grid_map_input = [sys.stdin.readline().split() for _ in range(grid_height_input)]
    process_grid(grid_width_input, grid_height_input, grid_map_input)