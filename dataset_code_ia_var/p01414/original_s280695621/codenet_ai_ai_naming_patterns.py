from collections import deque

input_tile_count = int(input())
grid_height = grid_width = 4
all_filled_mask = 1 << 16
tile_size_list = [list(map(int, input().split())) for tile_index in range(input_tile_count)]
grid_color_strs = [input() for row_index in range(grid_height)]
color_to_index = "RGB".index
placement_set = set()
for tile_index in range(input_tile_count):
    tile_height, tile_width = tile_size_list[tile_index]
    for start_row in range(1 - tile_height, grid_height):
        place_row = max(0, start_row); place_height = min(grid_height, start_row + tile_height) - place_row
        for start_col in range(1 - tile_width, grid_width):
            place_col = max(0, start_col); place_width = min(grid_width, start_col + tile_width) - place_col
            placement_set.add((place_col, place_row, place_width, place_height))
placement_count = len(placement_set)
mask_list = [0] * placement_count
color_mask_list = [None] * placement_count
for placement_index, (x_pos, y_pos, width, height) in enumerate(placement_set):
    base_mask = all_filled_mask - 1
    base_color_masks = [0] * 3
    for dy in range(height):
        for dx in range(width):
            bit_pos = 1 << ((y_pos + dy) * grid_width + (x_pos + dx))
            base_mask ^= bit_pos
            color_idx = color_to_index(grid_color_strs[y_pos + dy][x_pos + dx])
            base_color_masks[color_idx] |= bit_pos
    mask_list[placement_index] = base_mask
    color_mask_list[placement_index] = base_color_masks

state_min_step_list = [-1] * all_filled_mask
bfs_queue = deque([0])
state_min_step_list[0] = 0
while bfs_queue:
    current_state = bfs_queue.popleft()
    current_step = state_min_step_list[current_state]
    for placement_index in range(placement_count):
        next_state_base = current_state & mask_list[placement_index]
        for this_color_mask in color_mask_list[placement_index]:
            if this_color_mask == 0:
                continue
            candidate_state = next_state_base | this_color_mask
            if state_min_step_list[candidate_state] != -1:
                continue
            state_min_step_list[candidate_state] = current_step + 1
            bfs_queue.append(candidate_state)
print(state_min_step_list[all_filled_mask - 1])