from itertools import combinations as generate_combinations

def main():
    
    while True:
        
        number_of_players = int(input())
        
        if number_of_players == 0:
            break
        
        number_of_known_matches = int(input())
        
        match_results_matrix = [[None] * number_of_players for _ in range(number_of_players)]
        
        for _ in range(number_of_known_matches):
            winner_index, loser_index = map(int, input().split())
            winner_index -= 1
            loser_index -= 1
            match_results_matrix[winner_index][loser_index] = True
            match_results_matrix[loser_index][winner_index] = False

        win_counts_by_player = [row.count(True) for row in match_results_matrix]
        
        list_of_pending_opponents_by_player = [[] for _ in range(number_of_players)]
        missing_matches_count_by_player = [0] * number_of_players
        
        for player_index in range(number_of_players):
            for opponent_index in range(player_index + 1, number_of_players):
                if match_results_matrix[player_index][opponent_index] is None:
                    list_of_pending_opponents_by_player[player_index].append(opponent_index)
                    missing_matches_count_by_player[player_index] += 1
        
        memoization_dictionary = {}
        target_win_count = number_of_players // 2

        def count_valid_outcomes(current_player_index, current_win_counts):

            memoization_key = (current_player_index, tuple(current_win_counts))
            
            if memoization_key in memoization_dictionary:
                return memoization_dictionary[memoization_key]
            
            if current_player_index == number_of_players:
                return 1
            
            number_of_matches_player_should_lose = missing_matches_count_by_player[current_player_index] - (target_win_count - current_win_counts[current_player_index])
            
            if number_of_matches_player_should_lose < 0 or number_of_matches_player_should_lose > missing_matches_count_by_player[current_player_index]:
                return 0
            
            total_valid_combinations = 0

            for lose_to_indices in generate_combinations(
                list_of_pending_opponents_by_player[current_player_index], 
                number_of_matches_player_should_lose
            ):
                next_win_counts = current_win_counts[:]
                for opponent_index in lose_to_indices:
                    next_win_counts[opponent_index] += 1
                total_valid_combinations += count_valid_outcomes(
                    current_player_index + 1,
                    next_win_counts
                )

            memoization_dictionary[memoization_key] = total_valid_combinations
            
            return total_valid_combinations

        print(count_valid_outcomes(0, win_counts_by_player))

main()