while True:

    user_card_sequence = input().strip()

    if user_card_sequence == '-':

        break

    number_of_shuffles = int(input())

    for shuffle_index in range(number_of_shuffles):

        shuffle_position = int(input())

        left_sequence = user_card_sequence[shuffle_position:]
        right_sequence = user_card_sequence[:shuffle_position]

        user_card_sequence = left_sequence + right_sequence

    print(user_card_sequence)