user_input_characters_list = list(input())

unique_characters_set = set(user_input_characters_list)

if len(user_input_characters_list) == len(unique_characters_set):

    print('yes')

else:

    print('no')