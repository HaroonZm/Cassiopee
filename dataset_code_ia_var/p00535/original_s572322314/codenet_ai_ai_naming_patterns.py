import heapq

input_height, input_width = map(int, input().split())
grid_map = [[-1] + list(input()) + [-1] for _ in range(input_height)]
grid_map.insert(0, [-1] * (input_width + 2))
grid_map.append([-1] * (input_width + 2))

priority_queue = []
for row_idx in range(1, input_height + 1):
    for col_idx in range(1, input_width + 1):
        cell_value = grid_map[row_idx][col_idx]
        if "1" <= cell_value <= "9":
            grid_map[row_idx][col_idx] = int(cell_value)
        elif cell_value == ".":
            grid_map[row_idx][col_idx] = 0
            heapq.heappush(priority_queue, (0, col_idx, row_idx))

neighbor_offsets = ((0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1))

while priority_queue:
    current_turn, current_col, current_row = heapq.heappop(priority_queue)
    for offset_col, offset_row in neighbor_offsets:
        neighbor_col = current_col + offset_col
        neighbor_row = current_row + offset_row
        if grid_map[neighbor_row][neighbor_col] > 0:
            grid_map[neighbor_row][neighbor_col] -= 1
            if grid_map[neighbor_row][neighbor_col] == 0:
                heapq.heappush(priority_queue, (current_turn + 1, neighbor_col, neighbor_row))

print(current_turn)