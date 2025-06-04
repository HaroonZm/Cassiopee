user_input_string = input()

for character_index in range(len(user_input_string)):

    character_occurrences = user_input_string.count(user_input_string[character_index])

    if character_occurrences % 2 != 0:

        print('No')

        exit()

print('Yes')