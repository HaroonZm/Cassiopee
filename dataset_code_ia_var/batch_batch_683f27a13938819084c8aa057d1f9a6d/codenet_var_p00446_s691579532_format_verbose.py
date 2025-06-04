while True:

    number_of_cards_per_player = int(input())

    if number_of_cards_per_player == 0:
        exit()

    taro_cards = []
    for card_index in range(0, number_of_cards_per_player):
        taro_cards.append(int(input()))

    hanako_cards = []
    for card_value in range(1, 2 * number_of_cards_per_player + 1):
        if card_value not in taro_cards:
            hanako_cards.append(card_value)

    taro_cards.sort()

    current_played_card = 0
    is_taro_turn = True

    while len(taro_cards) != 0 and len(hanako_cards) != 0:

        if is_taro_turn:
            for taro_card_index in range(len(taro_cards)):
                if taro_cards[taro_card_index] > current_played_card:
                    current_played_card = taro_cards[taro_card_index]
                    taro_cards.remove(taro_cards[taro_card_index])
                    break
                if taro_card_index == len(taro_cards) - 1:
                    current_played_card = 0
            is_taro_turn = False

        else:
            for hanako_card_index in range(len(hanako_cards)):
                if hanako_cards[hanako_card_index] > current_played_card:
                    current_played_card = hanako_cards[hanako_card_index]
                    hanako_cards.remove(hanako_cards[hanako_card_index])
                    break
                if hanako_card_index == len(hanako_cards) - 1:
                    current_played_card = 0
            is_taro_turn = True

    print(len(hanako_cards))
    print(len(taro_cards))