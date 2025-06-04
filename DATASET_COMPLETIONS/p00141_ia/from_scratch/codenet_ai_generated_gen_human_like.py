d = int(input())
for _ in range(d):
    n = int(input())
    # 初期化：全て空白のn行n列
    grid = [[' ' for _ in range(n)] for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    fill = True  # 塗るか空白かの切り替え用（線＝#、間は空白）
    # 左下を基点とし、時計回りの渦巻きを作るので、
    # lineごとに「#」と「 」が交互に入る形を意識しつつ描く
    while left <= right and top <= bottom:
        if fill:
            # 上辺（bottom行) 塗る
            for c in range(left, right + 1):
                grid[bottom][c] = '#'
            bottom -= 1
            # 右辺 塗る
            for r in range(bottom, top - 1, -1):
                grid[r][right] = '#'
            right -= 1
        else:
            # 上辺（bottom行) 空白（何もしない）
            bottom -= 1
            # 右辺 空白（何もしない）
            right -= 1

        if left <= right and top <= bottom:
            if fill:
                # 下辺（top行）塗る
                for c in range(right, left - 1, -1):
                    grid[top][c] = '#'
                top += 1
                # 左辺 塗る
                for r in range(top, bottom + 1):
                    grid[r][left] = '#'
                left += 1
            else:
                # 下辺 空白（何もしない）
                top += 1
                # 左辺 空白（何もしない）
                left += 1
        fill = not fill

    for row in range(n):
        print(''.join(grid[row]))
    print()