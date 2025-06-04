while True:
    n = int(input())
    if n == 0:
        break
    # 初期化
    magic = [[0]*n for _ in range(n)]
    # 初期の位置 (中央の一つ下)
    r = n // 2 + 1
    c = n // 2
    if r >= n:
        r = 0
    # 1からn*nまで数字を入れる
    for num in range(1, n*n+1):
        magic[r][c] = num
        # 次の座標候補（右下）
        nr = r + 1
        nc = c + 1
        # はみ出した場合の処理
        if nr >= n:
            nr = 0
        if nc >= n:
            nc = 0
        # もし埋まっていたら左下（左端に行ったら右端に戻る）
        if magic[nr][nc] != 0:
            nr = r + 1
            nc = c - 1
            if nr >= n:
                nr = 0
            if nc < 0:
                nc = n - 1
        r, c = nr, nc
    # 出力
    for row in magic:
        line = ""
        for x in row:
            line += f"{x:4d}"
        print(line.lstrip())