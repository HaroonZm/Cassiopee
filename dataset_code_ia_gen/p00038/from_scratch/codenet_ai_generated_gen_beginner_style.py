while True:
    try:
        line = input()
        cards_str = line.split(",")
        cards = [int(c) for c in cards_str]

        counts = {}
        for c in cards:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        values = sorted(counts.values(), reverse=True)

        # 判定用にカードの数字をソート
        sorted_cards = sorted(cards)

        # ストレート判定関数
        def is_straight(cards):
            # 普通に並んでいるか
            cards_sorted = sorted(set(cards))
            if len(cards_sorted) != 5:
                return False
            # 例えば 1 2 3 4 5 の判定
            normal_straight = True
            for i in range(4):
                if cards_sorted[i+1] - cards_sorted[i] != 1:
                    normal_straight = False
                    break
            if normal_straight:
                return True
            # A を 14 として最後にする場合（10 J Q K A）
            # J=11,Q=12,K=13,A=1 のため、A=1は特殊な扱いで、10,11,12,13,1はストレート扱い
            # なので、A を 14 とみなしてチェックしてみる
            ace_as_14 = [14 if x==1 else x for x in cards]
            ace_cards_sorted = sorted(set(ace_as_14))
            if len(ace_cards_sorted) != 5:
                return False
            for i in range(4):
                if ace_cards_sorted[i+1] - ace_cards_sorted[i] != 1:
                    return False
            return True

        # 役判定
        if 4 in values:
            print("four card")
        elif 3 in values and 2 in values:
            print("full house")
        elif is_straight(cards):
            print("straight")
        elif 3 in values:
            print("three card")
        elif values.count(2) == 2:
            print("two pair")
        elif 2 in values:
            print("one pair")
        else:
            print("null")

    except EOFError:
        break