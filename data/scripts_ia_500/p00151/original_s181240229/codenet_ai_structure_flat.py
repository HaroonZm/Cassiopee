import sys, os

PYDEV = os.environ.get('PYDEV')
if PYDEV=="True":
    sys.stdin = open("sample-input.txt", "rt")

while True:
    n = int(input())
    if n == 0:
        break
    grid = [input().strip() for _ in range(n)]
    L = 0
    for row in grid:
        parts = row.split('0')
        for part in parts:
            if len(part) > L:
                L = len(part)
    for c in range(n):
        col = ''.join(grid[r][c] for r in range(n))
        parts = col.split('0')
        for part in parts:
            if len(part) > L:
                L = len(part)
    for row in range(-n, 2*n):
        diag1 = ''.join(grid[row+c][c] for c in range(n) if 0 <= row + c < n)
        parts = diag1.split('0')
        for part in parts:
            if len(part) > L:
                L = len(part)
        diag2 = ''.join(grid[row-c][c] for c in range(n) if 0 <= row - c < n)
        parts = diag2.split('0')
        for part in parts:
            if len(part) > L:
                L = len(part)
    print(L)