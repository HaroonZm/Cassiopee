def get_input():
    return int(input())

def create_empty_grid(n):
    return [[" " for _ in range(n)] for _ in range(n)]

def set_first_column_hash(grid, n):
    for i in range(n):
        grid[i][0] = "#"

def compute_step_length(n, m):
    return n - 1 - (m // 2) * 2

def move_position(x, y, d):
    if d == 0:
        y -= 1
    elif d == 1:
        x += 1
    elif d == 2:
        y += 1
    elif d == 3:
        x -= 1
    return x, y

def update_grid(grid, x, y):
    grid[y][x] = "#"

def print_row(row):
    for c in row:
        print(c, end="")
    print("")

def print_grid(grid):
    for r in grid:
        print_row(r)

def process_spiral(n):
    grid = create_empty_grid(n)
    set_first_column_hash(grid, n)
    d = 1
    x, y = 0, 0
    for m in range(n - 1):
        l = compute_step_length(n, m)
        for _ in range(l):
            x, y = move_position(x, y, d)
            update_grid(grid, x, y)
        d = (d + 1) % 4
    return grid

def main():
    a = get_input()
    for j in range(a):
        n = get_input()
        grid = process_spiral(n)
        print_grid(grid)
        if j != a - 1:
            print("")

main()