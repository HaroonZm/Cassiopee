def max_consecutive_ones(grid, n):
    max_len = 0
    # dp arrays to store consecutive ones count for directions:
    # horizontal, vertical, diagonal (top-left to bottom-right), anti-diagonal (top-right to bottom-left)
    hori = [[0]*n for _ in range(n)]
    vert = [[0]*n for _ in range(n)]
    diag = [[0]*n for _ in range(n)]
    anti = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if grid[i][j] == '1':
                hori[i][j] = hori[i][j-1] + 1 if j > 0 else 1
                vert[i][j] = vert[i-1][j] + 1 if i > 0 else 1
                diag[i][j] = diag[i-1][j-1] + 1 if i > 0 and j > 0 else 1
                anti[i][j] = anti[i-1][j+1] + 1 if i > 0 and j < n-1 else 1
                max_len = max(max_len, hori[i][j], vert[i][j], diag[i][j], anti[i][j])
    return max_len


import sys
input = sys.stdin.readline
while True:
    n = input()
    if not n:
        break
    n = n.strip()
    if n == '0':
        break
    n = int(n)
    grid = [input().strip() for _ in range(n)]
    print(max_consecutive_ones(grid, n))