# ゲームルールに基づいて確率計算し、YES/NOを出力するプログラム

def main():
    import sys

    # 1から10までのカードがそれぞれ1枚ずつ存在
    full_deck = set(range(1, 11))

    for line in sys.stdin:
        if not line.strip():
            continue
        C1, C2, C3 = map(int, line.strip().split())

        # 現在見えているカード：あなたの2枚と相手の表のカードの3枚
        known_cards = {C1, C2, C3}

        # あなたの現在の合計値
        current_sum = C1 + C2

        # 引くカードの候補はfull_deckからknown_cardsを除いたもの
        remaining_cards = full_deck - known_cards

        # あと1枚引いて合計が20以下になる枚数をカウント
        valid_count = 0
        for card in remaining_cards:
            if current_sum + card <= 20:
                valid_count += 1

        total_remaining = len(remaining_cards)
        # 50%以上かどうか判定（分数で計算）
        if total_remaining == 0:
            # 引けるカードがなければ引けないのでNO
            print("NO")
            continue

        probability = valid_count / total_remaining

        if probability >= 0.5:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()