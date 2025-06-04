while True:
    hands = []
    for _ in range(5):
        h = int(input())
        if h == 0:
            exit()
        hands.append(h)

    unique = set(hands)
    if len(unique) == 1 or len(unique) == 3:
        # 全員同じ手か3手全てある場合はあいこ
        for _ in range(5):
            print(3)
    else:
        # 2種類の手の場合の勝敗判定
        # 勝つ手 → 負ける手 の関係を辞書で表現
        win_map = {1: 2, 2: 3, 3: 1}  # グーはチョキに勝つ、チョキはパーに勝つ、パーはグーに勝つ
        hand1, hand2 = unique
        if win_map[hand1] == hand2:
            winner = hand1
            loser = hand2
        else:
            winner = hand2
            loser = hand1

        for h in hands:
            if h == winner:
                print(1)
            else:
                print(2)