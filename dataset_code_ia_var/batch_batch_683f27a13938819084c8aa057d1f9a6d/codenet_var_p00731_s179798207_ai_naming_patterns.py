from Queue import Queue
MOVE_LEFT = ((-1, 0), (-1, 1), (-1, 2), (-1, -1), (-1, -2), (-2, 0), (-2, 1), (-2, -1), (-3, 0))
MOVE_RIGHT = ((1, 0), (1, 1), (1, 2), (1, -1), (1, -2), (2, 0), (2, 1), (2, -1), (3, 0))
MOVES = (MOVE_LEFT, MOVE_RIGHT)
INFINITY_COST = 1000
FOOT_LEFT = 0
FOOT_RIGHT = 1
while True:
    width, height = map(int, raw_input().split())
    if width == 0 and height == 0:
        break
    grid_cells = [raw_input().split() for row_index in range(height)]
    cost_table = [[[INFINITY_COST, INFINITY_COST] for col_index in range(width)] for row_index in range(height)]
    position_queue = Queue()
    target_positions = []
    for row_index in range(height):
        for col_index in range(width):
            cell_value = grid_cells[row_index][col_index]
            if cell_value == "S":
                position_queue.put((col_index, row_index, FOOT_LEFT))
                position_queue.put((col_index, row_index, FOOT_RIGHT))
                cost_table[row_index][col_index][FOOT_LEFT] = 0
                cost_table[row_index][col_index][FOOT_RIGHT] = 0
            elif cell_value == "T":
                target_positions.append((col_index, row_index))
    while not position_queue.empty():
        current_x, current_y, current_foot = position_queue.get()
        if current_foot == FOOT_RIGHT:
            for move_delta_x, move_delta_y in MOVES[FOOT_LEFT]:
                next_x = current_x + move_delta_x
                next_y = current_y + move_delta_y
                if 0 <= next_x < width and 0 <= next_y < height and grid_cells[next_y][next_x] != "X" and grid_cells[next_y][next_x] != "S":
                    if grid_cells[next_y][next_x] == "T":
                        next_cost = cost_table[current_y][current_x][FOOT_RIGHT]
                    else:
                        next_cost = int(grid_cells[next_y][next_x]) + cost_table[current_y][current_x][FOOT_RIGHT]
                    if cost_table[next_y][next_x][FOOT_LEFT] > next_cost:
                        cost_table[next_y][next_x][FOOT_LEFT] = next_cost
                        position_queue.put((next_x, next_y, FOOT_LEFT))
        elif current_foot == FOOT_LEFT:
            for move_delta_x, move_delta_y in MOVES[FOOT_RIGHT]:
                next_x = current_x + move_delta_x
                next_y = current_y + move_delta_y
                if 0 <= next_x < width and 0 <= next_y < height and grid_cells[next_y][next_x] != "X" and grid_cells[next_y][next_x] != "S":
                    if grid_cells[next_y][next_x] == "T":
                        next_cost = cost_table[current_y][current_x][FOOT_LEFT]
                    else:
                        next_cost = int(grid_cells[next_y][next_x]) + cost_table[current_y][current_x][FOOT_LEFT]
                    if cost_table[next_y][next_x][FOOT_RIGHT] > next_cost:
                        cost_table[next_y][next_x][FOOT_RIGHT] = next_cost
                        position_queue.put((next_x, next_y, FOOT_RIGHT))
    minimal_total_cost = INFINITY_COST
    for target_x, target_y in target_positions:
        minimal_total_cost = min(minimal_total_cost, cost_table[target_y][target_x][FOOT_LEFT])
        minimal_total_cost = min(minimal_total_cost, cost_table[target_y][target_x][FOOT_RIGHT])
    print minimal_total_cost if minimal_total_cost != INFINITY_COST else -1