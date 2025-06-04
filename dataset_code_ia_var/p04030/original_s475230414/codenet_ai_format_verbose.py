user_input_string = input()

user_input_length = len(user_input_string)

final_character_list = []

for current_index in range(user_input_length):

    current_character = user_input_string[current_index]

    if current_character == '0':

        final_character_list.append('0')

    elif current_character == '1':

        final_character_list.append('1')

    else:

        if final_character_list != []:

            final_character_list.pop(-1)

final_list_length = len(final_character_list)

for output_index in range(final_list_length - 1):

    print(final_character_list[output_index], end="")

print(final_character_list[final_list_length - 1])