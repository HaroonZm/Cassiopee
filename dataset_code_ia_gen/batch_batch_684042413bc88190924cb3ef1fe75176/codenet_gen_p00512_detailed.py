# 問題の概要：
# 複数行の注文データが与えられ，同じ製品名の注文数を合計し，
# 製品名を指定の順序（文字列の長さ昇順，長さが同じ場合は辞書順）でソートして出力する。
#
# 入力例:
# 5
# A 20
# B 20
# A 20
# AB 10
# Z 10
#
# 出力例:
# A 40
# B 20
# Z 10
# AB 10
#
# 以下に詳細コメント付きの実装を示す。

import sys

def main():
    # 入力の一行目は注文データの行数 n
    n = int(sys.stdin.readline())

    # 製品名ごとの注文数の合計を保持する辞書を用意
    product_counts = {}

    # n行の注文データを読み込み
    for _ in range(n):
        # 製品名と注文数を空白で分割して取得
        line = sys.stdin.readline().strip()
        if not line:
            continue  # 念のため空行があればスキップ
        product, count_str = line.split()
        count = int(count_str)

        # 辞書に登録。既にあれば加算，なければ新規登録
        if product in product_counts:
            product_counts[product] += count
        else:
            product_counts[product] = count

    # ソートの基準：
    # 1) 製品名の長さ（小さい順）
    # 2) 長さが同じ場合は辞書順（アルファベット順）
    # sorted関数のkeyにタプル(length, product)を指定することで実現
    sorted_products = sorted(product_counts.items(), key=lambda x: (len(x[0]), x[0]))

    # 出力
    # 各製品名と合計注文数を空白区切りで出力し，
    # 出力最後の行にも改行を必ず入れる
    for product, total_count in sorted_products:
        print(product, total_count)

if __name__ == "__main__":
    main()