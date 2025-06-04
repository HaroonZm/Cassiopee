import sys

# 変数の初期化
count_triangle = 0      # 三角形の総数
count_right = 0         # 直角三角形の数
count_acute = 0         # 鋭角三角形の数
count_obtuse = 0        # 鈍角三角形の数

for line in sys.stdin:
    # 入力の整形と分割
    parts = line.strip().split()
    if len(parts) < 3:
        # 3つ以上の整数が入力行に含まれていない場合は無視する
        continue

    # 三つの整数に変換
    try:
        a, b, c = map(int, parts[:3])
    except:
        # 数値変換に失敗したら無視して次へ
        continue

    # 三角形の成立判定
    # 三角形成立条件: 任意の2辺の和 > 残りの辺
    sides = sorted([a, b, c])
    if sides[0] + sides[1] <= sides[2]:
        # 三角形が存在しない場合は集計結果を出力して終了
        print(f"{count_triangle} {count_right} {count_acute} {count_obtuse}")
        break

    # 三角形は存在するのでカウント
    count_triangle += 1

    # 三角形の種類判定
    # 各辺の二乗を計算
    x2 = sides[0] ** 2
    y2 = sides[1] ** 2
    z2 = sides[2] ** 2

    # 直角三角形: 最長辺の二乗 == 他の2辺の二乗和
    if z2 == x2 + y2:
        count_right += 1
    # 鋭角三角形: 最長辺の二乗 < 他の2辺の二乗和
    elif z2 < x2 + y2:
        count_acute += 1
    # 鈍角三角形: 最長辺の二乗 > 他の2辺の二乗和
    else:
        count_obtuse += 1

# 入力が終了して三角形が存在しないケースがない場合は
# 一応最終集計を出力（問題文では必ず存在しない入力があるとあるため基本不要）
else:
    print(f"{count_triangle} {count_right} {count_acute} {count_obtuse}")