from heapq import heappop, heappush
from string import ascii_lowercase as ascii_lowercase_letters

# Mapping from lowercase letter to integer index
letter_to_index = dict((letter, index) for index, letter in enumerate(ascii_lowercase_letters))

def position_to_indices(position_tuple):
    letter_part, number_part = position_tuple
    return (letter_to_index[letter_part], int(number_part) - 1)

def convert_position_string(position_string):
    return position_to_indices(position_string.split("-"))

def find_minimum_delivery_cost():
    priority_queue = [(0, start_position_row, start_position_col)]
    while len(priority_queue) != 0:
        current_cost, current_row, current_col = heappop(priority_queue)
        if (current_row, current_col) == goal_position:
            return current_cost
        if (current_cost, current_row, current_col) in visited_states:
            continue
        visited_states[(current_cost, current_row, current_col)] = True
        for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_row = current_row + delta_row
            next_col = current_col + delta_col
            if 0 <= next_row < total_rows and 0 <= next_col < total_columns:
                next_cost = movement_cost[next_row][next_col][current_row][current_col] + base_additional_cost + current_cost
                if field_properties[next_row][next_col] == 0:
                    heappush(priority_queue, (next_cost, next_row, next_col))
                else:
                    if delta_row == 0:
                        if (next_cost / field_properties[next_row][next_col]) % 2 == 1:
                            heappush(priority_queue, (next_cost, next_row, next_col))
                    else:
                        if (next_cost / field_properties[next_row][next_col]) % 2 == 0:
                            heappush(priority_queue, (next_cost, next_row, next_col))

while True:
    total_rows, total_columns = map(int, raw_input().split())
    if total_rows | total_columns == 0:
        break

    visited_states = {}
    base_additional_cost = input()
    field_properties = [[0 for _ in range(total_columns)] for _ in range(total_rows)]
    movement_cost = [[[[0 for _ in range(total_columns)] for _ in range(total_rows)]
                      for _ in range(total_columns)] for _ in range(total_rows)]

    for _ in xrange(input()):
        position_string, property_value = raw_input().split()
        property_row, property_col = convert_position_string(position_string)
        field_properties[property_row][property_col] = int(property_value)

    for _ in xrange(input()):
        first_position_indices, second_position_indices = map(convert_position_string, raw_input().split())
        row1, col1 = first_position_indices
        row2, col2 = second_position_indices
        movement_cost[row1][col1][row2][col2] = movement_cost[row2][col2][row1][col1] = 1 << 30

    for _ in xrange(input()):
        position1_str, position2_str, cost_value = raw_input().split()
        row1, col1 = convert_position_string(position1_str)
        row2, col2 = convert_position_string(position2_str)
        movement_cost[row1][col1][row2][col2] = movement_cost[row2][col2][row1][col1] = int(cost_value)

    start_position_indices, goal_position_indices = map(convert_position_string, raw_input().split())
    start_position_row, start_position_col = start_position_indices
    goal_position = tuple(goal_position_indices)

    print find_minimum_delivery_cost()