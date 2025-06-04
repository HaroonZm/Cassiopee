# 定義された色の名前と対応するRGB値のリスト
# 各色は16進数で0から255の範囲の値を持つ
colors = [
    ("black",   (0x00, 0x00, 0x00)),
    ("blue",    (0x00, 0x00, 0xff)),
    ("lime",    (0x00, 0xff, 0x00)),
    ("aqua",    (0x00, 0xff, 0xff)),
    ("red",     (0xff, 0x00, 0x00)),
    ("fuchsia", (0xff, 0x00, 0xff)),
    ("yellow",  (0xff, 0xff, 0x00)),
    ("white",   (0xff, 0xff, 0xff))
]

def hex_to_int(s):
    """
    16進数の文字列を整数に変換する。
    sは長さ2の文字列として仮定するが、念のため例外処理も行う。
    不正な16進数の場合はNoneを返す。
    """
    try:
        return int(s, 16)
    except ValueError:
        return None

def parse_color_code(code):
    """
    色コードを受け取り、R,G,Bの整数値を取得する。
    codeは '#RGB' の形式を想定。
    無効なコードが混入している可能性も考慮し、全体を整形・変換し、
    不正な値の場合は誤差を少なくするため0〜255の範囲内で補正。
    """
    # codeは#に続き6文字の16進数のはずだが異常値にも対応
    if len(code) != 7 or code[0] != '#':
        # 無効な場合は黒に近い色として0番のblackを返す (後で距離計算で対応)
        return None
    r = hex_to_int(code[1:3])
    g = hex_to_int(code[3:5])
    b = hex_to_int(code[5:7])
    if r is None or g is None or b is None:
        return None
    # 範囲外も念のためClamp（だが本問題の入力想定外）
    r = min(max(r, 0), 255)
    g = min(max(g, 0), 255)
    b = min(max(b, 0), 255)
    return (r, g, b)

def distance_sq(c1, c2):
    """
    2つのRGBタプルのユークリッド距離の2乗を計算
    距離の大小比較で十分なので平方根は計算しない（計算コスト削減）
    """
    return (c1[0]-c2[0])**2 + (c1[1]-c2[1])**2 + (c1[2]-c2[2])**2

def find_closest_color(code):
    """
    与えられたカラーコードのRGB値から、colorsリストの中で
    最も距離が近い色の名前を返す。
    無効なコードの場合は、colorsリストの先頭の色を返す（問題の挙動として「白」などで対応しても良いが保守的に black）
    """
    rgb = parse_color_code(code)
    if rgb is None:
        # 無効値はblackを返しておく（例: #decadeはパースに失敗するため)
        # ただし問題のサンプルでは#decadeはwhiteを返している。
        # これはおそらく誤字表記のため#decadeの部分だけ正しく切り出しているか、
        # もしくは距離計算で一番近い色としてwhiteとなっている。
        # ここでは、距離計算のために不正な16進2文字があれば近似数値を推定できるように置き換え処理する実装に変更する。

        # 変更: 不正な16進数が含まれている場合、各2文字ごとに不正な文字を'0'に置換してリトライ
        # 例: #decade → de ca de → de=222, ca=202, de=222となるため強引に文字列処理可能
        def fix_invalid_hex(s):
            res = ''
            for ch in s:
                if ch.lower() in '0123456789abcdef':
                    res += ch
                else:
                    res += '0'   # 置換文字
            return res

        s = code[1:]
        fixed = fix_invalid_hex(s)
        r = int(fixed[0:2],16)
        g = int(fixed[2:4],16)
        b = int(fixed[4:6],16)
        rgb = (r,g,b)

    min_dist = None
    min_name = None
    for name, (r2,g2,b2) in colors:
        dist = distance_sq(rgb, (r2,g2,b2))
        if min_dist is None or dist < min_dist:
            min_dist = dist
            min_name = name
    return min_name

import sys

def main():
    """
    標準入力よりカラーコードを1行ずつ読み込み、
    入力が'0'のとき終了。
    各カラーコードについて最も近い色名を出力する。
    """
    for line in sys.stdin:
        line=line.strip()
        if line == '0':
            break
        result = find_closest_color(line)
        print(result)

if __name__ == '__main__':
    main()