H, W = map(int, input().split())
grid = [input() for _ in range(H)]

result = [[-1]*W for _ in range(H)]

for i in range(H):
    last_cloud = -1
    for j in range(W):
        if grid[i][j] == 'c':
            result[i][j] = 0
            last_cloud = j
        elif last_cloud != -1:
            result[i][j] = j - last_cloud

for row in result:
    print(*row)