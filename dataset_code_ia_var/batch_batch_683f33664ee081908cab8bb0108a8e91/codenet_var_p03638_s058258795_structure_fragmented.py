def read_dimensions():
    return map(int, input().split())

def read_number():
    return int(input())

def read_list():
    return list(map(int, input().split()))

def create_grid_path(H, W):
    def get_row_indices(i, W):
        def forward_range(W):
            return range(W)
        def backward_range(W):
            return reversed(range(W))
        return forward_range(W) if i % 2 == 0 else backward_range(W)
    def row_path(i, W):
        return [(i, j) for j in get_row_indices(i, W)]
    def all_paths(H, W):
        res = []
        for i in range(H):
            res.extend(row_path(i, W))
        return res
    return all_paths(H, W)

def make_color_list(A):
    def expand_color(i, a):
        return [i+1] * a
    def expand_list(A):
        res = []
        for i, a in enumerate(A):
            res.extend(expand_color(i, a))
        return res
    return expand_list(A)

def make_empty_grid(H, W):
    return [[0] * W for _ in range(H)]

def fill_grid(grid, path, color_list):
    def place_color(k, pos):
        i, j = pos
        grid[i][j] = color_list[k]
    for k, p in enumerate(path):
        place_color(k, p)
    return grid

def print_grid(grid):
    def print_row(row):
        print(' '.join(map(str, row)))
    for row in grid:
        print_row(row)

def main():
    H, W = read_dimensions()
    N = read_number()
    A = read_list()
    path = create_grid_path(H, W)
    colors = make_color_list(A)
    grid = make_empty_grid(H, W)
    grid = fill_grid(grid, path, colors)
    print_grid(grid)

main()