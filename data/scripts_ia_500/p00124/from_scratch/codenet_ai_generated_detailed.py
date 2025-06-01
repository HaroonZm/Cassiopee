# 勝ち点計算と並べ替えを行うプログラム

def main():
    dataset_count = 0  # データセット数
    while True:
        n = input().strip()
        if n == '':
            # 空行が入ることを想定し読み直す
            continue
        n = int(n)
        if n == 0:
            # チーム数0で入力終了
            break

        teams = []
        for i in range(n):
            # 入力：チーム名 勝ち数 負け数 引き分け数
            line = input().strip()
            while line == '':
                # 空行を飛ばす（念のため）
                line = input().strip()
            parts = line.split()
            name = parts[0]
            w = int(parts[1])
            l = int(parts[2])
            d = int(parts[3])
            # 勝ち点は勝3点、引分1点、負け0点
            points = w * 3 + d * 1 + l * 0
            teams.append((name, points, i))  # iは入力順保持用

        # 勝ち点の降順でソート。勝ち点同値なら入力順(i)の昇順で安定ソート
        teams.sort(key=lambda x: (-x[1], x[2]))

        # データセット間に空行を入れる
        if dataset_count > 0:
            print()

        # 結果出力
        for team in teams:
            print(f"{team[0]},{team[1]}")

        dataset_count += 1


if __name__ == "__main__":
    main()