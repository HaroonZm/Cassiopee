# チケットの種類をキーとして価格を保持する辞書を用意
ticket_prices = {
    1: 6000,  # S席
    2: 4000,  # A席
    3: 3000,  # B席
    4: 2000   # C席
}

# 4行入力を受け取る
for _ in range(4):
    t, n = map(int, input().split())  # チケット種類tと枚数nを取得
    # 売上金額を計算（チケット単価×枚数）
    total = ticket_prices[t] * n
    # 計算結果を出力
    print(total)