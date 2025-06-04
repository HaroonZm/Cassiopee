# 標高差（高さの差）を求めるプログラム
# 複数行で与えられた山の高さの中から、一番高い山と一番低い山を見つけ
# その差を計算して出力します。

import sys

def main():
    elevations = []
    # 標準入力から複数行を読み込む
    for line in sys.stdin:
        line = line.strip()
        # 空行は無視
        if not line:
            continue
        # 実数として標高を読み取る
        elevation = float(line)
        elevations.append(elevation)
    # 入力が空であれば何もしない（または0を出力）
    if not elevations:
        print(0.0)
        return
    # 一番高い山と一番低い山を取得
    max_elevation = max(elevations)
    min_elevation = min(elevations)
    # 差を計算
    diff = max_elevation - min_elevation
    # 小数点以下の誤差0.01許容されているので、そのまま出力
    # 必要に応じて小数点以下1桁以上を表示できるようフォーマットする
    print(diff)

if __name__ == "__main__":
    main()