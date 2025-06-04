from heapq import heappush as pq_push, heappop as pq_pop

def process_grid():
    grid_height, grid_width = map(int, input().split())
    grid_map = [[-1] + list(input()) + [-1] for _ in range(grid_height)]
    grid_map.insert(0, [-1] * (grid_width + 2))
    grid_map.append([-1] * (grid_width + 2))
    
    frontier = []
    for row_idx in range(1, grid_height + 1):
        for col_idx in range(1, grid_width + 1):
            cell_value = grid_map[row_idx][col_idx]
            if "1" <= cell_value <= "9":
                grid_map[row_idx][col_idx] = int(cell_value)
            elif cell_value == ".":
                grid_map[row_idx][col_idx] = 0
                pq_push(frontier, (0, col_idx, row_idx))
    
    neighbor_offsets = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    last_turn_count = 0
    while frontier:
        current_turn, current_x, current_y = pq_pop(frontier)
        last_turn_count = current_turn
        for offset_x, offset_y in neighbor_offsets:
            neighbor_x = current_x + offset_x
            neighbor_y = current_y + offset_y
            if grid_map[neighbor_y][neighbor_x] > 0:
                grid_map[neighbor_y][neighbor_x] -= 1
                if grid_map[neighbor_y][neighbor_x] == 0:
                    pq_push(frontier, (current_turn + 1, neighbor_x, neighbor_y))
    print(last_turn_count)

process_grid()