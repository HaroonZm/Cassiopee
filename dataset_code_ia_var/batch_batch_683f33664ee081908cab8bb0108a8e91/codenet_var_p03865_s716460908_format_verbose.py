user_input_characters = list(input())

number_of_characters = len(user_input_characters)

first_character = user_input_characters[0]
last_character = user_input_characters[-1]

string_length_is_even = (number_of_characters % 2 == 0)

if first_character == last_character:

    if string_length_is_even:
        print("First")
    else:
        print("Second")

else:

    if string_length_is_even:
        print("Second")
    else:
        print("First")