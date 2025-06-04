def get_relative_positions():
    return [[-3,0],[-2,0],[-1,0],[1,0],[2,0],[3,0],[0,-3],[0,-2],[0,-1],[0,1],[0,2],[0,3]]

def is_within_bounds(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def is_one(A, x, y):
    return A[y][x] == '1'

def set_zero(A, x, y):
    A[y][x] = '0'

def explore_neighbors(A, x, y):
    positions = get_relative_positions()
    for dx, dy in positions:
        nx, ny = x + dx, y + dy
        if is_within_bounds(nx, ny) and is_one(A, nx, ny):
            explore(A, nx, ny)

def explore(A, x, y):
    set_zero(A, x, y)
    explore_neighbors(A, x, y)

def read_grid():
    return [list(input()) for _ in range(8)]

def read_coordinates():
    x = int(input()) - 1
    y = int(input()) - 1
    return x, y

def print_data_label(i):
    print(f'Data {i+1}:')

def print_grid(A):
    for r in A:
        print(*r, sep='')

def skip_blank():
    input()

def one_case(i):
    print_data_label(i)
    skip_blank()
    A = read_grid()
    x, y = read_coordinates()
    explore(A, x, y)
    print_grid(A)

def main():
    n = int(input())
    for i in range(n):
        one_case(i)

main()