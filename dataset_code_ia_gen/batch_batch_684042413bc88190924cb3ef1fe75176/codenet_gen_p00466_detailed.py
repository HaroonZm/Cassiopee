# プログラムの説明：
# 1. 入力は複数のデータセットからなる。
# 2. 各データセットは10行で構成され、1行目は10冊の合計金額、次の9行は読み取れた本の価格。
# 3. 合計金額が0のときは入力終了の合図。
# 4. 各データセットごとに、読み取れなかった本の価格を計算して出力する。
# この問題は単純に合計金額から読み取れた9冊分の価格の合計を引くだけで求まる。

while True:
    total_price = int(input())   # 10冊の合計金額を取得
    if total_price == 0:         # 合計金額が0なら終了
        break

    known_prices = []
    for _ in range(9):
        price = int(input())     # 読み取れた9冊の価格を取得
        known_prices.append(price)

    missing_price = total_price - sum(known_prices)  # 読み取れなかった本の価格を計算
    print(missing_price)                             # 結果を出力