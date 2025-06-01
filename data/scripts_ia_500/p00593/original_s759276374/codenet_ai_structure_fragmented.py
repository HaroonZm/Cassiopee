def read_input():
    return int(input())

def create_grid(n):
    return [[0]*n for _ in range(n)]

def set_value(grid, y, x, value):
    grid[y][x] = value

def can_move_right(x, n):
    return x < n -1

def can_move_down(y, n):
    return y < n -1

def can_move_up(y):
    return y > 0

def can_move_left(x):
    return x > 0

def move_right(x):
    return x + 1

def move_down(y):
    return y + 1

def move_up(y):
    return y - 1

def move_left(x):
    return x - 1

def fill_single_cell(grid, y, x):
    set_value(grid, y, x, 1)

def fill_starting_positions(grid, y, x, value, n):
    set_value(grid, y, x, value)
    if can_move_right(x, n):
        x = move_right(x)
        value +=1
        set_value(grid, y, x, value)
    else:
        y = move_down(y)
        value +=1
        set_value(grid, y, x, value)
    return y, x, value

def fill_diagonal_down(grid, y, x, value, n):
    while x >0 and can_move_down(y, n):
        y = move_down(y)
        x = move_left(x)
        value += 1
        set_value(grid, y, x, value)
    return y, x, value

def fill_next_position_after_diagonal_down(grid, y, x, value, n):
    if can_move_down(y, n):
        y = move_down(y)
        value +=1
        set_value(grid, y, x, value)
    else:
        x = move_right(x)
        value +=1
        set_value(grid, y, x, value)
    return y, x, value

def fill_diagonal_up(grid, y, x, value, n):
    while can_move_up(y) and can_move_right(x, n):
        y = move_up(y)
        x = move_right(x)
        value +=1
        set_value(grid, y, x, value)
    return y, x, value

def fill_grid(n):
    grid = create_grid(n)
    y = 0
    x = 0
    value = 1
    if n ==1:
        fill_single_cell(grid, y, x)
        return grid
    set_value(grid, y, x, value)
    while value < n*n:
        y, x, value = fill_starting_positions(grid, y, x, value, n)
        y, x, value = fill_diagonal_down(grid, y, x, value, n)
        y, x, value = fill_next_position_after_diagonal_down(grid, y, x, value, n)
        y, x, value = fill_diagonal_up(grid, y, x, value, n)
    return grid

def print_case(case):
    print("Case %d:" % case)

def print_grid(grid, n):
    for i in range(n):
        print("%3d"*n % tuple(grid[i]))

def main():
    case =1
    while True:
        n = read_input()
        if n == 0:
            break
        grid = fill_grid(n)
        print_case(case)
        print_grid(grid, n)
        case +=1

main()