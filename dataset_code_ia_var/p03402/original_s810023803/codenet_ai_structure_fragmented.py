def read_input():
    return map(int, input().split())

def create_grid(char, rows, cols):
    return [[char] * cols for _ in range(rows)]

def place_blocks_on_grid(grid, count, place_char, start_ny, other_char):
    nx = 0
    ny = start_ny
    for _ in range(count):
        set_cell(grid, ny, nx, place_char)
        nx, ny = get_next_position(nx, ny, len(grid[0]))
    return grid

def set_cell(grid, y, x, char):
    grid[y][x] = char

def get_next_position(nx, ny, column_limit):
    nx += 2
    if nx >= column_limit:
        nx = 0
        ny += 2
    return nx, ny

def print_grid_dimensions(rows, cols):
    print(f"{rows},{cols}".replace(',', ' '))

def print_grid(grid):
    for row in grid:
        print("".join(row))

def generate_grids(A, B):
    rows = 100
    half = rows // 2
    cols = 100
    gridA = create_grid(".", half, cols)
    gridB = create_grid("#", half, cols)
    gridA = place_blocks_on_grid(gridA, B-1, "#", 0, ".")
    gridB = place_blocks_on_grid(gridB, A-1, ".", 1, "#")
    return gridA, gridB

def merge_and_print_grids(gridA, gridB):
    print_grid_dimensions(len(gridA) + len(gridB), len(gridA[0]))
    print_grid(gridA)
    print_grid(gridB)

def main():
    A, B = read_input()
    gridA, gridB = generate_grids(A, B)
    merge_and_print_grids(gridA, gridB)

main()