MAX_X = 2000
MAX_Y = 2000

def create_grid(width, height):
    return [[0 for _ in range(width)] for _ in range(height)]

def read_rectangle():
    return map(int, input().split())

def update_grid_with_rectangle(grid, x, y, w, h):
    for i in range(x, x + w):
        for j in range(y, y + h):
            increment_cell(grid, i, j)

def increment_cell(grid, i, j):
    grid[i][j] += 1

def count_cells_with_value_one(grid, width, height):
    count = 0
    for i in range(width):
        count += count_row_cells_with_value_one(grid, i, height)
    return count

def count_row_cells_with_value_one(grid, row, height):
    count = 0
    for j in range(height):
        count += is_cell_value_one(grid, row, j)
    return count

def is_cell_value_one(grid, i, j):
    return 1 if grid[i][j] == 1 else 0

def main():
    grid = create_grid(MAX_X, MAX_Y)
    read_and_update_rectangles(grid, 2)
    result = count_cells_with_value_one(grid, MAX_X, MAX_Y)
    print(result)

def read_and_update_rectangles(grid, number):
    for _ in range(number):
        x, y, w, h = read_rectangle()
        update_grid_with_rectangle(grid, x, y, w, h)

main()