while True:

    deck_of_cards = raw_input()

    if deck_of_cards == '-':
        break

    else:
        number_of_shuffles = int(raw_input())

        for shuffle_index in range(number_of_shuffles):

            number_of_cards_to_cut = int(raw_input())

            top_cut = deck_of_cards[:number_of_cards_to_cut]
            bottom_remaining = deck_of_cards[number_of_cards_to_cut:]
            deck_of_cards = bottom_remaining + top_cut

        print deck_of_cards