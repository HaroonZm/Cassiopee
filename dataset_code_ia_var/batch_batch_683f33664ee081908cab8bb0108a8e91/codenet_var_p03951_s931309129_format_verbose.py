number_of_characters = int(input())

first_string = input()

second_string = input()

for concatenated_length in range(number_of_characters, 2 * number_of_characters + 1):

    substring_from_first = first_string[concatenated_length - number_of_characters :]

    substring_from_second = second_string[:2 * number_of_characters - concatenated_length]

    if substring_from_first == substring_from_second:

        print(concatenated_length)

        exit()