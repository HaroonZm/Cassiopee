# 単位のリストを定義
# 単位は10^4の倍数ごとに対応する
units = ["", "Man", "Oku", "Cho", "Gai", "Jo", "Ko", "Jo"]  # 「塵劫記」の説明に合わせて、必要な単位を追加
# 実際は問題例に「Jo」と「Ko」などが含まれているため、単位名を実際のものに合わせる
# 参考："穣"(Jo)は10^28, "垓"(Gai)は10^20, "京"(Kei)は10^16, "兆"(Cho)は10^12, "億"(Oku)は10^8, "万"(Man)は10^4
# 問題文の例から単位は["", "Man", "Oku", "Cho", "Kei", "Gai", "Jo"] の順序が正しい
units = ["", "Man", "Oku", "Cho", "Kei", "Gai", "Jo"]  # 10^0, 10^4, 10^8, 10^12, 10^16, 10^20, 10^28


def format_chinkoki(num: int) -> str:
    """
    入力：numは10^72未満の正整数
    出力：塵劫記の単位で区切った文字列

    アプローチ：
    1. 4桁ごと（つまり10^4単位）に区切る。
    2. それぞれのブロックは1~9999の数。
    3. ゼロの場合はスキップ。
    4. 単位はunitsに対応する。
    5. 最上位ブロックから順に連結。

    例：
    126765060022822940149673205376 -> 126穣7650垓6002京2822兆9401億4967万320万5376
    ではなく問題の例のように4桁ごとに区切って単位をつける。
    """
    # 文字列に変換し、後ろから4桁ずつ区切る
    s = str(num)
    # 右から4桁ごとに分割 (逆順)
    parts = []
    while s:
        parts.append(s[-4:])
        s = s[:-4]
    # partsは最下位から最上位の順なので逆順にする
    parts.reverse()
    # partsの長さによって単位を割り当てる
    # 例： parts[0]には最上位の数字、単位はunits[length - 1 - 0]
    # unitsは7種類なので、7を超えることはないはず (10^28までだが問題は10^72未満)
    # 問題上では問題ないが、安全のため判定する
    n_parts = len(parts)
    result = []
    for i, block in enumerate(parts):
        val = int(block)
        if val == 0:
            continue
        unit_index = n_parts - 1 - i  # 桁に紐づく単位のインデックス
        unit = units[unit_index] if unit_index < len(units) else ""
        # ゼロ埋めは不要なので整数のまま文字列化
        result.append(str(val) + unit)
    return "".join(result) if result else "0"


def main():
    import sys

    for line in sys.stdin:
        # 入力は2つの整数m, nが1行にある形式かもしれないので変換を適宜対応
        # 問題文は「m」と「n」が別々の行に入るとのことなので2行ずつ読み取る
        line = line.strip()
        if not line:
            continue
        m = int(line)
        n_line = sys.stdin.readline()
        if not n_line:
            break
        n = int(n_line.strip())
        if m == 0 and n == 0:
            break
        # 指数計算
        val = pow(m, n)
        # 表示
        print(format_chinkoki(val))


if __name__ == "__main__":
    main()