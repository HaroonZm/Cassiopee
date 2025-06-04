n = int(input())
for case in range(1, n + 1):
    input()  # 空行を読み捨てる
    grid = []
    for _ in range(8):
        line = input()
        grid.append(list(line))
    X = int(input())
    Y = int(input())

    # 爆弾の座標は (X, Y)、座標系は左上(1,1)、左下(1,8)、右上(8,1)、右下(8,8)
    # 入力の行列は grid[y][x] で y=0..7, x=0..7
    # Yが行のindexに対応するが左上(1,1)がgrid[0][0] で左下(1,8)がgrid[7][0]
    # よって Y は行方向 座標系は上から数えるので gridのインデックスは y = Y - 1
    start_y = Y - 1
    start_x = X - 1

    # 爆発済みをマークするための配列
    exploded = [[False]*8 for _ in range(8)]

    # 爆弾の爆発範囲内の爆風を処理するためのキューを用いる(簡単なBFS)
    queue = []

    # 最初の爆弾がそこにあるかチェック
    if grid[start_y][start_x] == '1':
        queue.append((start_y, start_x))
        exploded[start_y][start_x] = True
    else:
        # 爆弾がない場合はそのまま
        pass

    while queue:
        y, x = queue.pop(0)
        # 爆発の影響範囲と連鎖爆発（上下左右3マス以内）
        for dy in range(-3, 4):
            ny = y + dy
            if 0 <= ny < 8:
                if grid[ny][x] == '1' and not exploded[ny][x]:
                    exploded[ny][x] = True
                    queue.append((ny, x))
        for dx in range(-3, 4):
            nx = x + dx
            if 0 <= nx < 8:
                if grid[y][nx] == '1' and not exploded[y][nx]:
                    exploded[y][nx] = True
                    queue.append((y, nx))

    # 爆発しなかった爆弾だけ残す
    for y in range(8):
        for x in range(8):
            if exploded[y][x]:
                grid[y][x] = '0'

    print("Data {}:".format(case))
    for row in grid:
        print("".join(row))