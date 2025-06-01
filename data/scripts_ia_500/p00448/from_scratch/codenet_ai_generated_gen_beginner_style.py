while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break
    senbei = []
    for _ in range(R):
        senbei.append(list(map(int, input().split())))
    max_shukka = 0
    # すべての行の裏返しパターン（2^R通り）を試す
    for row_flip in range(1 << R):
        # row_flipのビットiが1ならi行目を裏返す
        # 行の裏返しだけでsenbeiの状態を決定する
        # 列ごとはあとで縦裏返しで調整
        flipped = []
        for i in range(R):
            if (row_flip >> i) & 1:
                # 裏返しならセンスチェンジ：0->1,1->0
                flipped.append([1 - x for x in senbei[i]])
            else:
                flipped.append(senbei[i])
        shukka = 0
        # 各列ごとに裏返すかどうかを判断
        for col in range(C):
            cnt0 = 0
            cnt1 = 0
            for row in range(R):
                if flipped[row][col] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1
            # 縦裏返しをした場合としない場合のうち多い方を取る
            shukka += max(cnt0, cnt1)
        if shukka > max_shukka:
            max_shukka = shukka
    print(max_shukka)