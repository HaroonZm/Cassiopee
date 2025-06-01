import queue

direction_row = [0, 1, 0, -1]
direction_col = [1, 0, -1, 0]

while True:

    width, height = map(int, input().split())

    if width == 0:
        break

    allowed_fatigue, max_fatigue, starting_fatigue_index = map(int, input().split())

    floor_map = [list(map(int, input().split())) for _ in range(height)]

    # Initialize 3D distance array: fatigue_level x height x width
    fatigue_costs = [[[1e9] * width for _ in range(height)] for _ in range(max_fatigue + 1)]

    priority_queue = queue.PriorityQueue()

    # Set starting positions in the top row for the initial fatigue state
    for column_index in range(width):
        initial_cost = -min(0, floor_map[0][column_index])
        fatigue_costs[starting_fatigue_index - 1][0][column_index] = initial_cost
        priority_queue.put((initial_cost, starting_fatigue_index - 1, 0, column_index))

    while not priority_queue.empty():

        current_cost, fatigue_state, current_row, current_col = priority_queue.get()

        # Skip if cost already updated to a better one or if fatigue state too low
        if fatigue_costs[fatigue_state][current_row][current_col] < current_cost or fatigue_state <= 1:
            continue

        # Explore all four directions
        for direction_index in range(4):

            next_row = current_row + direction_row[direction_index]
            next_col = current_col + direction_col[direction_index]

            # Check bounds
            if next_row < 0 or next_row >= height or next_col < 0 or next_col >= width:
                continue

            cell_value = floor_map[next_row][next_col]

            if cell_value < 0:
                # Going downwards: fatigue decreases by abs(cell_value)
                new_fatigue_state = fatigue_state - 1
                new_cost = fatigue_costs[fatigue_state][current_row][current_col] - cell_value

                if fatigue_costs[new_fatigue_state][next_row][next_col] > new_cost:
                    fatigue_costs[new_fatigue_state][next_row][next_col] = new_cost
                    priority_queue.put((new_cost, new_fatigue_state, next_row, next_col))

            else:
                # Going upwards or flat: fatigue increases but capped by max_fatigue
                new_fatigue_state = min(fatigue_state - 1 + cell_value, max_fatigue)
                new_cost = fatigue_costs[fatigue_state][current_row][current_col]

                if fatigue_costs[new_fatigue_state][next_row][next_col] > new_cost:
                    fatigue_costs[new_fatigue_state][next_row][next_col] = new_cost
                    priority_queue.put((new_cost, new_fatigue_state, next_row, next_col))

    minimum_cost = 1e9

    # Find the minimum cost to reach the bottom row with any valid fatigue state
    for column_index in range(width):
        for fatigue_state in range(1, max_fatigue + 1):
            if fatigue_costs[fatigue_state][height - 1][column_index] < minimum_cost:
                minimum_cost = fatigue_costs[fatigue_state][height - 1][column_index]

    if minimum_cost <= allowed_fatigue:
        print(minimum_cost)
    else:
        print('NA')