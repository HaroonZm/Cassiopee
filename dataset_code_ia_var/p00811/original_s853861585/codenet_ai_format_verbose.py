import math

def get_prime_flags_up_to(limit):

    is_prime_flag_list = [False, False]

    is_prime_flag_list += [True for current_number in range(2, limit + 1)]

    upper_bound = int(math.sqrt(limit)) + 1

    current_divisor = 2

    while current_divisor <= upper_bound:

        if not is_prime_flag_list[current_divisor]:

            current_divisor += 1

            continue

        multiple = 2

        while current_divisor * multiple <= limit:

            is_prime_flag_list[current_divisor * multiple] = False

            multiple += 1

        current_divisor += 1

    return is_prime_flag_list



prime_number_flags = get_prime_flags_up_to(50000)

while True:

    input_values = raw_input().split(" ")

    maximum_value, minimum_aspect_ratio_numerator, maximum_aspect_ratio_denominator = map(int, input_values)

    if (maximum_value, minimum_aspect_ratio_numerator, maximum_aspect_ratio_denominator) == (0, 0, 0):

        break

    largest_rectangle = (0, 0, 0)

    candidate_larger_side = maximum_value // 2

    while candidate_larger_side >= 2:

        if not prime_number_flags[candidate_larger_side]:

            candidate_larger_side -= 1

            continue

        candidate_smaller_side = min(maximum_value // candidate_larger_side + 1, candidate_larger_side)

        while candidate_smaller_side * maximum_aspect_ratio_denominator >= candidate_larger_side * minimum_aspect_ratio_numerator:

            if (not prime_number_flags[candidate_smaller_side] or 
               candidate_smaller_side * candidate_larger_side > maximum_value):

                candidate_smaller_side -= 1

                continue

            if largest_rectangle[0] <= candidate_smaller_side * candidate_larger_side:

                largest_rectangle = (
                    candidate_smaller_side * candidate_larger_side,
                    candidate_smaller_side,
                    candidate_larger_side
                )

            candidate_smaller_side -= 1

        candidate_larger_side -= 1

    print largest_rectangle[1], largest_rectangle[2]