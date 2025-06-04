import sys
import operator

input_stream = sys.stdin

while True:
    number_of_teams = int(input_stream.readline())
    
    if number_of_teams == 0:
        break

    teams_data = []
    for team_index in range(number_of_teams):
        team_stats = input_stream.readline().split()
        teams_data.append(team_stats)

    teams_with_scores_and_index = []
    for original_index, team_stats in enumerate(teams_data):
        team_name = team_stats[0]
        number_of_losses = team_stats.count('0')
        number_of_wins = team_stats.count('1')
        teams_with_scores_and_index.append(
            (team_name, -number_of_losses, number_of_wins, original_index)
        )

    teams_with_scores_and_index.sort(
        key=operator.itemgetter(1, 2, 3)
    )

    team_names_sorted = [
        team_info[0] for team_info in teams_with_scores_and_index
    ]
    
    print('\n'.join(team_names_sorted))