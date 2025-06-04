user_input = input()

forbidden_uppercase_letters = 'BDEFGHIJKLMNOPQRSTUVWXYZ'

is_first_character_A = (user_input[0] == 'A')
count_of_A_in_string = user_input.count('A')
count_of_C_in_string = user_input.count('C')
count_of_C_in_middle_substring = user_input[2:-1].count('C')

if (
    is_first_character_A
    and count_of_A_in_string == 1
    and count_of_C_in_string == 1
    and count_of_C_in_middle_substring == 1
):
    for forbidden_letter in forbidden_uppercase_letters:
        if forbidden_letter in user_input:
            break
    else:
        print('AC')
        exit()

print('WA')