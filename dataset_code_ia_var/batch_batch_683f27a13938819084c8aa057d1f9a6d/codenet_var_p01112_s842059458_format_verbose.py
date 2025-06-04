from collections import defaultdict

def count_possible_distributions(number_of_players):
    
    number_of_constraints = int(input())
    
    pair_indices_map = defaultdict(int)
    pair_index_counter = 0
    
    for player_a in range(1, number_of_players + 1):
        for player_b in range(player_a + 1, number_of_players + 1):
            pair_indices_map[pair_index_counter] = (player_a, player_b)
            pair_index_counter += 1
    
    constraint_map = defaultdict(int)
    
    for _ in range(number_of_constraints):
        constrained_winner, constrained_loser = map(int, input().split())
        constraint_map[(constrained_winner, constrained_loser)] = 1
        constraint_map[(constrained_loser, constrained_winner)] = -1
    
    configurations_count = defaultdict(int)
    initial_win_counts = [0] * number_of_players
    configurations_count[tuple(initial_win_counts)] = 1
    
    for current_pair_index in range(pair_index_counter):
        updated_configurations_count = defaultdict(int)
        for player_wins_tuple, current_configuration_count in configurations_count.items():
            player_wins_list = list(player_wins_tuple)
            player_x, player_y = pair_indices_map[current_pair_index]
            if constraint_map[(player_x, player_y)]:
                if constraint_map[(player_x, player_y)] == 1:
                    if player_wins_list[player_x - 1] == number_of_players // 2:
                        continue
                    player_wins_list[player_x - 1] += 1
                    updated_configurations_count[tuple(player_wins_list)] += current_configuration_count
                else:
                    if player_wins_list[player_y - 1] == number_of_players // 2:
                        continue
                    player_wins_list[player_y - 1] += 1
                    updated_configurations_count[tuple(player_wins_list)] += current_configuration_count
            else:
                if player_wins_list[player_y - 1] != number_of_players // 2:
                    player_wins_list[player_y - 1] += 1
                    updated_configurations_count[tuple(player_wins_list)] += current_configuration_count
                    player_wins_list[player_y - 1] -= 1
                if player_wins_list[player_x - 1] != number_of_players // 2:
                    player_wins_list[player_x - 1] += 1
                    updated_configurations_count[tuple(player_wins_list)] += current_configuration_count
        configurations_count = updated_configurations_count
    
    print(
        configurations_count[tuple([number_of_players // 2] * number_of_players)]
    )

if __name__ == "__main__":
    while True:
        number_of_players = int(input())
        if number_of_players:
            count_possible_distributions(number_of_players)
        else:
            break