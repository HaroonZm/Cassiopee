user_input_string = input()

alphabet_characters = 'abc'

number_of_unique_characters_with_single_occurrence = sum(
    1
    if user_input_string.count(character) == 1
    else 0
    for character in alphabet_characters
)

if number_of_unique_characters_with_single_occurrence == 3:
    result_message = 'Yes'
else:
    result_message = 'No'

print(result_message)