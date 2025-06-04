# 解説：
# 各データセットについて、
# ・鍵の数 n と鍵のリスト k1, k2, ..., kn を読み込む
# ・訪問駅のリスト s を読み込む
# 鍵は訪問駅リストの何駅前かを示す。
# n < len(s) の場合、鍵は順に循環して使う。
# sの各文字に対し、対応する鍵を使って1文字ずつ戻った駅名を復号化する。

# 駅名は"a"〜"z"と"A"〜"Z"の52文字で環状になっている
# "a"(0)〜"z"(25), "A"(26)〜"Z"(51)
# 次が分かるようにインデックス0〜51で処理
# 前の駅は (現在インデックス - 鍵値) %52

def char_to_index(c):
    """駅の文字を0-51のインデックスに変換"""
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    else:  # 'A' <= c <= 'Z'
        return ord(c) - ord('A') + 26

def index_to_char(i):
    """インデックス0-51を駅の文字に変換"""
    if 0 <= i <= 25:
        return chr(i + ord('a'))
    else:
        return chr(i - 26 + ord('A'))

while True:
    n = int(input())
    if n == 0:
        break
    keys = list(map(int, input().split()))
    s = input()
    res = []
    length = len(s)
    for i, c in enumerate(s):
        key = keys[i % n]  # 鍵が繰り返し使われる
        idx = char_to_index(c)
        new_idx = (idx - key) % 52
        res.append(index_to_char(new_idx))
    print("".join(res))