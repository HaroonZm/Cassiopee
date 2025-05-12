while True:
    N, M, Q = map(int, input().split())  # N個のスイッチ, M個のライト, Q個のクエリ
    if N == 0 and M == 0 and Q ==0:
        exit()
    # 全ての配列を繋がっていることを仮定する
    correspondence = [set(list(range(M))) for _ in range(N)]
    # print(correspondence) 全てのスイッチと繋がっていることが確認できた
    switch_status = [0]*N  # スイッチの初期状態
    light_status = [0]*M  # ライトの初期状態
    for _ in range(Q):  # Q個のクエリが飛んでくる
        s, b = map(str, input().split())  # 操作したスイッチの情報と, 現在のライトの状態
        # 1つずつxorを取りたい
        # 操作したスイッチのインデックス (リスト)と、変化したライトのインデックス (set)が欲しい
        switch_index = list(map(int, s))  # 今回操作したスイッチの情報, これで数字に変換できる
        light_index = list(map(int, b))  # 現在のライトの情報, これで数字に変換できる

        changed_switch = []
        for i in range(len(switch_index)):
            if switch_index[i] == 1:
                changed_switch.append(i)
                switch_status[i] = switch_status[i] ^ 1  # 今まで0なら次の状態は1へ, 今まで1なら次の状態は0へ
        # changed_switchを使って色々やる
        # その前にまず、状態が変わったの一覧を手に入れる
        changed_light = []
        for i in range(len(light_index)):
            if light_status[i] ^ light_index[i]:  # 状態が変わったなら
                changed_light.append(i)  # 状態が変わったライト
        light_status = light_index  # ライトの状態を更新する
        set_changed_light = set(changed_light)
        # print(correspondence)
        for i in range(N):
            if i in changed_switch:
                correspondence[i] &= set_changed_light
            else:
                correspondence[i] -= set_changed_light
        # for c in changed_switch:  # 状態が変わったスイッチ, その他のスイッチからはライトを削除する必要ありそう
        #     correspondence[c] &= set_changed_light
    # print(correspondence)
    ans = [[] for _ in range(M)]  # M個のライトの状態
    for i, lights in enumerate(correspondence):
        for l in lights:
            ans[l].append(i)
    true_ans = ""
    co_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", \
    12: "C", 13: "D", 14: "E", 15: "F", 16: "G", 17: "H", 18: "I", 19: "J", 20: "K", 21: "L", 22: "M", 23: "N", 24: "O", \
    25: "P", 26: "Q", 27: "R", 28: "S", 29: "T", 30: "U", 31: "V", 32: "W", 33: "X", 34: "Y", 35: "Z"}
    for i in range(M):
        if len(ans[i]) > 1:
            true_ans += "?"
        else:
            true_ans += co_dict[ans[i][0]]

    print(true_ans)

# [{8, 9}, {6, 7}, {0, 1, 2, 3, 4, 5}]
# 2222221100