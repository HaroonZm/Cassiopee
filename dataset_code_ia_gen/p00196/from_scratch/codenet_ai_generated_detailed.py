# 野球大会の順位を決めるプログラム

# アプローチ：
# 1. 各データセットごとにチーム数、チームの成績を受け取る。
# 2. 勝ち数は値が0の数、負け数は値が1の数でカウント。
# 3. 同順位のチームがいる場合は入力順を優先するため、
#    ソート時に元のインデックスも保持しておく。
# 4. ソートのキーは(勝ち数の降順, 負け数の昇順, 入力順の昇順)。
# 5. 結果を上位から順に出力。
# 6. 0が入力されたら終了。

import sys

def main():
    input = sys.stdin.readline

    while True:
        n_line = input()
        if not n_line:
            break
        n = n_line.strip()
        if n == '0':
            break
        n = int(n)

        teams = []
        # チーム情報入力
        for i in range(n):
            line = input().strip().split()
            t = line[0]                 # チーム名（一文字）
            results = list(map(int, line[1:]))

            # 勝ち数 : 0 の数
            win_count = results.count(0)
            # 負け数 : 1 の数
            lose_count = results.count(1)

            # 元の入力順も保持
            teams.append((t, win_count, lose_count, i))

        # ソート（勝ち数多い順、負け数少ない順、入力順）
        teams.sort(key=lambda x: (-x[1], x[2], x[3]))

        # 出力
        for team in teams:
            print(team[0])

if __name__ == "__main__":
    main()