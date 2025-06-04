alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:

    number_of_operations = input()

    if number_of_operations == 0:
        break

    string_characters = list(raw_input())

    operation_indices = [map(int, raw_input().split()) for _ in range(number_of_operations)]

    for start_index, end_index in operation_indices[::-1]:

        index_difference = abs(start_index - end_index)

        new_char_at_start = alphabet[(alphabet.index(string_characters[end_index - 1]) + index_difference) % 26]
        new_char_at_end = alphabet[(alphabet.index(string_characters[start_index - 1]) + index_difference) % 26]

        string_characters[start_index - 1] = new_char_at_start
        string_characters[end_index - 1] = new_char_at_end

    print "".join(string_characters)