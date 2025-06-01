while True:
    H, W, N = map(int, input().split())
    if H == 0 and W == 0 and N == 0:
        break
    grid = [list(map(int, input().split())) for _ in range(H)]
    for _ in range(N):
        i, j = 0, 0
        while i < H and j < W:
            if grid[i][j] == 1:
                grid[i][j] = 0
                j += 1
            else:
                grid[i][j] = 1
                i += 1
        print(i + 1, j + 1)