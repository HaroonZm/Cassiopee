from collections import defaultdict
import sys

def solve():
    input_line = sys.stdin.readline
    output_write = sys.stdout.write

    direction_to_index = "<v>^".index

    number_of_tiles = int(input_line())
    tiles_by_y_coordinate = defaultdict(list)

    for tile_index in range(number_of_tiles):
        x_str, y_str, direction_char = input_line().split()
        x_coordinate = int(x_str)
        y_coordinate = int(y_str)
        direction_index = direction_to_index(direction_char)
        tiles_by_y_coordinate[y_coordinate].append((x_coordinate, direction_index))

    sorted_y_with_tiles = list(tiles_by_y_coordinate.items())
    sorted_y_with_tiles.sort()  # Sort ascending by y

    direction_from_tile_index = [0] * number_of_tiles  # Stores direction index for each tile
    neighbor_indices = [[-1] * 4 for _ in range(number_of_tiles)]  # Each tile can have up to 4 neighbors (left, up, right, down)

    next_available_tile_index = 0
    last_tile_index_for_x = {}

    for y_coordinate, tiles_in_row in sorted_y_with_tiles:
        tiles_in_row.sort()  # Sort tiles for the same y by x coordinate ascending
        previous_tile_index_in_row = -1

        for x_coordinate, direction_index in tiles_in_row:
            current_tile_neighbors = neighbor_indices[next_available_tile_index]
            direction_from_tile_index[next_available_tile_index] = direction_index

            # Connect to vertical neighbor if x already exists
            if x_coordinate in last_tile_index_for_x:
                above_tile_index = last_tile_index_for_x[x_coordinate]
                current_tile_neighbors[3] = above_tile_index  # 3: Down neighbor is above tile
                neighbor_indices[above_tile_index][1] = next_available_tile_index  # 1: Up neighbor is current
            last_tile_index_for_x[x_coordinate] = next_available_tile_index

            # Connect to horizontal neighbor (previous in this row)
            if previous_tile_index_in_row != -1:
                current_tile_neighbors[0] = previous_tile_index_in_row  # 0: Left neighbor
                neighbor_indices[previous_tile_index_in_row][2] = next_available_tile_index  # 2: Right neighbor is current
            previous_tile_index_in_row = next_available_tile_index

            next_available_tile_index += 1

    max_path_length = 0

    for start_tile_index in range(number_of_tiles):
        current_path_length = 0

        # Make a deep copy of the neighbor indices for this simulation
        simulation_neighbors = [neighbor[:]
                                for neighbor in neighbor_indices]

        current_tile_index = start_tile_index

        while current_tile_index != -1:
            current_direction = direction_from_tile_index[current_tile_index]
            neighbors = simulation_neighbors[current_tile_index]
            left_neighbor, up_neighbor, right_neighbor, down_neighbor = neighbors

            # Remove current tile by linking neighbors together
            if left_neighbor != -1:
                simulation_neighbors[left_neighbor][2] = right_neighbor
            if up_neighbor != -1:
                simulation_neighbors[up_neighbor][3] = down_neighbor
            if right_neighbor != -1:
                simulation_neighbors[right_neighbor][0] = left_neighbor
            if down_neighbor != -1:
                simulation_neighbors[down_neighbor][1] = up_neighbor

            current_path_length += 1
            current_tile_index = neighbors[current_direction]

        if current_path_length > max_path_length:
            max_path_length = current_path_length

    output_write("%d\n" % max_path_length)

solve()