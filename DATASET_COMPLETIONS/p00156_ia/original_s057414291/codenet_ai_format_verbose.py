from heapq import heappush, heappop

while True:
    width, height = map(int, input().split())
    if width == 0:
        break

    map_rows = ["X" + input() + "X" for _ in range(height)]
    map_rows.insert(0, "X" * (width + 2))
    map_rows.append("X" * (width + 2))

    priority_queue = []
    visited_cells = [[False] * (width + 2) for _ in range(height + 2)]
    reached_goal_directly = False

    # Initialize border positions in the priority queue
    for x_position in range(1, width + 1):
        if map_rows[1][x_position] == "&" or map_rows[height][x_position] == "&":
            reached_goal_directly = True
            break

        cost_start_top = 1 if map_rows[1][x_position] == "#" else 0
        status_start_top = 0 if map_rows[1][x_position] == "#" else 1
        heappush(priority_queue, (cost_start_top, status_start_top, (x_position, 1)))
        visited_cells[1][x_position] = True

        cost_start_bottom = 1 if map_rows[height][x_position] == "#" else 0
        status_start_bottom = 0 if map_rows[height][x_position] == "#" else 1
        heappush(priority_queue, (cost_start_bottom, status_start_bottom, (x_position, height)))
        visited_cells[height][x_position] = True

    # Initialize left and right borders in the priority queue
    for y_position in range(1, height + 1):
        if map_rows[y_position][1] == "&" or map_rows[y_position][width] == "&":
            reached_goal_directly = True
            break

        cost_start_left = 1 if map_rows[y_position][1] == "#" else 0
        status_start_left = 0 if map_rows[y_position][1] == "#" else 1
        heappush(priority_queue, (cost_start_left, status_start_left, (1, y_position)))
        visited_cells[y_position][1] = True

        cost_start_right = 1 if map_rows[y_position][width] == "#" else 0
        status_start_right = 0 if map_rows[y_position][width] == "#" else 1
        heappush(priority_queue, (cost_start_right, status_start_right, (width, y_position)))
        visited_cells[y_position][width] = True

    if reached_goal_directly:
        print(0)
        continue

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    goal_reached = False

    # Breadth-first search prioritizing lower cost first; prioritize positions inside moats
    while priority_queue and not goal_reached:
        current_cost, current_status, (current_x, current_y) = heappop(priority_queue)

        for delta_x, delta_y in directions:
            next_x = current_x + delta_x
            next_y = current_y + delta_y

            if not visited_cells[next_y][next_x]:
                visited_cells[next_y][next_x] = True
                cell_symbol = map_rows[next_y][next_x]

                if cell_symbol == "&":
                    print(current_cost)
                    goal_reached = True
                    break

                elif cell_symbol == "#":
                    if current_status == 1:
                        heappush(priority_queue, (current_cost + 1, 0, (next_x, next_y)))
                    else:
                        heappush(priority_queue, (current_cost, 0, (next_x, next_y)))

                elif cell_symbol == ".":
                    heappush(priority_queue, (current_cost, 1, (next_x, next_y)))