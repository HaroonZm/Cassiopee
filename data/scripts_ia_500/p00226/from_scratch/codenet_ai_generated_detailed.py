# プログラムの概要:
# このプログラムは複数のデータセットを入力として受け取り、
# 各データセットにおいて正解(r)と回答(a)の4桁の数字列に対して
# ヒット数（位置も数字も同じもの）とブロー数（数字は同じで位置は違うもの）を計算し出力する。
# 入力は「0 0」で終わる。
# 各データセットの結果は1行に「ヒット数 ブロー数」と表示される。

while True:
    line = input().strip()
    if line == '0 0':
        # 終了条件
        break

    r, a = line.split()

    # ヒットの数を数える
    # ヒットは同じ位置で同じ数字
    hit = 0
    for i in range(4):
        if r[i] == a[i]:
            hit += 1

    # ブローの数を数える
    # まずヒットで一致した位置を除いた数字をカウントする
    # ブローは位置は違うが数字が正解に存在するもの
    # したがって正解の数字の頻度と回答の数字の頻度を数え、
    # ヒット分を除いた重複している部分の合計をブローとする。

    # ヒットがある位置の数字は除外して扱うため、
    # それ以外の数字のリストを作る
    r_rest = []
    a_rest = []
    for i in range(4):
        if r[i] != a[i]:
            r_rest.append(r[i])
            a_rest.append(a[i])

    # 正解の残り数字のカウント
    from collections import Counter
    r_count = Counter(r_rest)
    a_count = Counter(a_rest)

    # ブローをカウント
    # それぞれの数字について、min(正解の数字数, 回答の数字数)の合計
    blow = 0
    for digit in a_count:
        blow += min(r_count.get(digit, 0), a_count[digit])

    print(hit, blow)