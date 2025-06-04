while True:

    number_of_iterations = input()
    
    if number_of_iterations == 0:
        break

    input_string = raw_input() + ' '
    
    for iteration_index in range(number_of_iterations):

        consecutive_character_count = 1
        compressed_string = ''

        for character_index in range(len(input_string) - 1):

            if input_string[character_index] == input_string[character_index + 1]:
                consecutive_character_count += 1
            else:
                compressed_string += "%d%s" % (consecutive_character_count, input_string[character_index])
                consecutive_character_count = 1

        input_string = compressed_string + ' '
    
    print input_string.rstrip()