def read_input():
    return input()

def is_termination(n):
    return n == 0

def create_grid(n):
    return [[0] * n for _ in range(n)]

def init_position():
    return 0, 0

def handle_case_one(grid):
    grid[0][0] = 1

def inside_main_loop(value, n):
    return value < n * n

def assign_value(grid, x, y, value):
    grid[y][x] = value

def can_move_right(x, n):
    return x < n - 1

def move_right(x, value):
    return x + 1, value + 1

def can_move_down(y, n):
    return y < n - 1

def move_down(y, value):
    return y + 1, value + 1

def in_descending_diagonal(x, y, n):
    return x > 0 and y < n - 1

def move_descending_diag(x, y, value):
    return x - 1, y + 1, value + 1

def in_ascending_diagonal(y, x, n):
    return y > 0 and x < n - 1

def move_ascending_diag(x, y, value):
    return x + 1, y - 1, value + 1

def print_case_label(case):
    print("Case %d:" % case)

def print_grid(grid, n):
    for i in range(n):
        print("%3d" * n % tuple(grid[i]))

def process_case(n, case):
    value = 1
    grid = create_grid(n)
    x, y = init_position()
    if n == 1:
        handle_case_one(grid)
        print_case_label(case)
        print_grid(grid, n)
        return
    while inside_main_loop(value, n):
        assign_value(grid, x, y, value)
        if can_move_right(x, n):
            x, value = move_right(x, value)
            assign_value(grid, x, y, value)
        else:
            y, value = move_down(y, value)
            assign_value(grid, x, y, value)
        while in_descending_diagonal(x, y, n):
            x, y, value = move_descending_diag(x, y, value)
            assign_value(grid, x, y, value)
        if can_move_down(y, n):
            y, value = move_down(y, value)
            assign_value(grid, x, y, value)
        else:
            x, value = move_right(x, value)
            assign_value(grid, x, y, value)
        while in_ascending_diagonal(y, x, n):
            x, y, value = move_ascending_diag(x, y, value)
            assign_value(grid, x, y, value)
    print_case_label(case)
    print_grid(grid, n)

def to_int(val):
    try:
        return int(val)
    except:
        return 0

def main_loop():
    case = 1
    while True:
        n = read_input()
        try:
            n = int(n)
        except:
            n = to_int(n)
        if is_termination(n):
            break
        process_case(n, case)
        case += 1

main_loop()