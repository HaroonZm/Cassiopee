# プログラムの概要：
# 入力された左右の視力データを読み込み、それぞれの視力を判定基準に従ってA,B,C,Dに分類する。
# 各判定ごとに左右の人数をカウントし、最終的に判定ごとに人数を出力する。
# 
# 判定基準：
# A: 視力 >= 1.1
# B: 0.6 <= 視力 < 1.1
# C: 0.2 <= 視力 < 0.6
# D: 視力 < 0.2
#
# 入力は最大40行までで、各行は "l r" 形式の視力データ。
# 終了条件は明示されていないため、EOFまで読み込む形で対応。

import sys

def classify_vision(v):
    """視力vを判定し、判定文字('A','B','C','D')を返す関数"""
    if v >= 1.1:
        return 'A'
    elif v >= 0.6:
        return 'B'
    elif v >= 0.2:
        return 'C'
    else:
        return 'D'

def main():
    # 各判定ごとの左右視力人数カウント用辞書を用意
    # 例：counts['A']['L'] は判定Aで左視力の人数
    counts = {
        'A': {'L':0, 'R':0},
        'B': {'L':0, 'R':0},
        'C': {'L':0, 'R':0},
        'D': {'L':0, 'R':0},
    }

    # 標準入力から1行ずつ読み込み
    for line in sys.stdin:
        line=line.strip()
        if not line:
            continue  # 空行はスキップ
        l_str, r_str = line.split()
        l = float(l_str)
        r = float(r_str)

        # 左右の視力を判定に変換
        left_class = classify_vision(l)
        right_class = classify_vision(r)

        # カウントを増やす
        counts[left_class]['L'] += 1
        counts[right_class]['R'] += 1

    # 判定順に並べ替えて出力
    for judge in ['A','B','C','D']:
        print(counts[judge]['L'], counts[judge]['R'])


if __name__ == '__main__':
    main()