number_of_players, initial_points, number_of_rounds = map(int, input().split())

player_points = [0] * number_of_players

for round_index in range(number_of_rounds):
    
    player_index = int(input())
    
    player_points[player_index - 1] += 1

for player_index in range(number_of_players):
    
    final_points = player_points[player_index] + initial_points - number_of_rounds
    
    if final_points > 0:
        print("Yes")
    else:
        print("No")