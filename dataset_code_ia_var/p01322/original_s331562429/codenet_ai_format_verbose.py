while True:

    number_of_patterns, number_of_inputs = map(int, input().split())

    if number_of_patterns == 0 and number_of_inputs == 0:
        break

    pattern_list = [ [] for _ in range(number_of_patterns) ]

    for pattern_index in range(number_of_patterns):

        pattern_definition = input().split()

        pattern_list[pattern_index] = [
            list(pattern_definition[0]),      # Pattern as list of chars
            int(pattern_definition[1])        # Associated score
        ]

    total_score = 0

    for _ in range(number_of_inputs):

        input_string_characters = list(input())

        for pattern_index in range(number_of_patterns):

            pattern_characters = pattern_list[pattern_index][0]
            pattern_score = pattern_list[pattern_index][1]

            pattern_matches = True

            for character_index in range(8):
                if (
                    pattern_characters[character_index] != '*' and
                    pattern_characters[character_index] != input_string_characters[character_index]
                ):
                    pattern_matches = False
                    break

            if pattern_matches:
                total_score += pattern_score
                break

    print(total_score)