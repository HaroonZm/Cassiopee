import os
import sys

if os.environ.get('PYDEV') == 'True':
    sys.stdin = open('sample-input.txt', 'rt')

def max_consecutive_length(line):
    return max(map(len, line.split('0')), default=0)

def grid_length(n, grid):
    max_len = 0

    # Rows and columns
    max_len = max(
        max_len,
        max(
            max_consecutive_length(row)
            for row in grid
        ),
        max(
            max_consecutive_length(''.join(grid[r][c] for r in range(n)))
            for c in range(n)
        )
    )

    # Diagonals: from top-left to bottom-right and top-right to bottom-left
    for start in range(-n + 1, n):
        diag_lr = ''.join(grid[r][r - start] for r in range(max(start, 0), min(n, n + start)))
        diag_rl = ''.join(grid[r][start + n - 1 - r] for r in range(max(start, 0), min(n, n + start)))

        max_len = max(max_len, max_consecutive_length(diag_lr), max_consecutive_length(diag_rl))

    return max_len

while (n := int(sys.stdin.readline())) != 0:
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    print(grid_length(n, grid))