# 解答例：PythonによるRank Checkerの実装

# このプログラムは以下の手順で動作します。
# 1. チームの整理番号と正解数を(番号,正解数)の形で読み込み、0,0で終了。
# 2. 正解数の多い順にソートし、順位付けする。
#    - 同じ正解数のチームは同順位とし、次の順位は順位数とは無関係に正解数ごとの異なる順位だけカウントする。
# 3. 問い合わせの整理番号を標準入力から読み込み、各チームの順位を出力する。

import sys

def main():
    # チームデータを格納する辞書：key=整理番号, value=正解数
    teams = {}

    # 予選結果の読み込み
    while True:
        line = sys.stdin.readline().rstrip()
        if not line:
            break
        p_s = line.split(',')
        if len(p_s) != 2:
            break
        p = int(p_s[0])
        s = int(p_s[1])
        if p == 0 and s == 0:
            break
        teams[p] = s

    # 正解数のリストを抽出し、降順でソート（重複無し）
    # これにより各正解数の順位を決める
    correct_counts = sorted(set(teams.values()), reverse=True)

    # 正解数 -> 順位 の辞書を作成
    # 例えば correct_counts = [30, 20, 10] → {30:1, 20:2, 10:3}
    rank_map = {}
    for idx, score in enumerate(correct_counts, start=1):
        rank_map[score] = idx

    # 問い合わせの処理
    for line in sys.stdin:
        q = line.strip()
        if not q:
            continue
        q_num = int(q)
        if q_num in teams:
            score = teams[q_num]
            print(rank_map[score])
        else:
            # チーム番号が存在しない場合は特に指示が無いが、
            # 問題文の制約上存在すると考えられるので、
            # ここでは何もしないか、0を出力しておく。必要に応じて変更可能。
            print(0)

if __name__ == "__main__":
    main()