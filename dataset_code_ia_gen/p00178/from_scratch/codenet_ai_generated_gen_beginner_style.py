while True:
    n = int(input())
    if n == 0:
        break

    board = []  # 盤面は上から下に積み上げる形で、各行は5つの0/1で表す

    for _ in range(n):
        d, p, q = map(int, input().split())
        # d: 向き(1横,2縦), p: ブロックの長さ, q: 位置(左端からの1~5)

        # 落とす位置に合わせてどこに置けるか探す
        # 高さ方向の位置は決まっていないので、一番低く置けるところを探す

        # boardが空の場合は高さ0行もしくはp行を用意する必要がある

        # ブロックが横向きのとき
        if d == 1:
            # 横向きなので横にp個のブロックが並ぶ。qは左端の位置。
            # まず置ける高さを探す。例えば高さhの行で、
            # board[h][q-1 ... q-1+p-1]に空きがないと置けない。

            # boardの高さは動的なので、高さを増やしながら探す
            h = 0
            while True:
                # この高さにブロックを置いてみる
                # もしboardに行がなければ作る
                while h >= len(board):
                    board.append([0, 0, 0, 0, 0])

                # q-1 から q-1+p-1 まで全部0なら置ける
                can_place = True
                for x in range(q - 1, q - 1 + p):
                    if board[h][x] == 1:
                        can_place = False
                        break
                if can_place:
                    # ここに置けるかどうかは、下にもう一段あるかどうかをチェックする必要がある
                    # 落ちてきて引っかかるのは、下の段に重なりがあるかどうか

                    # もしh == 0なら地面に置ける
                    # それ以外は一つ下の行board[h-1]の同じ場所にブロックがあれば乗る
                    # そうでなければ下が空いているのでさらに下に落ちる

                    if h == 0:
                        # 地面に置ける
                        break

                    # 下の段に重なりあるか？
                    below_filled = False
                    for x in range(q - 1, q - 1 + p):
                        if board[h - 1][x] == 1:
                            below_filled = True
                            break
                    if below_filled:
                        break
                    else:
                        # さらに下に行く（hを一つ減らす）？ いやhは上から数える高さなのでhを増やす方向に落ちる
                        # ここでh行目に置けるか探しているので、hを一つ増やしてチェック
                        h += 1
                else:
                    # 置けないのでブロックはこれ以上上に置けないので上に積む行が上にできるのでh+=1
                    h += 1

            # h行目に置く
            for x in range(q - 1, q - 1 + p):
                board[h][x] = 1

        else:
            # d==2 縦向き
            # 縦長がp コマで1列のq番目の位置に落ちる
            # つまり、盤面上で高さhの行からh+p-1の行までがすべて空でなければならない
            # qは1..5なのでboard[][q-1]
            # 落ちる位置を下から重なり判定しながら探す

            h = 0
            while True:
                # boardの高さが足りなければ増やす
                while h + p - 1 >= len(board):
                    board.append([0, 0, 0, 0, 0])

                # h-1の段で引っかかるか見つける（ただしh=0は地面）
                if h == 0:
                    # 地面に置けるか判定する
                    # この高さhからh+p-1までのq-1列すべてが0か
                    can_place = True
                    for row in range(h, h + p):
                        if board[row][q - 1] == 1:
                            can_place = False
                            break
                    if can_place:
                        break  # hでOK
                    else:
                        h += 1
                        continue
                else:
                    # h-1の段のq-1に1があるか
                    if board[h - 1][q - 1] == 1:
                        # その上のhからh+p-1まで空ならここに置ける
                        can_place = True
                        for row in range(h, h + p):
                            if board[row][q - 1] == 1:
                                can_place = False
                                break
                        if can_place:
                            break
                        else:
                            h += 1
                            continue
                    else:
                        # まだ下まで到達していないのでh+=1して続ける
                        h += 1
                        continue

            # hからh+p-1までq-1列を1にする
            for row in range(h, h + p):
                board[row][q - 1] = 1

        # ブロックを置いた後に横一列が全部埋まっている行を消す
        # 消した行より上のブロックは下に落ちるので、消した行を削除して上の行を1段下げる形になる
        new_board = []
        for row in board:
            if sum(row) < 5:
                new_board.append(row)
        board = new_board

    # 最後に残ったブロックの数はboardのすべての1の数
    result = 0
    for row in board:
        result += sum(row)
    print(result)