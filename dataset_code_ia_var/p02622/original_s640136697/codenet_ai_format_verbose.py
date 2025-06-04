first_string_characters = list(input())

second_string_characters = list(input())

number_of_differences = 0

for character_index in range(len(first_string_characters)):

    if first_string_characters[character_index] != second_string_characters[character_index]:

        number_of_differences += 1

print(number_of_differences)