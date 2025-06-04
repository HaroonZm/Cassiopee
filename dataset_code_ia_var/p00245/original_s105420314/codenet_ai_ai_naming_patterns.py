import sys
from heapq import heappush, heappop
from string import digits

CONST_INF = 10**9
CONST_DIRS = ((-1, 0), (0, -1), (1, 0), (0, 1))

input_read = sys.stdin.readline
output_write = sys.stdout.write

while True:
    grid_width, grid_height = map(int, input_read().split())
    if grid_width == 0 and grid_height == 0:
        break

    grid_map = [input_read().split() for _ in range(grid_height)]
    num_items = int(input_read())
    time_gates = [[] for _ in range(10)]
    for item_idx in range(num_items):
        gate_type, gate_duration, gate_start, gate_end = map(int, input_read().split())
        if gate_start < gate_end:
            time_gates[gate_type].append((item_idx, gate_duration, gate_start, gate_end))
    for gate_type_list in time_gates:
        gate_type_list.sort(key=lambda elem: elem[1])

    value_by_mask = [0] * (1 << num_items)
    for bitmask in range(1 << num_items):
        value = 0
        for gate_type_list in time_gates:
            gate_best_duration = 0
            for idx, duration, start, end in gate_type_list:
                if bitmask & (1 << idx):
                    gate_best_duration = duration
            value += gate_best_duration
        value_by_mask[bitmask] = value

    unlock_set_grid = [[None] * grid_width for _ in range(grid_height)]
    player_x = player_y = 0
    for row_idx in range(grid_height):
        for col_idx in range(grid_width):
            cell_val = grid_map[row_idx][col_idx]
            if cell_val in digits:
                continue
            if cell_val == 'P':
                player_y, player_x = row_idx, col_idx
            unlock_set = set()
            for dx, dy in CONST_DIRS:
                nbr_x = col_idx + dx
                nbr_y = row_idx + dy
                if not (0 <= nbr_x < grid_width and 0 <= nbr_y < grid_height):
                    continue
                nbr_cell_val = grid_map[nbr_y][nbr_x]
                if nbr_cell_val in digits:
                    for gate in time_gates[int(nbr_cell_val)]:
                        unlock_set.add(gate)
            unlock_set_grid[row_idx][col_idx] = unlock_set

    dist = [[[CONST_INF] * (1 << num_items) for _ in range(grid_width)] for _ in range(grid_height)]
    pq = [(0, 0, player_x, player_y)]
    dist[player_y][player_x][0] = 0
    while pq:
        cost_curr, state_curr, x_curr, y_curr = heappop(pq)
        state_dist = dist[y_curr][x_curr]
        time_at_state = state_dist[state_curr]
        if time_at_state < cost_curr:
            continue
        for idx, duration, start, end in unlock_set_grid[y_curr][x_curr]:
            if time_at_state < end and not (state_curr & (1 << idx)):
                trigger_time = max(start, time_at_state)
                next_state = state_curr | (1 << idx)
                if trigger_time < state_dist[next_state]:
                    state_dist[next_state] = trigger_time
                    heappush(pq, (trigger_time, next_state, x_curr, y_curr))
        for dx, dy in CONST_DIRS:
            nbr_x, nbr_y = x_curr + dx, y_curr + dy
            if not (0 <= nbr_x < grid_width and 0 <= nbr_y < grid_height):
                continue
            if unlock_set_grid[nbr_y][nbr_x] is None:
                continue
            if time_at_state + 1 < dist[nbr_y][nbr_x][state_curr]:
                dist[nbr_y][nbr_x][state_curr] = time_at_state + 1
                heappush(pq, (time_at_state + 1, state_curr, nbr_x, nbr_y))

    max_value = 0
    for col_idx in range(grid_width):
        for row_idx in range(grid_height):
            cell_dist = dist[row_idx][col_idx]
            for mask in range(1 << num_items):
                if cell_dist[mask] < CONST_INF:
                    max_value = max(max_value, value_by_mask[mask])
    output_write("%d\n" % max_value)