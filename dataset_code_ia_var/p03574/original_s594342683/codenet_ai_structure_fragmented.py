import sys

def read_dimensions():
    return map(int, input().split())

def read_single_line():
    return list(input())

def read_grid(height):
    grid = []
    for _ in range(height):
        grid.append(read_single_line())
    return grid

def in_bounds(i, j, H, W):
    return 0 <= i < H and 0 <= j < W

def is_mine(cell):
    return cell == '#'

def get_neighbor_positions(i, j):
    return [
        (i-1, j-1), (i-1, j), (i-1, j+1),
        (i, j-1),            (i, j+1),
        (i+1, j-1), (i+1, j), (i+1, j+1)
    ]

def count_mines_for_cell(grid, i, j, H, W):
    count = 0
    for ni, nj in get_neighbor_positions(i, j):
        if check_and_count_mine(grid, ni, nj, H, W):
            count += 1
    return count

def check_and_count_mine(grid, ni, nj, H, W):
    if in_bounds(ni, nj, H, W) and is_mine(grid[ni][nj]):
        return True
    return False

def process_cell(grid, i, j, H, W):
    if is_mine(grid[i][j]):
        return
    count = count_mines_for_cell(grid, i, j, H, W)
    grid[i][j] = str(count)

def process_grid(grid, H, W):
    for i in range(H):
        for j in range(W):
            process_cell(grid, i, j, H, W)

def print_line(line):
    print(''.join(line))

def print_grid(grid, H):
    for i in range(H):
        print_line(grid[i])

def main():
    H, W = read_dimensions()
    grid = read_grid(H)
    process_grid(grid, H, W)
    print_grid(grid, H)

main()