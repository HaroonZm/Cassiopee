from collections import Counter

total_tiles, max_distance, modulo = map(int, input().split())

dynamic_program_table = [Counter() for _ in range(2 * total_tiles)]

# Initial state: no tile placed on the left, only base at position 0
dynamic_program_table[0][(None, (0,))] = 1

for current_position in range(2 * total_tiles - 1):

    for (last_tile_on_left, tiles_on_top_stack), current_count in dynamic_program_table[current_position].items():

        if len(tiles_on_top_stack) > max_distance + 1:
            continue

        # Place a horizontal tile to the left, if possible
        if last_tile_on_left is None:
            if tiles_on_top_stack and current_position + 1 - tiles_on_top_stack[0] <= max_distance:
                new_key = (current_position + 1, tiles_on_top_stack)
                dynamic_program_table[current_position + 1][new_key] = (
                    dynamic_program_table[current_position + 1][new_key] + current_count
                ) % modulo

        # Place a horizontal tile on top, if possible
        elif (current_position + 1 - last_tile_on_left <= max_distance) and \
             len(tiles_on_top_stack) > 1 and (current_position + 1 - tiles_on_top_stack[1] <= max_distance):

            new_key = (current_position + 1, tiles_on_top_stack[1:])
            dynamic_program_table[current_position + 1][new_key] = (
                dynamic_program_table[current_position + 1][new_key] + current_count
            ) % modulo

        # Place a vertical tile, if possible
        if tiles_on_top_stack and (current_position + 1 - tiles_on_top_stack[-1] <= max_distance):
            extended_tiles_on_top_stack = list(tiles_on_top_stack)
            extended_tiles_on_top_stack.append(current_position + 1)
            new_tiles_on_top_stack = tuple(extended_tiles_on_top_stack)
            new_key = (last_tile_on_left, new_tiles_on_top_stack)
            dynamic_program_table[current_position + 1][new_key] = (
                dynamic_program_table[current_position + 1][new_key] + current_count
            ) % modulo

final_result = 0

for (last_tile_on_left, tiles_on_top_stack), ways_count in dynamic_program_table[2 * total_tiles - 1].items():

    if len(tiles_on_top_stack) == 1:
        assert last_tile_on_left == 2 * total_tiles - 1
        final_result = (final_result + ways_count) % modulo

print(final_result)