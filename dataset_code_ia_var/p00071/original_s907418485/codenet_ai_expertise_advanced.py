from functools import partial

def bomb(y, x, grid):
    grid[y][x] = '0'
    range_check = lambda ny, nx: 0 <= nx < 8 and 0 <= ny < 8 and grid[ny][nx] == '1'
    offsets = [(-3, 0), (-2, 0), (-1, 0), (1, 0), (2, 0), (3, 0),
               (0, -3), (0, -2), (0, -1), (0, 1), (0, 2), (0, 3)]
    stack = [(y + dy, x + dx) for dx, dy in offsets if range_check(y + dy, x + dx)]
    while stack:
        ny, nx = stack.pop()
        grid[ny][nx] = '0'
        stack.extend(
            (ny + dy, nx + dx)
            for dx, dy in offsets
            if range_check(ny + dy, nx + dx)
        )
    return grid

def main():
    import sys
    input = partial(next, iter(sys.stdin))
    T = int(input())
    for i in range(1, T + 1):
        input()
        grid = [list(input().strip()) for _ in range(8)]
        x, y = int(input()), int(input())
        bomb(y - 1, x - 1, grid)
        print(f'Data {i}:')
        print('\n'.join(''.join(row) for row in grid))

if __name__ == '__main__':
    main()