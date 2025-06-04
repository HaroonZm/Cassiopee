number_of_players, minimum_points_to_stay, number_of_rounds = map(int, input().split())

player_answer_indices = [int(input()) for _ in range(number_of_rounds)]

player_correct_counts = [0 for _ in range(number_of_players)]

for round_index in range(number_of_rounds):
    
    answered_player_index = player_answer_indices[round_index] - 1
    
    player_correct_counts[answered_player_index] += 1

for player_index in range(number_of_players):
    
    incorrect_count = number_of_rounds - player_correct_counts[player_index]
    
    if incorrect_count >= minimum_points_to_stay:
        print('No')
    else:
        print('Yes')