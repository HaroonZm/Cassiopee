num_teams = int(raw_input())
team_points = {}
team_ranks = {}
tie_count = 0
current_rank = -1
previous_points = -1
for team_index in range(num_teams):
    team_points[team_index] = 0
num_matches = num_teams * (num_teams - 1) / 2
for _ in range(num_matches):
    team_a, team_b, score_a, score_b = [int(x) for x in raw_input().split(" ")]
    if score_a > score_b:
        team_points[team_a - 1] += 3
    elif score_a < score_b:
        team_points[team_b - 1] += 3
    else:
        team_points[team_a - 1] += 1
        team_points[team_b - 1] += 1

points_list = team_points.items()
points_list.sort(cmp=(lambda x, y: cmp(y[1], x[1])))
for i in range(len(points_list)):
    if previous_points == points_list[i][1]:
        tie_count += 1
    else:
        current_rank += tie_count + 1
        previous_points = points_list[i][1]
        tie_count = 0
    team_ranks.update({points_list[i][0]: current_rank + 1})

for team_index in range(num_teams):
    print team_ranks[team_index]