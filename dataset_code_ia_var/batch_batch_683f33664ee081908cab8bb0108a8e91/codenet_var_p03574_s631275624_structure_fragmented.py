def read_dimensions():
    return map(int, input().split())

def read_grid_row():
    return list(input())

def initialize_grid(h):
    grid = []
    for _ in range(h):
        grid.append(read_grid_row())
    return grid

def get_neighbor_directions():
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [1, 0, -1, 1, -1, 1, 0, -1]
    return dx, dy

def in_bounds(x, y, h, w):
    return 0 <= x < h and 0 <= y < w

def is_mine(cell):
    return cell == "#"

def count_adjacent_mines(i, j, h, w, s, dx, dy):
    count = 0
    for k in range(8):
        di = compute_new_x(i, dx, k)
        dj = compute_new_y(j, dy, k)
        if not in_bounds(di, dj, h, w):
            continue
        if is_mine(s[di][dj]):
            count = increment_count(count)
    return count

def compute_new_x(i, dx, k):
    return i + dx[k]

def compute_new_y(j, dy, k):
    return j + dy[k]

def increment_count(count):
    return count + 1

def set_cell_value(s, i, j, value):
    s[i][j] = str(value)

def process_grid(h, w, s):
    dx, dy = get_neighbor_directions()
    for i in range(h):
        for j in range(w):
            if is_mine(s[i][j]):
                continue
            count = count_adjacent_mines(i, j, h, w, s, dx, dy)
            set_cell_value(s, i, j, count)

def print_grid(s, h):
    for idx in range(h):
        print(transform_row(s, idx))

def transform_row(s, idx):
    return "".join(s[idx])

def main():
    h, w = read_dimensions()
    s = initialize_grid(h)
    process_grid(h, w, s)
    print_grid(s, h)

main()