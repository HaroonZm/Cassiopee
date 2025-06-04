user_input_string = input()

first_character_is_uppercase_A = user_input_string[0] == "A"

substring_between_second_and_penultimate_characters = user_input_string[2:-1]
number_of_uppercase_C_in_substring = substring_between_second_and_penultimate_characters.count("C")

substring_from_second_character_onward = user_input_string[1:]
lowercase_version_of_substring = substring_from_second_character_onward.replace("C", "c")
all_remaining_characters_are_lowercase = lowercase_version_of_substring.islower()

if (
    first_character_is_uppercase_A
    and number_of_uppercase_C_in_substring == 1
    and all_remaining_characters_are_lowercase
):
    print("AC")
    exit()

print("WA")