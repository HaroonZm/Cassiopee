n = int(input())  # データセット数を読み込む

for _ in range(n):
    digits = input()  # 8桁の数字の並びを読み込む

    # 最大の整数を作るために数字を降順にソート
    max_num_str = ''.join(sorted(digits, reverse=True))
    # 最小の整数を作るために数字を昇順にソート
    min_num_str = ''.join(sorted(digits))

    # 文字列を整数に変換（先頭の0も含めて自然な整数として扱われる）
    max_num = int(max_num_str)
    min_num = int(min_num_str)

    # 最大の整数と最小の整数の差を求めて出力
    print(max_num - min_num)