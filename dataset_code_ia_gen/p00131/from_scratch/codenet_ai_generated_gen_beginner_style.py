n = int(input())
for _ in range(n):
    grid = [list(map(int, input().split())) for _ in range(10)]

    res = [[0]*10 for _ in range(10)]

    for i in range(10):
        for j in range(10):
            s = grid[i][j]
            if i > 0:
                s ^= res[i-1][j]
            if j > 0:
                s ^= res[i][j-1]
            if i > 0 and j > 0:
                s ^= res[i-1][j-1]
            res[i][j] = s

    for i in range(10):
        print(' '.join(str(x) for x in res[i]))