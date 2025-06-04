from heapq import heappush, heappop
from string import digits
import sys

read_line_from_stdin = sys.stdin.readline
write_to_stdout = sys.stdout.write

directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
INFINITY = 10 ** 9

while True:
    grid_width, grid_height = map(int, read_line_from_stdin().split())
    if grid_width == 0 and grid_height == 0:
        break

    map_grid = [read_line_from_stdin().split() for _ in range(grid_height)]
    number_of_items = int(read_line_from_stdin())
    item_info_by_digit = [[] for _ in range(10)]

    for item_index in range(number_of_items):
        group, value, start_time, end_time = map(int, read_line_from_stdin().split())
        if start_time < end_time:
            item_info_by_digit[group].append((item_index, value, start_time, end_time))

    for item_group_info in item_info_by_digit:
        item_group_info.sort(key=lambda x: x[1])

    collected_value_for_state = [0] * (1 << number_of_items)
    for state_bitmask in range(1 << number_of_items):
        total_value = 0
        for item_group_info in item_info_by_digit:
            highest_value_in_group = 0
            for item_index, value, start_time, end_time in item_group_info:
                if state_bitmask & (1 << item_index):
                    highest_value_in_group = value
            total_value += highest_value_in_group
        collected_value_for_state[state_bitmask] = total_value

    available_items_adjacent = [[None] * grid_width for _ in range(grid_height)]
    start_x = start_y = 0

    for row in range(grid_height):
        for col in range(grid_width):
            cell_content = map_grid[row][col]
            if cell_content in digits:
                continue
            if cell_content == 'P':
                start_y = row
                start_x = col
            adjacent_items_set = set()
            for dx, dy in directions:
                neighbor_col = col + dx
                neighbor_row = row + dy
                if not (0 <= neighbor_col < grid_width and 0 <= neighbor_row < grid_height):
                    continue
                neighbor_cell_content = map_grid[neighbor_row][neighbor_col]
                if neighbor_cell_content in digits:
                    for item_info in item_info_by_digit[int(neighbor_cell_content)]:
                        adjacent_items_set.add(item_info)
            available_items_adjacent[row][col] = adjacent_items_set

    min_time_to_state = [[[INFINITY] * (1 << number_of_items) for _ in range(grid_width)] for _ in range(grid_height)]
    priority_queue = [(0, 0, start_x, start_y)]
    min_time_to_state[start_y][start_x][0] = 0

    while priority_queue:
        current_time, collected_state, current_x, current_y = heappop(priority_queue)
        min_time_for_current_position = min_time_to_state[current_y][current_x]
        current_min_time = min_time_for_current_position[collected_state]
        if current_min_time < current_time:
            continue

        for item_index, value, start_time, end_time in available_items_adjacent[current_y][current_x]:
            if current_min_time < end_time and not (collected_state & (1 << item_index)):
                possible_start_time = max(start_time, current_min_time)
                new_collected_state = collected_state | (1 << item_index)
                if possible_start_time < min_time_for_current_position[new_collected_state]:
                    min_time_for_current_position[new_collected_state] = possible_start_time
                    heappush(priority_queue, (possible_start_time, new_collected_state, current_x, current_y))

        for dx, dy in directions:
            neighbor_x = current_x + dx
            neighbor_y = current_y + dy
            if not (0 <= neighbor_x < grid_width and 0 <= neighbor_y < grid_height):
                continue
            if available_items_adjacent[neighbor_y][neighbor_x] is None:
                continue
            if current_min_time + 1 < min_time_to_state[neighbor_y][neighbor_x][collected_state]:
                min_time_to_state[neighbor_y][neighbor_x][collected_state] = current_min_time + 1
                heappush(priority_queue, (current_min_time + 1, collected_state, neighbor_x, neighbor_y))

    maximum_collected_value = 0
    for x in range(grid_width):
        for y in range(grid_height):
            min_time_list_for_pos = min_time_to_state[y][x]
            for collected_state in range(1 << number_of_items):
                if min_time_list_for_pos[collected_state] < INFINITY:
                    maximum_collected_value = max(maximum_collected_value, collected_value_for_state[collected_state])

    write_to_stdout("%d\n" % maximum_collected_value)