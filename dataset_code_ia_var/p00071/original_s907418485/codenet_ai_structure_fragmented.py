def set_bomb_zero(y, x, a):
    a[y][x] = '0'

def get_bomb_positions():
    return [[-3, 0], [-2, 0], [-1, 0], [1, 0], [2, 0], [3, 0],
            [0, -3], [0, -2], [0, -1], [0, 1], [0, 2], [0, 3]]

def is_within_bounds(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def is_one(y, x, a):
    return a[y][x] == '1'

def handle_bomb_explosion(y, x, a):
    set_bomb_zero(y, x, a)
    process_adjacent_bombs(y, x, a)
    return a

def process_adjacent_bombs(y, x, a):
    for dx, dy in get_bomb_positions():
        new_x, new_y = x + dx, y + dy
        if is_within_bounds(new_x, new_y) and is_one(new_y, new_x, a):
            handle_bomb_explosion(new_y, new_x, a)

def get_number_of_cases():
    return int(input())

def skip_empty_input():
    input()

def read_grid():
    return [list(input()) for _ in range(8)]

def read_x():
    return int(input())

def read_y():
    return int(input())

def run_one_case(case_index):
    skip_empty_input()
    grid = read_grid()
    x = read_x()
    y = read_y()
    handle_bomb_explosion(y - 1, x - 1, grid)
    print_case_header(case_index)
    print_grid(grid)

def print_case_header(index):
    print('Data %d:' % (index + 1))

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def main():
    cases = get_number_of_cases()
    for i in range(cases):
        run_one_case(i)

main()