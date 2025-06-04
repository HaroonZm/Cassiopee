while True:
    # 入力から生徒数nと場所数mを取得
    n, m = map(int, input().split())
    # n,mが共に0なら終了
    if n == 0 and m == 0:
        break

    # 各場所ごとに行きたい生徒の人数をカウントするリストを初期化
    counts = [0] * m

    for _ in range(n):
        # 生徒のアンケート結果を取得
        prefs = list(map(int, input().split()))
        # 各場所について○(1)ならカウントアップ
        for i in range(m):
            counts[i] += prefs[i]

    # 場所の番号と訪問希望者数をセットにしてリストにする [(場所番号, 人数), ...]
    places = [(i + 1, counts[i]) for i in range(m)]

    # 行きたい人数が多い順にソート、人数が同じ場合は場所番号の昇順でソート
    places.sort(key=lambda x: (-x[1], x[0]))

    # ソートした結果の場所番号のみを出力（空白区切り）
    print(' '.join(str(place[0]) for place in places))