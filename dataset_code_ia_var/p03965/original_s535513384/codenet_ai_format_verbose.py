user_input_string = input()

number_of_rounds = len(user_input_string)

gu_counter = 0
pa_counter = 0

def get_janken_score(my_hand, opponent_hand):
    if (my_hand == "g") and (opponent_hand == "p"):
        return -1
    elif (my_hand == "p") and (opponent_hand == "g"):
        return 1
    else:
        return 0

total_score = 0

for round_index in range(number_of_rounds):

    if gu_counter == pa_counter:

        total_score = total_score + get_janken_score("g", user_input_string[round_index])
        gu_counter = gu_counter + 1

    else:

        total_score = total_score + get_janken_score("p", user_input_string[round_index])
        pa_counter = pa_counter + 1

print(total_score)