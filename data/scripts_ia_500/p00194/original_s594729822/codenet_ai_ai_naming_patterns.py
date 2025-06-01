from heapq import heappop, heappush
from string import ascii_lowercase as ascii_letters

LETTER_TO_INDEX = {letter: index for index, letter in enumerate(ascii_letters)}

def parse_position(position_str):
    letter, number = position_str.split("-")
    return LETTER_TO_INDEX[letter], int(number) - 1

def solve_minimum_cost_path():
    priority_queue = [(0, start_row, start_col)]
    while priority_queue:
        current_cost, current_row, current_col = heappop(priority_queue)
        if (current_row, current_col) == goal_position:
            return current_cost
        if (current_cost, current_row, current_col) in visited_states:
            continue
        visited_states[(current_cost, current_row, current_col)] = True
        for delta_row, delta_col in ((0,1), (0,-1), (1,0), (-1,0)):
            next_row = current_row + delta_row
            next_col = current_col + delta_col
            if 0 <= next_row < rows_count and 0 <= next_col < cols_count:
                transition_cost = conditions[next_row][next_col][current_row][current_col] + base_cost + current_cost
                if field_map[next_row][next_col] == 0:
                    heappush(priority_queue, (transition_cost, next_row, next_col))
                else:
                    if delta_row == 0:
                        if (transition_cost / field_map[next_row][next_col]) % 2 == 1:
                            heappush(priority_queue, (transition_cost, next_row, next_col))
                    else:
                        if (transition_cost / field_map[next_row][next_col]) % 2 == 0:
                            heappush(priority_queue, (transition_cost, next_row, next_col))

while True:
    rows_count, cols_count = map(int, raw_input().split())
    if rows_count == 0 and cols_count == 0:
        break
    visited_states = {}
    base_cost = input()
    field_map = [[0]*cols_count for _ in xrange(rows_count)]
    conditions = [[[[0]*cols_count for _ in xrange(rows_count)] for _ in xrange(cols_count)] for _ in xrange(rows_count)]
    for _ in xrange(input()):
        position_str, cell_cost = raw_input().split()
        row_idx, col_idx = parse_position(position_str)
        field_map[row_idx][col_idx] = int(cell_cost)
    for _ in xrange(input()):
        pos1_str, pos2_str = raw_input().split()
        row1, col1 = parse_position(pos1_str)
        row2, col2 = parse_position(pos2_str)
        conditions[row1][col1][row2][col2] = conditions[row2][col2][row1][col1] = 1 << 30
    for _ in xrange(input()):
        pos1_str, pos2_str, dist_str = raw_input().split()
        row1, col1 = parse_position(pos1_str)
        row2, col2 = parse_position(pos2_str)
        dist = int(dist_str)
        conditions[row1][col1][row2][col2] = conditions[row2][col2][row1][col1] = dist
    start_position, goal_position = map(parse_position, raw_input().split())
    start_row, start_col = start_position
    print solve_minimum_cost_path()