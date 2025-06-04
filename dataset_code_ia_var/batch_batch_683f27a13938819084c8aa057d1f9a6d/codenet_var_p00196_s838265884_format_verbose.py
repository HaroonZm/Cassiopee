def display_sorted_team_names_by_victories_and_draws():
    
    number_of_teams = int(input())
    
    if number_of_teams == 0:
        return -1
    
    team_scores_list = []
    
    for team_index in range(number_of_teams):
        
        team_data = input().split()
        
        team_name = team_data[0]
        number_of_victories = 0
        number_of_draws = 0
        
        for match_result in team_data[1:]:
            if match_result == '1':
                continue
            elif match_result == '0':
                number_of_victories += 1
            else:
                number_of_draws += 1
        
        team_scores_list.append((team_name, number_of_victories, number_of_draws))
    
    sorted_team_scores = sorted(
        team_scores_list,
        reverse=True,
        key=lambda team_stats: (team_stats[1], team_stats[2])
    )
    
    for team_stats in sorted_team_scores:
        print(team_stats[0])

while True:
    should_terminate = display_sorted_team_names_by_victories_and_draws()
    if should_terminate is not None:
        break