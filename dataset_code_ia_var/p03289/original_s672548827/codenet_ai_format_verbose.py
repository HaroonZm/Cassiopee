user_input_characters = [character for character in input()]

first_character_is_uppercase_a = user_input_characters[0] == "A"
substring_between_second_and_last_has_exactly_one_uppercase_c = user_input_characters[2:-1].count("C") == 1

if first_character_is_uppercase_a and substring_between_second_and_last_has_exactly_one_uppercase_c:

    user_input_characters.remove("A")
    user_input_characters.remove("C")

    remaining_characters_as_string = "".join(user_input_characters)

    all_remaining_characters_are_lowercase = remaining_characters_as_string.islower()

    if all_remaining_characters_are_lowercase:
        print("AC")
    else:
        print("WA")
else:
    print("WA")