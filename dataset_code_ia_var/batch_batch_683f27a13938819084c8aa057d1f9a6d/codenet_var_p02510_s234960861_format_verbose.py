def perform_deck_shuffle(deck_string, cut_position):

    deck_characters = list(deck_string)

    bottom_part = deck_characters[cut_position:]
    top_part = deck_characters[0:cut_position]

    shuffled_deck_characters = bottom_part + top_part

    shuffled_deck_string = ''.join(shuffled_deck_characters)

    return shuffled_deck_string


while True:

    deck_input = raw_input().rstrip()

    if deck_input == '-':

        break

    else:

        number_of_shuffles = int(raw_input())

        for shuffle_index in range(number_of_shuffles):

            current_cut_position = int(raw_input())

            deck_input = perform_deck_shuffle(deck_input, current_cut_position)

        print deck_input