import sys

def set_recursion():
    sys.setrecursionlimit(10 ** 5 + 10)

def get_input():
    return sys.stdin.readline().strip()

def read_hw():
    return map(int, get_input().split())

def read_grid(H):
    return [[char for char in get_input()] for _ in range(H)]

def initialize_matrix(H, W):
    return [[0]*W for _ in range(H)]

def fill_left(grid, l, H, W):
    for h in range(H):
        update_left_row(grid, l, h, W)

def update_left_row(grid, l, h, W):
    cur = 0
    for w in range(W):
        cur = left_cell_value(grid, h, w, cur)
        l[h][w] = cur

def left_cell_value(grid, h, w, cur):
    if grid[h][w] == '#':
        return 0
    else:
        return cur + 1

def fill_right(grid, r, H, W):
    for h in range(H):
        update_right_row(grid, r, h, W)

def update_right_row(grid, r, h, W):
    cur = 0
    for w in reversed(range(W)):
        cur = right_cell_value(grid, h, w, cur)
        r[h][w] = cur

def right_cell_value(grid, h, w, cur):
    if grid[h][w] == '#':
        return 0
    else:
        return cur + 1

def fill_up(grid, u, H, W):
    for w in range(W):
        update_up_column(grid, u, w, H)

def update_up_column(grid, u, w, H):
    cur = 0
    for h in range(H):
        cur = up_cell_value(grid, h, w, cur)
        u[h][w] = cur

def up_cell_value(grid, h, w, cur):
    if grid[h][w] == '#':
        return 0
    else:
        return cur + 1

def fill_down(grid, d, H, W):
    for w in range(W):
        update_down_column(grid, d, w, H)

def update_down_column(grid, d, w, H):
    cur = 0
    for h in reversed(range(H)):
        cur = down_cell_value(grid, h, w, cur)
        d[h][w] = cur

def down_cell_value(grid, h, w, cur):
    if grid[h][w] == '#':
        return 0
    else:
        return cur + 1

def get_max_illumination(l, r, u, d, H, W):
    ans = 0
    for h in range(H):
        for w in range(W):
            cur = illumination_score(l, r, u, d, h, w)
            ans = max(ans, cur)
    return ans

def illumination_score(l, r, u, d, h, w):
    return r[h][w] + l[h][w] + u[h][w] + d[h][w] - 3

def print_result(ans):
    print(ans)

def solve():
    set_recursion()
    H, W = read_hw()
    grid = read_grid(H)
    l = initialize_matrix(H, W)
    r = initialize_matrix(H, W)
    u = initialize_matrix(H, W)
    d = initialize_matrix(H, W)
    fill_left(grid, l, H, W)
    fill_right(grid, r, H, W)
    fill_up(grid, u, H, W)
    fill_down(grid, d, H, W)
    ans = get_max_illumination(l, r, u, d, H, W)
    print_result(ans)

solve()