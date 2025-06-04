user_input_string = input()

unique_characters_dictionary = {}

for character_index in range(len(user_input_string)):
    current_character = user_input_string[character_index]
    unique_characters_dictionary[current_character] = 1

if len(user_input_string) == len(unique_characters_dictionary):
    print("yes")
else:
    print("no")