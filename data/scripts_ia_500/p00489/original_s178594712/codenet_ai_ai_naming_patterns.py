import copy

num_players = int(input())
num_games = num_players * (num_players - 1) // 2

points_per_player = [0] * num_players
for _ in range(num_games):
    player1, player2, score1, score2 = map(int, input().split())
    if score1 > score2:
        points_per_player[player1 - 1] += 3
    elif score1 < score2:
        points_per_player[player2 - 1] += 3
    else:
        points_per_player[player1 - 1] += 1
        points_per_player[player2 - 1] += 1

sorted_points_desc = copy.deepcopy(points_per_player)
sorted_points_desc.sort(reverse=True)

ranks = [0] * num_players
for index, point in enumerate(points_per_player):
    ranks[index] = sorted_points_desc.index(point) + 1

for rank in ranks:
    print(rank)