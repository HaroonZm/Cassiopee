def get_all_divisors(integer_number):

    list_of_divisors = []

    for potential_divisor in range(1, int(integer_number ** 0.5) + 1):

        if integer_number % potential_divisor == 0:

            list_of_divisors.append(potential_divisor)

            corresponding_divisor = integer_number // potential_divisor

            if potential_divisor != corresponding_divisor:

                list_of_divisors.append(corresponding_divisor)

    list_of_divisors.sort()

    return list_of_divisors


input_integer = int(input())

divisors_of_input = get_all_divisors(input_integer)

sum_of_valid_values = 0

for current_divisor in divisors_of_input:

    candidate_value = input_integer // current_divisor - 1

    if candidate_value != 0:

        if (input_integer % candidate_value) == (input_integer // candidate_value):

            sum_of_valid_values += candidate_value

print(sum_of_valid_values)