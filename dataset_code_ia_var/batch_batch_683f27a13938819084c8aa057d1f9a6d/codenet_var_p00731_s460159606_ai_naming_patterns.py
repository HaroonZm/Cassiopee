from heapq import heappush, heappop

DIR_RIGHT_NEXT = tuple((dx, dy) for dx in range(-3, 0) for dy in range(-2, 3) if abs(dx) + abs(dy) <= 3)
DIR_LEFT_NEXT = tuple((dx, dy) for dx in range(1, 4) for dy in range(-2, 3) if abs(dx) + abs(dy) <= 3)
DIGIT_CHARS = tuple(str(num) for num in range(10))
FOOT_LEFT, FOOT_RIGHT = 0, 1
COST_INFINITY = 10 ** 20

def parse_tile(char):
    if char in DIGIT_CHARS:
        return int(char)
    if char in ("T", "S"):
        return 0
    return -1

while True:
    inp_width, inp_height = map(int, input().split())
    if inp_width == 0:
        break

    grid_matrix = [[-1] * 3 + input().split() + [-1] * 3 for _ in range(inp_height)]
    for row_index in range(inp_height):
        grid_matrix[row_index] = list(map(parse_tile, grid_matrix[row_index]))
    grid_matrix.insert(0, [-1] * (inp_width + 6))
    grid_matrix.insert(0, [-1] * (inp_width + 6))
    grid_matrix.append([-1] * (inp_width + 6))
    grid_matrix.append([-1] * (inp_width + 6))

    start_tiles = []
    goal_tiles = []

    for grid_x in range(3, inp_width + 3):
        if grid_matrix[inp_height + 1][grid_x] == 0:
            start_tiles.append((grid_x, inp_height + 1))
        if grid_matrix[2][grid_x] == 0:
            goal_tiles.append((grid_x, 2))

    state_queue = []
    state_cost = {}
    for sx, sy in start_tiles:
        heappush(state_queue, (0, sx, sy, FOOT_LEFT))
        heappush(state_queue, (0, sx, sy, FOOT_RIGHT))
        state_cost[(sx, sy, FOOT_LEFT)] = 0
        state_cost[(sx, sy, FOOT_RIGHT)] = 0

    while state_queue:
        accum_cost, curr_x, curr_y, curr_foot = heappop(state_queue)
        if curr_foot == FOOT_RIGHT:
            movement_deltas = DIR_RIGHT_NEXT
            next_foot = FOOT_LEFT
        else:
            movement_deltas = DIR_LEFT_NEXT
            next_foot = FOOT_RIGHT

        for delta_x, delta_y in movement_deltas:
            next_x = curr_x + delta_x
            next_y = curr_y + delta_y
            step_cost = grid_matrix[next_y][next_x]
            if step_cost == -1:
                continue
            state_key = (next_x, next_y, next_foot)
            if state_key not in state_cost or state_cost[state_key] > accum_cost + step_cost:
                state_cost[state_key] = accum_cost + step_cost
                heappush(state_queue, (accum_cost + step_cost, next_x, next_y, next_foot))

    min_total_cost = COST_INFINITY
    for gx, gy in goal_tiles:
        for test_foot in (FOOT_LEFT, FOOT_RIGHT):
            key = (gx, gy, test_foot)
            if key in state_cost:
                if state_cost[key] < min_total_cost:
                    min_total_cost = state_cost[key]
    if min_total_cost == COST_INFINITY:
        print(-1)
    else:
        print(min_total_cost)