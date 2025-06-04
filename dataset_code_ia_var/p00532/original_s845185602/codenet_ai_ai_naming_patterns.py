num_players = int(input())
num_rounds = int(input())

answer_list = list(map(int, input().split()))
guess_matrix = [list(map(int, input().split())) for round_index in range(num_rounds)]

score_list = [0 for player_index in range(num_players)]

for round_index in range(num_rounds):
    incorrect_count = 0
    for player_index in range(num_players):
        if answer_list[round_index] == guess_matrix[round_index][player_index]:
            score_list[player_index] += 1
        else:
            incorrect_count += 1
    score_list[answer_list[round_index] - 1] += incorrect_count

for player_index in range(num_players):
    print(score_list[player_index])