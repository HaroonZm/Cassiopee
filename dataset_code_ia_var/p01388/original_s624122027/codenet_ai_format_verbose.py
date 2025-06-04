user_input_string = str(input())

maximum_complete_cups = 0

count_k_letters = user_input_string.count('K')
count_u_letters = user_input_string.count('U')
count_p_letters = user_input_string.count('P')
count_c_letters = user_input_string.count('C')

while True:

    if (
        count_k_letters == 0
        or count_u_letters == 0
        or count_p_letters == 0
        or count_c_letters == 0
    ):
        break

    else:
        maximum_complete_cups += 1
        count_k_letters -= 1
        count_u_letters -= 1
        count_p_letters -= 1
        count_c_letters -= 1

print(maximum_complete_cups)