INFINITY_CONSTANT = 10 ** 10
MODULO = 10 ** 9 + 7

def count_possible_solutions(first_number_str, second_number_str, result_number_str):

    reversed_first_number = first_number_str[::-1]
    reversed_second_number = second_number_str[::-1]
    reversed_result_number = result_number_str[::-1]

    carry_possibilities_previous_digit = [1, 0, 0]
    total_digits = len(reversed_first_number)

    for digit_index in range(total_digits):

        carry_possibilities_current_digit = [0] * 3

        start_digit = 0
        if digit_index == total_digits - 1:
            start_digit = 1

        for carry_in in range(3):

            for digit_first in range(start_digit, 10):

                if reversed_first_number[digit_index] != '?' and int(reversed_first_number[digit_index]) != digit_first:
                    continue

                for digit_second in range(start_digit, 10):

                    if reversed_second_number[digit_index] != '?' and int(reversed_second_number[digit_index]) != digit_second:
                        continue

                    for digit_result in range(start_digit, 10):

                        if reversed_result_number[digit_index] != '?' and int(reversed_result_number[digit_index]) != digit_result:
                            continue

                        sum_digits = carry_in + digit_first + digit_second

                        if sum_digits % 10 != digit_result:
                            continue

                        carry_out = sum_digits // 10

                        carry_possibilities_current_digit[carry_out] += carry_possibilities_previous_digit[carry_in]
                        carry_possibilities_current_digit[carry_out] %= MODULO

        carry_possibilities_previous_digit = carry_possibilities_current_digit

    solution_count = carry_possibilities_previous_digit[0]
    print(solution_count)

def main():

    while True:

        input_first_number = input()
        if input_first_number == '0':
            return

        input_second_number = input()
        input_result_number = input()

        count_possible_solutions(input_first_number, input_second_number, input_result_number)

if __name__ == '__main__':
    main()