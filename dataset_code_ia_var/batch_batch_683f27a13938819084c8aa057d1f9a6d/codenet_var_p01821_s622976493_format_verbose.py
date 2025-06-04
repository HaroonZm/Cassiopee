number_input = int(input())


def compute_greatest_common_divisor(integer_a, integer_b):
    while integer_b:
        integer_a, integer_b = integer_b, integer_a % integer_b
    return integer_a


def compute_least_common_multiple(integer_a, integer_b):
    return integer_a // compute_greatest_common_divisor(integer_a, integer_b) * integer_b


def compute_carmichael_function(target_value):
    current_least_common_multiple = 1

    current_power_of_two = 0
    temp_target = target_value
    while temp_target & 1 == 0:
        current_power_of_two += 1
        temp_target >>= 1

    if current_power_of_two > 1:
        if current_power_of_two == 2:
            current_least_common_multiple = 2
        else:
            current_least_common_multiple = 2 ** (current_power_of_two - 2)

    current_prime_factor = 3
    while current_prime_factor * current_prime_factor <= temp_target:
        if temp_target % current_prime_factor == 0:
            exponent_prime_factor = 0
            while temp_target % current_prime_factor == 0:
                temp_target //= current_prime_factor
                exponent_prime_factor += 1
            current_least_common_multiple = compute_least_common_multiple(
                current_least_common_multiple,
                (current_prime_factor - 1) * current_prime_factor ** (exponent_prime_factor - 1)
            )
        current_prime_factor += 1

    if temp_target > 1:
        current_least_common_multiple = compute_least_common_multiple(
            current_least_common_multiple,
            temp_target - 1
        )

    return current_least_common_multiple


def compute_multiplicative_order(base, modulus):
    if modulus == 1:
        return 1

    reduced_base = base % modulus
    baby_step_limit = int(modulus ** 0.5) + 1

    value_to_exponent_mapping = {}
    current_value = 1

    for exponent_baby_step in range(baby_step_limit):
        value_to_exponent_mapping[current_value] = exponent_baby_step
        current_value = (current_value * reduced_base) % modulus
        if current_value == 1:
            return exponent_baby_step + 1
        if current_value in value_to_exponent_mapping:
            return -1

    accumulated_value = 1
    for exponent_giant_step in range(baby_step_limit):
        accumulated_value = (accumulated_value * current_value) % modulus
        if accumulated_value in value_to_exponent_mapping:
            return baby_step_limit * (exponent_giant_step + 1) - value_to_exponent_mapping[accumulated_value]

    return -1


carmichael_of_input = compute_carmichael_function(number_input)

multiplicative_order_result = compute_multiplicative_order(number_input, carmichael_of_input)

if (
    multiplicative_order_result == -1 or
    pow(number_input, multiplicative_order_result, carmichael_of_input) != (1 % carmichael_of_input)
):
    print(-1)
else:
    print(multiplicative_order_result)