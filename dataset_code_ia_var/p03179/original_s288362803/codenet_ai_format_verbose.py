number_of_positions = int(input())
inequality_sequence = input()
modulo = 10 ** 9 + 7

remaining_numbers = number_of_positions - 1
ways_to_form_sequence = [1] * number_of_positions

for current_inequality in inequality_sequence:

    updated_ways = [0] * number_of_positions

    if current_inequality == "<":

        for count_unused_right in range(remaining_numbers + 1):
            if count_unused_right >= 1:
                updated_ways[count_unused_right - 1] = (
                    (ways_to_form_sequence[count_unused_right] + updated_ways[count_unused_right - 1]) % modulo
                )

        ways_to_form_sequence = updated_ways

        for index in range(number_of_positions - 2, -1, -1):
            ways_to_form_sequence[index] = (
                (ways_to_form_sequence[index + 1] + ways_to_form_sequence[index]) % modulo
            )

    else:

        reversed_ways = [ways_to_form_sequence[remaining_numbers - idx] for idx in range(number_of_positions)]
        ways_to_form_sequence = reversed_ways

        for count_unused_right in range(remaining_numbers + 1):
            if count_unused_right >= 1:
                updated_ways[count_unused_right - 1] = (
                    (ways_to_form_sequence[count_unused_right] + updated_ways[count_unused_right - 1]) % modulo
                )

        ways_to_form_sequence = updated_ways

        for index in range(number_of_positions - 2, -1, -1):
            ways_to_form_sequence[index] = (
                (ways_to_form_sequence[index + 1] + ways_to_form_sequence[index]) % modulo
            )

        re_reversed_ways = [ways_to_form_sequence[remaining_numbers - 1 - idx] for idx in range(number_of_positions)]
        ways_to_form_sequence = re_reversed_ways

    remaining_numbers -= 1

print(ways_to_form_sequence[0])