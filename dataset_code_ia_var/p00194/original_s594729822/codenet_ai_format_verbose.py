from heapq import heappop, heappush
from string import ascii_lowercase as ascii_letters_lowercase

# Mapping each letter to an integer (horizontal coordinate to index)
column_letter_to_index_map = dict((letter, index) for index, letter in enumerate(ascii_letters_lowercase))

# Function to convert position string to (row, column) tuple
def parse_position(position_string):
    column_letter, row_number = position_string
    return (column_letter_to_index_map[column_letter], int(row_number) - 1)

# Function to split and parse position string of format "x-y"
def parse_position_with_split(position_with_dash):
    return parse_position(position_with_dash.split("-"))

def find_minimum_delivery_cost():
    priority_queue = [(0, start_position[0], start_position[1])]

    while priority_queue:
        current_cost, current_row, current_column = heappop(priority_queue)

        if (current_row, current_column) == goal_position:
            return current_cost

        if (current_cost, current_row, current_column) in visited_state_memo:
            continue

        visited_state_memo[(current_cost, current_row, current_column)] = True

        for row_offset, column_offset in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_row = current_row + row_offset
            next_column = current_column + column_offset

            if 0 <= next_row < grid_row_count and 0 <= next_column < grid_column_count:
                movement_additional_cost = movement_condition_cost[next_row][next_column][current_row][current_column] + movement_time_cost + current_cost

                if field_speed_factor[next_row][next_column] == 0:
                    heappush(priority_queue, (movement_additional_cost, next_row, next_column))
                else:
                    if row_offset == 0:
                        if (movement_additional_cost // field_speed_factor[next_row][next_column]) % 2 == 1:
                            heappush(priority_queue, (movement_additional_cost, next_row, next_column))
                    else:
                        if (movement_additional_cost // field_speed_factor[next_row][next_column]) % 2 == 0:
                            heappush(priority_queue, (movement_additional_cost, next_row, next_column))

while True:
    grid_row_count, grid_column_count = map(int, raw_input().split())
    if grid_row_count == 0 and grid_column_count == 0:
        break

    visited_state_memo = {}

    movement_time_cost = input()
    field_speed_factor = [[0] * grid_column_count for _ in xrange(grid_row_count)]
    movement_condition_cost = [[[[0] * grid_column_count for _ in xrange(grid_row_count)] for _ in xrange(grid_column_count)] for _ in xrange(grid_row_count)]

    special_cells_count = input()
    for _ in xrange(special_cells_count):
        cell_position_string, field_factor_value = raw_input().split()
        cell_row, cell_column = parse_position_with_split(cell_position_string)
        field_speed_factor[cell_row][cell_column] = int(field_factor_value)

    infinite_cost_cells_count = input()
    for _ in xrange(infinite_cost_cells_count):    
        (cell1_row, cell1_column), (cell2_row, cell2_column) = map(parse_position_with_split, raw_input().split())
        movement_condition_cost[cell1_row][cell1_column][cell2_row][cell2_column] = movement_condition_cost[cell2_row][cell2_column][cell1_row][cell1_column] = 1 << 30

    explicit_cost_cells_count = input()
    for _ in xrange(explicit_cost_cells_count):
        cell1_position, cell2_position, explicit_cost_value = raw_input().split()
        cell1_row, cell1_column = parse_position_with_split(cell1_position)
        cell2_row, cell2_column = parse_position_with_split(cell2_position)
        movement_condition_cost[cell1_row][cell1_column][cell2_row][cell2_column] = movement_condition_cost[cell2_row][cell2_column][cell1_row][cell1_column] = int(explicit_cost_value)

    start_position, goal_position = map(parse_position_with_split, raw_input().split())
    print find_minimum_delivery_cost()