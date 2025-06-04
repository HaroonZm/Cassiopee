def calculate_maximum_possible_wins_against_rock_paper_sequence(opponent_hand_sequence):

    total_rounds = len(opponent_hand_sequence)

    count_of_paper_moves = opponent_hand_sequence.count('p')

    maximum_possible_wins = (total_rounds // 2) - count_of_paper_moves

    return maximum_possible_wins


user_input_hand_sequence = input().strip()

print(calculate_maximum_possible_wins_against_rock_paper_sequence(user_input_hand_sequence))