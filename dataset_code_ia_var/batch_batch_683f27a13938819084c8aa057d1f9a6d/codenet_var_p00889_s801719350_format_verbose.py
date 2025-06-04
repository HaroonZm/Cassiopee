from collections import defaultdict

def digit_sequence_generator(sequence_length, seed_value, xor_value):
    current_value = seed_value

    for index in range(sequence_length):
        generated_digit = (current_value // 7) % 10
        yield generated_digit

        if current_value % 2 == 0:
            current_value //= 2
        else:
            current_value = (current_value // 2) ^ xor_value

def solve_problem_instance():
    sequence_length, seed_value, xor_value, divisor = map(int, input().split())

    if sequence_length == 0:
        return False

    generated_digits = list(digit_sequence_generator(sequence_length, seed_value, xor_value))

    result_count = 0

    if divisor == 2 or divisor == 5:
        non_zero_digit_counter = 0
        for digit_index in range(sequence_length):
            current_digit = generated_digits[digit_index]

            if current_digit != 0:
                non_zero_digit_counter += 1

            if current_digit % divisor == 0:
                result_count += non_zero_digit_counter

    else:
        modular_power_of_ten = pow(10, divisor - 2, divisor)
        prefix_sum_counter = defaultdict(int)
        prefix_sum_counter[0] = 1

        current_prefix_sum = 0
        power_of_ten_mod = 1
        leading_zero_flag = 1

        for digit_index in range(sequence_length):
            current_digit = generated_digits[digit_index]

            if leading_zero_flag and current_digit == 0:
                continue

            current_prefix_sum = (current_prefix_sum + power_of_ten_mod * current_digit) % divisor
            power_of_ten_mod = (power_of_ten_mod * modular_power_of_ten) % divisor

            result_count += prefix_sum_counter[current_prefix_sum]

            if digit_index < sequence_length - 1 and generated_digits[digit_index + 1] != 0:
                prefix_sum_counter[current_prefix_sum] += 1

            leading_zero_flag = 0

    print(result_count)
    return True

while solve_problem_instance():
    pass