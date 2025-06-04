from heapq import heappop, heappush
from string import ascii_lowercase as letters

letter_to_index = {letter: index for index, letter in enumerate(letters)}

def parse_cell(cell_str):
    letter, number = cell_str.split("-")
    return (letter_to_index[letter], int(number) - 1)

def solve_path():
    priority_queue = [(0, start_row, start_col)]
    while priority_queue:
        current_cost, current_row, current_col = heappop(priority_queue)
        if (current_row, current_col) == (goal_row, goal_col):
            return current_cost
        if (current_cost, current_row, current_col) in visited_states:
            continue
        visited_states[(current_cost, current_row, current_col)] = True
        for delta_row, delta_col in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            next_row = current_row + delta_row
            next_col = current_col + delta_col
            if 0 <= next_row < rows and 0 <= next_col < cols:
                next_cost = conditions_matrix[next_row][next_col][current_row][current_col] + cost_increment + current_cost
                if field_matrix[next_row][next_col] == 0:
                    heappush(priority_queue, (next_cost, next_row, next_col))
                else:
                    divisor = field_matrix[next_row][next_col]
                    quotient = next_cost / divisor
                    if delta_row == 0:
                        if quotient % 2 == 1:
                            heappush(priority_queue, (next_cost, next_row, next_col))
                    else:
                        if quotient % 2 == 0:
                            heappush(priority_queue, (next_cost, next_row, next_col))

while True:
    rows, cols = map(int, raw_input().split())
    if rows == 0 and cols == 0:
        break

    visited_states = {}
    cost_increment = input()
    field_matrix = [[0] * cols for _ in range(rows)]
    conditions_matrix = [[[[0]*cols for _ in range(rows)] for _ in range(cols)] for _ in range(rows)]

    for _ in range(input()):
        cell_str, value_str = raw_input().split()
        row_index, col_index = parse_cell(cell_str)
        field_matrix[row_index][col_index] = int(value_str)

    for _ in range(input()):
        cell_str_1, cell_str_2 = raw_input().split()
        r1, c1 = parse_cell(cell_str_1)
        r2, c2 = parse_cell(cell_str_2)
        conditions_matrix[r1][c1][r2][c2] = conditions_matrix[r2][c2][r1][c1] = 1 << 30

    for _ in range(input()):
        cell_str_1, cell_str_2, dist_str = raw_input().split()
        r1, c1 = parse_cell(cell_str_1)
        r2, c2 = parse_cell(cell_str_2)
        conditions_matrix[r1][c1][r2][c2] = conditions_matrix[r2][c2][r1][c1] = int(dist_str)

    start_row, start_col = parse_cell(raw_input().split()[0])
    goal_row, goal_col = parse_cell(raw_input().split()[1])
    print solve_path()