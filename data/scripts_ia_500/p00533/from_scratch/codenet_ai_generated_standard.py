H, W = map(int, input().split())
grid = [input() for _ in range(H)]

for i in range(H):
    res = []
    last_cloud = -1
    for j in range(W):
        if grid[i][j] == 'c':
            res.append(0)
            last_cloud = j
        else:
            if last_cloud == -1:
                res.append(-1)
            else:
                res.append(j - last_cloud)
    print(*res)