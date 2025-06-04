from itertools import combinations as generate_combinations

def calculate_possible_tournaments():
    
    while True:
        
        number_of_teams = int(input())
        
        if number_of_teams == 0:
            break
        
        number_of_known_results = int(input())
        
        match_results_matrix = [
            [None for _ in range(number_of_teams)] 
            for _ in range(number_of_teams)
        ]
        
        for _ in range(number_of_known_results):
            team1_index, team2_index = map(int, input().split())
            team1_index -= 1
            team2_index -= 1
            match_results_matrix[team1_index][team2_index] = True   # team1 beats team2
            match_results_matrix[team2_index][team1_index] = False  # team2 loses to team1
        
        victories_per_team = [
            match_result_row.count(True) 
            for match_result_row in match_results_matrix
        ]
        
        list_of_undecided_opponents = [[] for _ in range(number_of_teams)]
        count_of_undecided_matches = [0 for _ in range(number_of_teams)]
        
        for current_team_index in range(number_of_teams):
            for opponent_index in range(current_team_index + 1, number_of_teams):
                if match_results_matrix[current_team_index][opponent_index] is None:
                    list_of_undecided_opponents[current_team_index].append(opponent_index)
                    count_of_undecided_matches[current_team_index] += 1
        
        maximum_victories_per_team = number_of_teams // 2
        
        def explore_match_outcomes(
            team_index, 
            victories_for_teams
        ):
            
            if team_index == number_of_teams:
                return 1
            
            remaining_victories_possible = maximum_victories_per_team - victories_for_teams[team_index]
            
            if (
                remaining_victories_possible < 0 or 
                remaining_victories_possible > count_of_undecided_matches[team_index]
            ):
                return 0
            
            undecided_matches_left = (
                count_of_undecided_matches[team_index] - 
                remaining_victories_possible
            )
            count_valid_configurations = 0
            
            for opponents_to_win_against in generate_combinations(
                list_of_undecided_opponents[team_index], 
                undecided_matches_left
            ):
                updated_victories_for_teams = victories_for_teams[:]
                for opponent_index in opponents_to_win_against:
                    updated_victories_for_teams[opponent_index] += 1
                count_valid_configurations += explore_match_outcomes(
                    team_index + 1, 
                    updated_victories_for_teams
                )
            
            return count_valid_configurations
        
        possible_tournaments_count = explore_match_outcomes(0, victories_per_team)
        print(possible_tournaments_count)

calculate_possible_tournaments()