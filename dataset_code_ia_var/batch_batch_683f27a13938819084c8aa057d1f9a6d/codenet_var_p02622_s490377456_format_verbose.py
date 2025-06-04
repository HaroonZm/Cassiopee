first_string = input()
second_string = input()

number_of_differences = 0

for character_index in range(len(first_string)):

    if first_string[character_index] != second_string[character_index]:
        number_of_differences += 1

print(number_of_differences)