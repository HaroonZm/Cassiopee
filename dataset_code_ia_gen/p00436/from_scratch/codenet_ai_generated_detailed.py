n = int(input())  # n: 半デッキの枚数、合計のカード枚数は2n
m = int(input())  # 操作の回数

# 初期のカードの並び。上から1,2,...,2n
cards = list(range(1, 2 * n + 1))

for _ in range(m):
    k = int(input())
    if k == 0:
        # リフルシャッフル
        # 山A: 上からn枚, 山B: 残りのn枚
        A = cards[:n]
        B = cards[n:]
        shuffled = []
        # Aの1枚目、Bの1枚目、Aの2枚目、Bの2枚目、...の順に交互にカードを入れる
        for i in range(n):
            shuffled.append(A[i])
            shuffled.append(B[i])
        cards = shuffled
    else:
        # カット操作
        # 上からk枚を山A、残りを山Bに分け、Aの上にBを乗せる（つまりBが上に来てAが下に来る）
        A = cards[:k]
        B = cards[k:]
        # 山Aの上に山Bを重ねる → B の上に A を乗せると考えられるが問題文では「山Aの上に山Bをのせる」と書かれているので
        # 山Aを下に、山Bを上に重ねる → 山B + 山Aの順？
        # 問題文の日本語を正確に読むと「山Aの上に山Bをのせる」なので、山Bが上に来る → 山B + 山A
        cards = B + A

# 最終的なカードの並びを一枚ずつ出力
for card in cards:
    print(card)