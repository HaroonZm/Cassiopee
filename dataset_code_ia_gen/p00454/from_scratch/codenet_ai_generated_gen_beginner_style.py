while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    n = int(input())
    tape = []
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input().split())
        tape.append((x1, y1, x2, y2))

    xs = set([0, w])
    ys = set([0, h])
    for x1, y1, x2, y2 in tape:
        xs.add(x1)
        xs.add(x2)
        ys.add(y1)
        ys.add(y2)
    xs = sorted(xs)
    ys = sorted(ys)

    # 節の数は (len(xs)-1)*(len(ys)-1)
    grid = [[0]*(len(ys)-1) for _ in range(len(xs)-1)]

    # マスキングテープの覆う範囲を1にする
    for x1, y1, x2, y2 in tape:
        for i in range(len(xs)-1):
            if xs[i] >= x2 or xs[i+1] <= x1:
                continue
            for j in range(len(ys)-1):
                if ys[j] >= y2 or ys[j+1] <= y1:
                    continue
                grid[i][j] = 1

    visited = [[False]*(len(ys)-1) for _ in range(len(xs)-1)]

    def neighbors(i, j):
        res = []
        if i > 0:
            res.append((i-1, j))
        if i < len(xs)-2:
            res.append((i+1, j))
        if j > 0:
            res.append((i, j-1))
        if j < len(ys)-2:
            res.append((i, j+1))
        return res

    colors = 0
    for i in range(len(xs)-1):
        for j in range(len(ys)-1):
            if grid[i][j] == 0 and not visited[i][j]:
                colors += 1
                stack = [(i, j)]
                visited[i][j] = True
                while stack:
                    ci, cj = stack.pop()
                    for ni, nj in neighbors(ci, cj):
                        if grid[ni][nj] == 0 and not visited[ni][nj]:
                            visited[ni][nj] = True
                            stack.append((ni, nj))

    print(colors)