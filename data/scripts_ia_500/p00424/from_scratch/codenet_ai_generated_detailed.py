# 解説:
# 1. 入力は複数のデータセットで構成され、各データセットは変換表の行数 n から始まる。
# 2. n = 0 のとき入力終了。
# 3. 各データセットでは、変換表 (n行) とデータの文字数 m、その後にm行の1文字ずつのデータが与えられる。
# 4. 変換は、
#    - 変換表で定義された「前の文字」を見つけたら対応する「後ろの文字」に1度だけ変換。
#    - 変換後の文字がさらに変換されることはない。
#    - 変換表にない文字はそのまま保持。
# 5. 各データセットの変換後の文字列を1行で出力。
# 6. 各データセットの出力のあとに改行を入れる。

while True:
    n = int(input())
    if n == 0:
        break  # 入力終了

    # 変換表の読み込み
    transform_dict = {}
    for _ in range(n):
        prev_char, post_char = input().split()
        transform_dict[prev_char] = post_char

    m = int(input())  # 変換するデータの文字数

    result_chars = []
    for _ in range(m):
        c = input()
        # 変換表にある場合は1度だけ変換、それ以外はそのまま
        if c in transform_dict:
            result_chars.append(transform_dict[c])
        else:
            result_chars.append(c)

    # 結果をまとめて1行出力
    print(''.join(result_chars))