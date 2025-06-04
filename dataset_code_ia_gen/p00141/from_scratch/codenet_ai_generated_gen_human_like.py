d = int(input())
for _ in range(d):
    n = int(input())
    # 初期化：空白をセット
    grid = [[' ' for _ in range(n)] for _ in range(n)]

    top, bottom = 0, n - 1
    left, right = 0, n - 1

    # レイヤーごとに渦を描く
    while top <= bottom and left <= right:
        # 上辺（左から右）
        for c in range(left, right + 1):
            grid[bottom][c] = '#'
        bottom -= 1

        if top > bottom or left > right:
            break

        # 右辺（下から上）
        for r in range(bottom, top - 1, -1):
            grid[r][right] = '#'
        right -= 1

        if top > bottom or left > right:
            break

        # 下辺（右から左）
        for c in range(right, left - 1, -1):
            grid[top][c] = '#'
        top += 1

        if top > bottom or left > right:
            break

        # 左辺（上から下）
        for r in range(top, bottom + 1):
            grid[r][left] = '#'
        left += 1

    # 表示（左下を原点に見るため逆順に行を出力）
    for row in reversed(grid):
        print(''.join(row))
    print()