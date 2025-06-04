def calculate_check_digit(digits_list):
    weighted_sum = 0
    for position_index in range(11):
        current_digit = int(digits_list[position_index])
        if position_index <= 4:
            weight = 6 - position_index
        else:
            weight = 12 - position_index
        weighted_sum += current_digit * weight
    mod_result = weighted_sum % 11
    if mod_result <= 1:
        return 0
    else:
        return 11 - mod_result

input_digits = list(input())
unknown_index = input_digits.index('?')
if unknown_index == 11:
    print(calculate_check_digit(input_digits))
else:
    possible_solutions = []
    for candidate_digit in range(10):
        input_digits[unknown_index] = str(candidate_digit)
        if int(input_digits[11]) == calculate_check_digit(input_digits):
            possible_solutions.append(candidate_digit)
    if len(possible_solutions) == 1:
        print(possible_solutions[0])
    else:
        print("MULTIPLE")