import sys

def rectangles_overlap(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
    """
    判定2つの長方形が重なっているかどうかを返す関数。
    長方形の左下(x1, y1)、右上(x2, y2)の座標を受け取る。
    「接している」状態も重なっているとみなす。

    アプローチ:
    - 長方形が重ならない条件を考えると、
      どちらかの長方形がもう一方の左または右に完全に離れているか、
      または上下に完全に離れている時は重ならない。
    - それ以外は重なっている。
    """
    # 横方向に完全に離れている場合
    if xa2 < xb1 or xb2 < xa1:
        return False
    # 縦方向に完全に離れている場合
    if ya2 < yb1 or yb2 < ya1:
        return False
    # 上記以外は重なっているか接している
    return True

def main():
    """
    複数のデータセットを標準入力から読み込み、
    各データセットの長方形の重なり判定結果を出力する関数。
    """
    for line in sys.stdin:
        # 空行をスキップ
        if not line.strip():
            continue
        # 入力は1行に8つの座標値があるので、空白区切りで分割して読み込む
        tokens = line.strip().split()
        if len(tokens) != 8:
            # 入力データとして不正な行は無視
            continue

        # 文字列から浮動小数点数に変換
        xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2 = map(float, tokens)

        # 長方形A、Bの座標を整える（左下、右上を正しくする）
        # 入力が左下と右上の座標になっていることが前提だが念のためmin/maxで整える
        xa1, xa2 = min(xa1, xa2), max(xa1, xa2)
        ya1, ya2 = min(ya1, ya2), max(ya1, ya2)
        xb1, xb2 = min(xb1, xb2), max(xb1, xb2)
        yb1, yb2 = min(yb1, yb2), max(yb1, yb2)

        # 重なり判定
        if rectangles_overlap(xa1, ya1, xa2, ya2, xb1, yb1, xb2, yb2):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()