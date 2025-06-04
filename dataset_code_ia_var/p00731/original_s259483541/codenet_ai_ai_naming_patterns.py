import heapq

MOVE_RIGHT_PATTERN = tuple((dx, dy) for dx in range(-3, 0) for dy in range(-2, 3) if abs(dx) + abs(dy) <= 3)
MOVE_LEFT_PATTERN = tuple((dx, dy) for dx in range(1, 4) for dy in range(-2, 3) if abs(dx) + abs(dy) <= 3)
DIGIT_CHARS = tuple(str(num) for num in range(10))
SIDE_LEFT, SIDE_RIGHT = 0, 1
VALUE_INF = 10 ** 20

def cell_value(cell_char):
    if cell_char in DIGIT_CHARS:
        return int(cell_char)
    if cell_char in ("T", "S"):
        return 0
    return -1

while True:
    width, height = map(int, input().split())
    if width == 0:
        break

    grid_raw = [ [-1]*3 + input().split() + [-1]*3 for _ in range(height) ]
    grid = [ list(map(cell_value, row)) for row in grid_raw ]
    grid = [ [-1]*(width+6), [-1]*(width+6) ] + grid + [ [-1]*(width+6), [-1]*(width+6) ]

    def solve_min_path_cost():
        start_positions = []
        goal_positions = []
        for col in range(3, width+3):
            if grid[height+1][col] == 0:
                start_positions.append( (col, height+1) )
            if grid[2][col] == 0:
                goal_positions.append( (col, 2) )

        search_queue = []
        visited_cost = {}
        for sx, sy in start_positions:
            heapq.heappush(search_queue, (0, sx, sy, SIDE_LEFT))
            heapq.heappush(search_queue, (0, sx, sy, SIDE_RIGHT))
            visited_cost[(sx, sy, SIDE_LEFT)] = 0
            visited_cost[(sx, sy, SIDE_RIGHT)] = 0

        while search_queue:
            curr_cost, curr_x, curr_y, curr_side = heapq.heappop(search_queue)
            if curr_side == SIDE_RIGHT:
                move_pattern = MOVE_RIGHT_PATTERN
                next_side = SIDE_LEFT
            else:
                move_pattern = MOVE_LEFT_PATTERN
                next_side = SIDE_RIGHT

            for dx, dy in move_pattern:
                next_x, next_y = curr_x + dx, curr_y + dy
                if (next_x, next_y) in goal_positions:
                    return curr_cost
                next_cell_cost = grid[next_y][next_x]
                if next_cell_cost == -1:
                    continue
                visited_index = (next_x, next_y, next_side)
                total_next_cost = curr_cost + next_cell_cost
                if visited_index not in visited_cost or visited_cost[visited_index] > total_next_cost:
                    visited_cost[visited_index] = total_next_cost
                    heapq.heappush(search_queue, (total_next_cost, next_x, next_y, next_side))
        return -1

    print(solve_min_path_cost())