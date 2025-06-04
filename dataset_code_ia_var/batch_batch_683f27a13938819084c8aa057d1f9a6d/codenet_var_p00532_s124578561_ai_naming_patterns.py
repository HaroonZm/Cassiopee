input_count_main = int(input())
input_count_rounds = int(input())
initial_values_list = list(map(int, input().split()))
score_list = [0] * input_count_main
for round_index in range(input_count_rounds):
    round_values_list = list(map(int, input().split()))
    for player_index in range(input_count_main):
        if initial_values_list[round_index] == round_values_list[player_index]:
            score_list[player_index] += 1
        else:
            score_list[initial_values_list[round_index] - 1] += 1
_, = map(print, score_list)