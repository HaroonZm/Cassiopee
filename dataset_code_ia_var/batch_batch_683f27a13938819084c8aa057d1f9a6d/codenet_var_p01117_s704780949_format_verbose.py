while True:

    number_of_players, number_of_rounds = map(int, raw_input().split(' '))

    if number_of_players == 0:
        break

    scores_per_player = [0] * number_of_players

    for round_index in range(number_of_rounds):

        player_index = 0

        player_scores_this_round = map(int, raw_input().split(' '))

        for single_player_score in player_scores_this_round:
            scores_per_player[player_index] += single_player_score
            player_index += 1

    print max(scores_per_player)