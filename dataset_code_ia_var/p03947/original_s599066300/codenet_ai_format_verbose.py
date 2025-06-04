input_string = input()

length_of_input = len(input_string)

number_of_switches = 0

current_index = 0

if input_string[0] == "B":

    while current_index <= length_of_input - 2:

        if input_string[current_index] == "B" and input_string[current_index + 1] == "W":

            number_of_switches += 1

            current_index += 2

        else:

            current_index += 1

    if input_string[-1] == "W":

        result = str(number_of_switches * 2 - 1)

    else:

        result = str(number_of_switches * 2)

    print(result)

else:

    while current_index <= length_of_input - 2:

        if input_string[current_index] == "W" and input_string[current_index + 1] == "B":

            number_of_switches += 1

            current_index += 2

        else:

            current_index += 1

    if input_string[-1] == "B":

        result = str(number_of_switches * 2 - 1)

    else:

        result = str(number_of_switches * 2)

    print(result)