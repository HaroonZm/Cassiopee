from collections import Counter
import sys

def is_straight(cards):
    """判定：ストレートかどうかを確認する関数"""
    # カードをソート（昇順）
    sorted_cards = sorted(cards)
    # 通常の連続チェック
    for i in range(4):
        if sorted_cards[i+1] != sorted_cards[i] + 1:
            break
    else:
        # 連続していたらストレート
        return True

    # Aを1として扱う特殊ケース：
    # 例えば、A(1), 10,11,12,13の並びはストレートではないので弾く
    # Aを14として考え、例えば10,J,Q,K,A (10,11,12,13,1)を特別にチェック
    # そこでAを14に置換してチェックしてみる
    alt_cards = [14 if c == 1 else c for c in cards]
    sorted_alt = sorted(alt_cards)
    for i in range(4):
        if sorted_alt[i+1] != sorted_alt[i] + 1:
            break
    else:
        return True

    return False

def evaluate_hand(cards):
    """5枚のカードから役を判定する関数"""

    # カードのカウントを取得
    counts = Counter(cards)
    count_values = sorted(counts.values(), reverse=True)  # 出現数を降順に
    unique_cards = len(counts)

    # フォーカード（4枚同じ）
    if 4 in count_values:
        return "four card"
    # フルハウス（3枚＋2枚）
    if count_values == [3,2]:
        return "full house"
    # ストレート
    if unique_cards == 5 and is_straight(cards):
        return "straight"
    # スリーカード（3枚）
    if 3 in count_values:
        return "three card"
    # ツーペア（2組のペア）
    if count_values.count(2) == 2:
        return "two pair"
    # ワンペア（1組のペア）
    if 2 in count_values:
        return "one pair"
    # どれにも該当しない
    return "null"

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        # カードを読み込み
        cards = list(map(int, line.split(',')))
        # 判定
        result = evaluate_hand(cards)
        print(result)

if __name__ == "__main__":
    main()