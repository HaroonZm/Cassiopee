def read_inputs():
    return parse_input(input())

def parse_input(input_str):
    return map_inputs(map(int, input_str.split()))

def map_inputs(inputs):
    return tuple(inputs)

def get_grid_height():
    return 100

def get_grid_width():
    return 100

def create_empty_row():
    return ['.'] * get_grid_width()

def create_filled_row():
    return ['#'] * get_grid_width()

def generate_upper_half():
    return [create_empty_row() for _ in range(get_grid_height() // 2)]

def generate_lower_half():
    return [create_filled_row() for _ in range(get_grid_height() // 2)]

def combine_halves(upper, lower):
    return upper + lower

def initialize_grid():
    upper = generate_upper_half()
    lower = generate_lower_half()
    return combine_halves(upper, lower)

def get_index_tuple(n, base):
    return divmod(n, base)

def set_island(grid, a):
    for i in range(a):
        ai, aj = get_index_tuple(i, 50)
        set_grid_sharp(grid, ai, aj)

def set_grid_sharp(grid, ai, aj):
    x, y = 2 * ai, 2 * aj
    grid[x][y] = '#'

def set_lake(grid, b):
    for i in range(b):
        bi, bj = get_index_tuple(i, 50)
        set_grid_dot(grid, bi, bj)

def set_grid_dot(grid, bi, bj):
    x, y = 2 * bi + 51, 2 * bj
    grid[x][y] = '.'

def print_grid(grid):
    print(get_grid_height(), get_grid_width())
    for row in grid:
        print(''.join(row))

def main():
    B, A = read_inputs()
    grid = initialize_grid()
    set_island(grid, A - 1)
    set_lake(grid, B - 1)
    print_grid(grid)

main()