number_of_players, initial_points_per_player, number_of_rounds = map(int, input().split())

player_answer_counts = []
player_points = []

for round_index in range(number_of_rounds):
    player_answer_counts.append(int(input()))

for player_index in range(number_of_players):
    player_points.append(int(initial_points_per_player))

for round_index, answered_player_index in enumerate(player_answer_counts):
    player_points[answered_player_index - 1] += 1

for player_index, total_points in enumerate(player_points):
    if total_points - number_of_rounds > 0:
        print("Yes")
    else:
        print("No")