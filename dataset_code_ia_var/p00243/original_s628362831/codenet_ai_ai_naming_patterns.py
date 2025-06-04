from collections import deque
import sys

def fill_region(region_state, adjacency_dict, target_color):
    filled_count = 0
    original_color = region_state[0]
    pending_positions = [0]
    for current_position in pending_positions:
        if region_state[current_position] == original_color:
            region_state[current_position] = target_color
            filled_count += 1
            pending_positions.extend(adjacency_dict[current_position])
    return filled_count

def minimal_recolor_operations(state_list, adjacency_dict):
    bfs_queue = deque([(state_list, 0, 0)])
    while True:
        current_state, prev_filled_count, current_depth = bfs_queue.popleft()
        current_color = current_state[0]

        possible_colors = ['R', 'G', 'B']
        possible_colors.remove(current_color)

        for candidate_state, next_color in zip((current_state, current_state[:]), possible_colors):
            region_filled_count = fill_region(candidate_state, adjacency_dict, next_color)
            if region_filled_count == len(candidate_state):
                return current_depth
            if region_filled_count == prev_filled_count:
                break
            bfs_queue.append((candidate_state, region_filled_count, current_depth + 1))

def extract_neighbors(map_state, target_color, map_width, map_height, start_x, start_y):
    neighboring_region_indices = set()
    original_color = map_state[start_y * map_width + start_x]
    positions_to_process = deque([(start_x, start_y)])
    while len(positions_to_process):
        current_x, current_y = positions_to_process.pop()
        position_index = current_y * map_width + current_x
        if map_state[position_index] == original_color:
            map_state[position_index] = target_color
            if current_x > 0:
                positions_to_process.append((current_x - 1, current_y))
            if current_y > 0:
                positions_to_process.append((current_x, current_y - 1))
            if current_x + 1 < map_width:
                positions_to_process.append((current_x + 1, current_y))
            if current_y + 1 < map_height:
                positions_to_process.append((current_x, current_y + 1))
        elif map_state[position_index] != target_color and isinstance(map_state[position_index], int):
            neighboring_region_indices.update([map_state[position_index]])
    return neighboring_region_indices

def main():
    input_stream = sys.stdin
    while True:
        map_width, map_height = map(int, input_stream.readline().split())
        if map_width == 0 and map_height == 0:
            break
        raw_grid = [input_stream.readline().split() for _ in range(map_height)]
        flat_grid = [cell for row in raw_grid for cell in row]
        region_list = []
        adjacency_dict = {}
        for current_y in range(map_height):
            for current_x in range(map_width):
                cell_index = current_y * map_width + current_x
                if flat_grid[cell_index] in ('R', 'G', 'B'):
                    region_id = len(region_list)
                    region_list.append(flat_grid[cell_index])
                    neighbor_indices = extract_neighbors(flat_grid, region_id, map_width, map_height, current_x, current_y)
                    neighbor_indices = list(neighbor_indices)
                    try:
                        adjacency_dict[region_id].extend(neighbor_indices)
                    except KeyError:
                        adjacency_dict[region_id] = neighbor_indices
                    for neighbor_id in neighbor_indices:
                        try:
                            adjacency_dict[neighbor_id].append(region_id)
                        except KeyError:
                            adjacency_dict[neighbor_id] = [region_id]
        print(minimal_recolor_operations(region_list, adjacency_dict))

main()