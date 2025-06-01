# ポケベル打ちの変換プログラム

# 手順：
# 1. 変換表を辞書で定義する。各2桁の数字列を対応する文字にマッピング。
# 2. 入力文字列を2文字ずつ区切って変換表で検索し、対応する文字を取得。
# 3. 不正なコード（変換表に存在しないキー）の場合はNAを出力。
# 4. 複数行の入力に対応し、各行ごとに変換して出力。

import sys

# 図2の変換表（ポケベル打ち）を辞書で定義
mapping = {
    "11":"a", "12":"b", "13":"c", "14":"d", "15":"e",
    "21":"f", "22":"g", "23":"h", "24":"i", "25":"j",
    "31":"k", "32":"l", "33":"m", "34":"n", "35":"o",
    "41":"p", "42":"q", "43":"r", "44":"s", "45":"t",
    "51":"u", "52":"v", "53":"w", "54":"x", "55":"y",
    "56":"z",
    "61":".", "62":"?", "63":"!", "64":" "
}

def decode_pager_code(line):
    # 入力が偶数桁でなければNA（全部2桁単位で区切るため）
    if len(line) % 2 != 0:
        return "NA"
    result_chars = []
    for i in range(0, len(line), 2):
        code = line[i:i+2]
        if code not in mapping:
            return "NA"  # 変換表にないコードはNA
        result_chars.append(mapping[code])
    return "".join(result_chars)

def main():
    # 入力は複数行、最大50行未満
    # sys.stdin読み込みで対応
    for line in sys.stdin:
        line = line.strip()
        if line == "":
            continue
        print(decode_pager_code(line))

if __name__ == "__main__":
    main()