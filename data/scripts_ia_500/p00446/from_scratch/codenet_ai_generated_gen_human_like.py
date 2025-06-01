while True:
    n = int(input())
    if n == 0:
        break
    taro_cards = [int(input()) for _ in range(n)]
    all_cards = set(range(1, 2*n+1))
    taro_set = set(taro_cards)
    hanako_cards = sorted(all_cards - taro_set)

    taro_hand = sorted(taro_cards)
    hanako_hand = hanako_cards

    field = 0
    turn = 0  # 0: Taro, 1: Hanako
    taro_score = 0
    hanako_score = 0

    # We play until one player runs out of cards
    while taro_hand and hanako_hand:
        if turn == 0:
            # Taro's turn
            can_play = [c for c in taro_hand if c > field]
            if can_play:
                card = min(can_play)
                taro_hand.remove(card)
                field = card
            else:
                field = 0
        else:
            # Hanako's turn
            can_play = [c for c in hanako_hand if c > field]
            if can_play:
                card = min(can_play)
                hanako_hand.remove(card)
                field = card
            else:
                field = 0
        turn = 1 - turn

    # Game ends when either player runs out of cards
    taro_score = len(hanako_hand)
    hanako_score = len(taro_hand)

    print(taro_score)
    print(hanako_score)