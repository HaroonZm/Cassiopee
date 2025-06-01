def tetris_simulation():
    import sys

    # 横幅は5固定
    WIDTH = 5

    # 入力処理ループ
    while True:
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
            if line == '':
                return
        n = int(line)
        if n == 0:
            break

        board = []  # bottom-up: board[0]が一番下の行

        def ensure_height(h):
            while len(board) < h:
                board.append([0]*WIDTH)

        for _ in range(n):
            d,p,q = map(int, sys.stdin.readline().split())
            # d:1=横向き,2=縦向き
            # p:長さ
            # q:位置(1~5)
            q -= 1  # 0-indexed

            if d == 1:
                # 横向き長さp、左端q
                # 落ちる高さ探索：確認する場所はq~q+p-1の列の中で一番高い積み木の高さを探す
                max_height = 0
                for x in range(q,q+p):
                    col_h = 0
                    for y, row in enumerate(board):
                        if row[x]:
                            col_h = y+1
                    if col_h > max_height:
                        max_height = col_h
                # ブロックの底面はmax_heightの上に置くので行番号はmax_height
                landing_row = max_height
                ensure_height(landing_row+1)
                # ブロックを置く
                for x in range(q,q+p):
                    board[landing_row][x] = 1

            else:
                # 縦向き長さp、位置q
                # 落ちる高さ探索：col qの上で、縦にpを置ける最も低い場所
                col = q
                # 現在のcolの最高積み上げ高さ
                col_heights = 0
                for y, row in enumerate(board):
                    if row[col]:
                        col_heights = y+1
                # ブロックはcol_heightsの上に縦に並ぶ
                # なので下端行はcol_heights
                landing_row = col_heights
                ensure_height(landing_row+p)
                # ブロックを置く
                for y in range(landing_row, landing_row+p):
                    board[y][col] = 1

            # ライン消去判定
            new_board = []
            removed_lines = 0
            for row in board:
                if all(c==1 for c in row):
                    removed_lines += 1
                else:
                    new_board.append(row)
            # 消えた分だけ上から空行追加(盤面上に押し上げる形)
            for _ in range(removed_lines):
                new_board.append([0]*WIDTH)
            board = new_board

        # 最終的な残りマス数を数える
        ans = 0
        for row in board:
            ans += sum(row)
        print(ans)

if __name__ == '__main__':
    tetris_simulation()