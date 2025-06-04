while True:
    number_of_cards_per_player = int(input())

    if number_of_cards_per_player == 0:
        break

    card_used_by_player = [1] * (2 * number_of_cards_per_player + 1)

    for _ in range(1, number_of_cards_per_player + 1):
        card_played = int(input())
        card_used_by_player[card_played] = 0

    cards_remaining = [number_of_cards_per_player, number_of_cards_per_player]
    current_player = 0
    current_card_base = 0

    while cards_remaining[0] > 0 and cards_remaining[1] > 0:
        found_playable_card = True

        for candidate_card in range(current_card_base + 1, 2 * number_of_cards_per_player + 1):
            if card_used_by_player[candidate_card] == current_player:
                current_card_base = candidate_card
                card_used_by_player[candidate_card] = 2
                cards_remaining[current_player] -= 1
                found_playable_card = False
                break

            if candidate_card == 2 * number_of_cards_per_player:
                current_card_base = 0

        if found_playable_card:
            current_card_base = 0

        current_player = 1 - current_player

    print(cards_remaining[1])
    print(cards_remaining[0])